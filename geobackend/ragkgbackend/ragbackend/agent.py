import subprocess
import os
from utils import *
from config import *
from prompt import *
import graphrag

import langchain.agents as agents
# print(dir(agents))

import os
from langchain.chains import LLMChain, LLMRequestsChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores.chroma import Chroma
from langchain.vectorstores.faiss import FAISS
from langchain.schema import Document
from langchain.agents import ZeroShotAgent, AgentExecutor, Tool, create_json_agent
from langchain.memory import ConversationBufferMemory
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain import hub


class Agent():
    def __init__(self):
        # pass
        self.vdb = Chroma(
            persist_directory = os.path.join(os.path.dirname(__file__), './data/db'), 
            embedding_function = get_embeddings_model()
        )
         # 定义 graphrag 的 root 路径
        self.graphrag_root = "/home/nzj/ragkgbackend/ragtest"

    def generic_func(self,x,query):
        prompt = PromptTemplate.from_template(GENERIC_PROMPT_TPL)
        llm_chain = LLMChain(
            llm = get_llm_model(), 
            prompt = prompt,
            verbose = os.getenv('VERBOSE')
        )
        return llm_chain.run(query)

    def retrival_func(self,x,query):
        # 召回并过滤文档
        documents = self.vdb.similarity_search_with_relevance_scores(query, k=5)
        # print(documents)
        # exit()
        query_result = [doc[0].page_content for doc in documents if doc[1]>0.7]
        # print(query_result)

        # 填充提示词并总结答案
        prompt = PromptTemplate.from_template(RETRIVAL_PROMPT_TPL)
        retrival_chain = LLMChain(
            llm = get_llm_model(),
            prompt = prompt,
            verbose = os.getenv('VERBOSE')
        )
        inputs = {
            'query': query,
            'query_result': '\n\n'.join(query_result) if len(query_result) else '没有查到'
            # '\n\n'把“query_result”的list拼接成字符串
        }
        return retrival_chain.invoke(inputs)['text']

    # def graph_func(self,x,query):
    #     # 命名实体识别
    #     response_schemas = [
    #         ResponseSchema(type='list', name='disease', description='疾病名称实体'),
    #         ResponseSchema(type='list', name='symptom', description='疾病症状实体'),
    #         ResponseSchema(type='list', name='drug', description='药品名称实体'),
    #     ]

    #     output_parser = StructuredOutputParser(response_schemas=response_schemas)
    #     format_instructions = structured_output_parser(response_schemas)

    #     ner_prompt = PromptTemplate(
    #         template = NER_PROMPT_TPL,
    #         partial_variables = {'format_instructions': format_instructions},
    #         input_variables = ['query']
    #     )

    #     ner_chain = LLMChain(
    #         llm = get_llm_model(),
    #         prompt = ner_prompt,
    #         verbose = os.getenv('VERBOSE')
    #     )

    #     result = ner_chain.invoke({
    #         'query': query
    #     })['text']
        
        
    #     ner_result = output_parser.parse(result)
    #     # 从用户输入的问题中抽取实体
    #     print(ner_result)
    #     # exit()

    #     # 命名实体识别结果，填充模板
    #     graph_templates = []
    #     for key, template in GRAPH_TEMPLATE.items():
    #         slot = template['slots'][0]
    #         slot_values = ner_result[slot]
    #         # print(slot,slot_values)
    #         # exit()
    #         for value in slot_values:
    #             graph_templates.append({
    #                 'question': replace_token_in_string(template['question'], [[slot, value]]),
    #                 'cypher': replace_token_in_string(template['cypher'], [[slot, value]]),
    #                 'answer': replace_token_in_string(template['answer'], [[slot, value]]),
    #             })
    #     # print(graph_templates)
    #     # exit()
    #     if not graph_templates:
    #         return 
        
    #     # 计算问题相似度，筛选最相关问题----对config替换完的所有模板进行筛选
    #     graph_documents = [
    #         Document(page_content=template['question'], metadata=template)
    #         for template in graph_templates
    #     ]
    #     # print(graph_documents)
    #     # exit()
    #     # 对问题进行向量化计算，取前三
    #     db = FAISS.from_documents(graph_documents, get_embeddings_model())
    #     graph_documents_filter = db.similarity_search_with_relevance_scores(query, k=3)
    #     print(graph_documents_filter)

    #     # 执行CQL，拿到结果
    #     query_result = []
    #     neo4j_conn = get_neo4j_conn()
    #     for document in graph_documents_filter:
    #         question = document[0].page_content
    #         cypher = document[0].metadata['cypher']
    #         answer = document[0].metadata['answer']
    #         # 查询的问题
    #         # print(question)
    #         try:
    #             result = neo4j_conn.run(cypher).data()
    #             # CQL查询的结果
    #             # print(result)
    #             # exit()
    #             if result and any(value for value in result[0].values()):
    #                 answer_str = replace_token_in_string(answer, list(result[0].items()))
    #                 query_result.append(f'问题：{question}\n答案：{answer_str}')
    #         except:
    #             pass
    #     # print(query_result)
            
    #     # 总结答案
    #     prompt = PromptTemplate.from_template(GRAPH_PROMPT_TPL)
    #     graph_chain = LLMChain(
    #         llm = get_llm_model(),
    #         prompt = prompt,
    #         verbose = os.getenv('VERBOSE')
    #     )
    #     inputs = {
    #         'query': query,
    #         'query_result': '\n\n'.join(query_result) if len(query_result) else '没有查到'
    #     }
    #     return graph_chain.invoke(inputs)['text']
    def format_answer(self, result):
        """对 Graphrag 返回的结果进行格式化"""
        if not result:
            return "未找到相关信息。"
        return result.strip()
    
    def graph_func(self, x, query):
        """集成 Graphrag 的局部搜索和全局搜索"""
        try:
            # 1. 优先执行局部搜索
            local_search_cmd = [
                "python",
                "-m",
                "graphrag.query",
                "--root",
                self.graphrag_root,
                "--method",
                "local",
                query
            ]
            local_search_result = subprocess.run(
                local_search_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if local_search_result.returncode == 0 and local_search_result.stdout.strip():
                # 局部搜索有结果
                answer = self.format_answer(local_search_result.stdout.strip())
            else:
                # 2. 如果局部搜索没有结果，调用全局搜索
                global_search_cmd = [
                    "python",
                    "-m",
                    "graphrag.query",
                    "--root",
                    self.graphrag_root,
                    "--method",
                    "global",
                    query
                ]
                global_search_result = subprocess.run(
                    global_search_cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                if global_search_result.returncode == 0 and global_search_result.stdout.strip():
                    # 全局搜索有结果
                    answer = self.format_answer(global_search_result.stdout.strip())
                else:
                    # 如果全局搜索也没有结果，返回默认回答
                    answer = "未找到相关信息。"

            # 3. 使用一个提示模板，确保返回值格式化一致
            prompt = PromptTemplate.from_template(GRAPH_PROMPT_TPL)
            graph_chain = LLMChain(
                llm=get_llm_model(),
                prompt=prompt,
                verbose=os.getenv('VERBOSE')
            )

            # 构造输入，用于提示模板
            inputs = {
                'query': query,
                'query_result': answer
            }

            # 运行链并返回最终输出
            return graph_chain.invoke(inputs)['text']

        except Exception as e:
            # 捕获和处理异常
            return f"处理 Graphrag 查询时出错: {str(e)}"
    
   
    def search_func(self,query):
        prompt = PromptTemplate.from_template(SEARCH_PROMPT_TPL)
        llm_chain = LLMChain(
            llm = get_llm_model(),
            prompt = prompt,
            verbose = os.getenv('VERBOSE')
        )
        llm_request_chain = LLMRequestsChain(
            llm_chain = llm_chain,
            requests_key = 'query_result'
        )
        inputs = {
            'query': query,
            'url': 'https://www.google.com/search?q='+query.replace(' ', '+')
        }
        return llm_request_chain.invoke(inputs)['output']


# 统一的入口函数
    def query(self, query):
        tools = [
            Tool.from_function(
                name = 'generic_func',
                # func =self.generic_func,
                func = lambda x: self.generic_func(x, query),
                description = '可以解答通用领域的知识，例如打招呼，问你是谁等问题',
            ),
            Tool.from_function(
                name = 'retrival_func',
                func = lambda x: self.retrival_func(x, query),
                description = '用于回答断缝体油藏相关问题，断缝体油藏露头地质知识库的介绍',
            ),
            Tool(
                name = 'graph_func',
                # lambda为匿名函数，x是大模型总结的问题，query是原始的问题
                func = lambda x: self.graph_func(x, query),
                description = '用于回答地质领域相关问题、地质模式相关问题',
            ),
            Tool(
                name = 'search_func',
                func = self.search_func,
                description = '其他工具没有正确答案时，通过搜索引擎，回答通用类问题',
            ),
        ]
        # agent
        prefix = """请用中文，尽你所能回答以下问题。您可以使用以下工具："""
        suffix = """Begin!

        History: {chat_history}
        Question: {input}
        Thought:{agent_scratchpad}"""

        agent_prompt = ZeroShotAgent.create_prompt(
            tools=tools,
            prefix=prefix,
            suffix=suffix,
            input_variables=['input', 'agent_scratchpad', 'chat_history']
        )
        llm_chain = LLMChain(llm=get_llm_model(), prompt=agent_prompt)
        agent = ZeroShotAgent(llm_chain=llm_chain)

        memory = ConversationBufferMemory(memory_key='chat_history')
        agent_chain = AgentExecutor.from_agent_and_tools(
            agent = agent, 
            tools = tools, 
            memory = memory, 
            handle_parsing_errors=True,   
            verbose = os.getenv('VERBOSE'),
            max_iterations=10,  # 设置最大迭代次数
            timeout=60          # 设置超时限制
        )
        return agent_chain.run({'input': query})

    #     prompt = hub.pull('hwchase17/react-chat')
    #     prompt.template = '请用中文回答问题！Final Answer 必须尊重 Obversion 的结果，不能改变语义。\n\n' + prompt.template
    #     agent = create_react_agent(llm=get_llm_model(), tools=tools, prompt=prompt)
    #     memory = ConversationBufferMemory(memory_key='chat_history')
    #     agent_executor = AgentExecutor.from_agent_and_tools(
    #         agent = agent, 
    #         tools = tools, 
    #         memory = memory, 
    #         handle_parsing_errors = True,
    #         verbose = os.getenv('VERBOSE')
    #     )
    #     return agent_executor.invoke({"input": query})['output']


if __name__ == '__main__':
    agent = Agent()

    
    
    
    # print(agent.graph_func('什么是构型特征?'))
    

  