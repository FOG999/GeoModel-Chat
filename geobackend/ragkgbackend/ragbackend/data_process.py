from utils import *

import os
from glob import glob
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import CSVLoader, PyMuPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def doc2vec():
    # 定义文本分割器
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    # 读取并分割文件
    dir_path = os.path.join(os.path.dirname(__file__), './data/inputs/')
    print(dir_path)

    documents = []
    # 使用glob遍历文件夹
    for file_path in glob(dir_path + '*.*'):
        loader = None
        if file_path.endswith('.csv'):
            loader = CSVLoader(file_path, encoding='utf-8')  # 指定编码为 UTF-8
        elif file_path.endswith('.pdf'):
            loader = PyMuPDFLoader(file_path)
        elif file_path.endswith('.txt'):
            loader = TextLoader(file_path, encoding='utf-8')  # 指定编码为 UTF-8
        if loader:
            documents += loader.load_and_split(text_splitter)
    print(documents)

    # 向量化并缓存存储
    if documents:
        vdb = Chroma.from_documents(
            documents = documents, 
            embedding = get_embeddings_model(),
            persist_directory = os.path.join(os.path.dirname(__file__), './data/db/')
            # 持久化存储到设置好的文件夹
        )
        vdb.persist()


if __name__ == '__main__':
    doc2vec() 