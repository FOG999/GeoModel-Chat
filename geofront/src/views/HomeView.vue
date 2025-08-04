<template>
  <el-container style="height: 100vh; border: none; background-color: #2A2D34;">
    <!-- 左侧历史记录 -->
    <el-aside width="250px" style="background-color: #FFFFFF;">
      <el-menu default-active="1" class="el-menu-vertical-demo" style="border-right: none;">
        <el-menu-item index="1">
          <el-icon><ChatSquare class="view-icon" /></el-icon>
          <span slot="title" style="font-size: 28px; color: #1c1c1c; font-weight: bold;">
            历史记录</span>
        </el-menu-item>
      </el-menu>
      <el-list style="padding: 20px;">
        <el-list-item
          v-for="(history, index) in historyList"
          :key="index"
          class="history-item"
          @click="loadHistory(history.messages)"
        >


          <el-card shadow="always" class="history-card">
            <div style="color: #E0E0E0; font-weight: 600;">{{ history.messages.length > 0 ? '最近对话' : '空会话' }}</div>
            <div v-if="history.messages.length > 0" style="color: #B0B0B0;">
              {{ history.messages.slice(-2).join(' | ') }}
            </div>
          </el-card>
        </el-list-item>
      </el-list>
    </el-aside>

    <!-- 中间聊天框 -->
    <el-container>
      <el-header style="background-color: #FFFFFF; text-align: left;">
        <span style="color: #111111; font-size: 32px; font-weight: bold; letter-spacing: 1px;">
          <svg xmlns="http://www.w3.org/2000/svg" width="38" height="38" fill="currentColor" class="bi bi-gpu-card" viewBox="0 0 16 16">
             <path d="M4 8a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Zm7.5-1.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Z"/>
             <path d="M0 1.5A.5.5 0 0 1 .5 1h1a.5.5 0 0 1 .5.5V4h13.5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5H2v2.5a.5.5 0 0 1-1 0V2H.5a.5.5 0 0 1-.5-.5Zm5.5 4a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5ZM9 8a2.5 2.5 0 1 0 5 0 2.5 2.5 0 0 0-5 0Z"/>
             <path d="M3 12.5h3.5v1a.5.5 0 0 1-.5.5H3.5a.5.5 0 0 1-.5-.5v-1Zm4 1v-1h4v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5Z"/>
          </svg> GIS Chat
        </span>
      </el-header>
      <el-main style="padding: 20px; overflow-y: auto; background-color: #efeeee;">
        <el-timeline :hide-line="true">
          <el-timeline-item
            v-for="(message, index) in messages"
            :key="index"
            :timestamp="message.timestamp"
            placement="top"
          >
            <div v-if="message.user === 'User'" class="message-right">
              <!-- 用户消息 -->
              <el-card shadow="hover" class="message-card user-message-card">
                <!-- 使用 Markdown 渲染消息内容 -->
                <div v-html="renderMarkdown(message.text)"></div>
              </el-card>
              <el-avatar size="medium" icon="el-icon-user-solid" class="user-avatar" />
            </div>
            <div v-else class="message-left">
              <!-- 机器人消息 -->
              <el-avatar size="medium" icon="el-icon-s-custom" class="bot-avatar" />
              <el-card shadow="hover" class="message-card bot-message-card">
                <!-- 使用 Markdown 渲染消息内容 -->
                <div v-html="renderMarkdown(message.text)"></div>
              </el-card>
            </div>
          </el-timeline-item>
        </el-timeline>
      </el-main>

      <!-- 输入框 -->
      <el-footer style="background-color: #1F1F24; padding: 20px; ">
        <el-input v-model="inputMessage" placeholder="输入消息..." @keyup.enter="sendMessage" clearable style="width: 80%; background-color: #3A3F4B; color: white; border: none;" />
        <el-button type="primary" @click="sendMessage" style="margin-left: 10px; background-color: #FF6A3D; border: none;">
          <el-icon><Promotion /></el-icon>
          <span>发送</span>
        </el-button>
        <el-button type="info" @click="startNewSession" style="margin-left: 10px; background-color: #5C6BC0; border: none;">
          <el-icon><Comment /></el-icon>
          <span>建立新会话</span>
        </el-button>
      </el-footer>
    </el-container>

    <!-- 右侧侧边栏 -->
    <el-aside width="450px" style="background-color: #FFFFFF; padding: 3px;">

      <div style="flex: 1; display: flex; flex-direction: column;width: 445px;height: 350px;" >
        <h3 style="color: #1c1c1c; font-weight: bold; font-size: 24px;" >文本图谱</h3>
        <!--        <TxtGraph  style="width: 100%; height: 350px;"  />-->
        <TxtGra  style="width: 100%; height: 350px;"  />
      </div>

      <div style="flex: 1; margin-bottom: 10px;">
        <h3 style="color: #1c1c1c; font-weight: bold;font-size: 24px;">实体图谱</h3>
        <NodesGraph style="width: 100%; height: 500px;" />
      </div>

      <div style="flex: 1;">
        <h3 style="color: #1c1c1c; font-weight: bold;font-size: 24px;">关系图表</h3>
        <el-button type="success" size="small" style="margin-bottom: 10px;">查看关系</el-button>
        <div style="background-color: #efefef; padding: 10px; border-radius: 8px; text-align: center;">
          <p style="color: #999;">关系图表将在这里展示。</p>
        </div>
      </div>
    </el-aside>

  </el-container>
  <FooterBar/>
</template>

<script>
import { ChatSquare, Promotion, Comment } from '@element-plus/icons-vue';
import TxtGraph from '../components/TxtGraph.vue';
import NodesGraph  from '../components/NodesGraph.vue';
import { marked } from 'marked';
import TxtGra from '@/components/TxtGra'
import FooterBar from '@/components/FooterBar' // 引入 Markdown 库

export default {
  name: 'HomeView',
  components: {
    FooterBar,
    TxtGra,
    ChatSquare,
    Promotion,
    Comment,
    TxtGraph,
    NodesGraph,
  },
  data() {
    return {
      messages: [], // 聊天记录
      inputMessage: '', // 当前输入的消息
      historyList: [], // 左侧历史记录
    };
  },
  methods: {
    sendMessage() {
      if (this.inputMessage.trim()) {
        const timestamp = new Date().toLocaleString(); // 使用日期和时间格式
        this.messages.push({ user: 'User', text: this.inputMessage, timestamp });
        fetch('http://localhost:8080/api/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: this.inputMessage }),
        })
          .then(response => response.json())
          .then(data => {
            // 显示服务器回复
            this.messages.push({ user: 'ChatGPT', text: data.response, timestamp: new Date().toLocaleString() });
          })
          .catch(err => {
            console.error('消息发送失败:', err);
          });

        // 清空输入框
        this.inputMessage = '';
      }
    },
    loadHistory(messages) {
      this.messages = messages.map(text => ({
        user: 'ChatGPT',
        text,
        timestamp: new Date().toLocaleString(),
      }));
    },
    startNewSession() {
      this.historyList.push({
        messages: this.messages.map(m => m.text),
      });
      this.messages = [];
    },
    renderMarkdown(text) {
      return marked(text); // 将 Markdown 转换为 HTML
    },
  },
}
</script>

<style scoped>
/* Flex 布局用于用户和机器人的消息区分 */
.message-left {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.message-right {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  margin-bottom: 10px;
}

/* 消息卡片样式 */
.user-message-card {
  background-color: #3A3F4B;
  color: white;
  border-radius: 10px;
  max-width: 60%;
  text-align: right;
  margin-right: 10px;
}

.bot-message-card {
  background-color: #5A5F6A;
  color: white;
  border-radius: 10px;
  max-width: 60%;
  text-align: left;
  margin-left: 10px;
}

/* 头像样式 */
.user-avatar {
  background-color: #FF6A3D;
  margin-left: 10px;
}

.bot-avatar {
  background-color: #5C6BC0;
  margin-right: 10px;
}

/* 历史记录样式 */
.history-item {
  margin-bottom: 20px;
}

.history-card {
  background-color: #3A3F4B;
  color: white;
  border-radius: 10px;
  cursor: pointer;
}

.history-card:hover {
  box-shadow: 0 14px 22px rgba(0, 0, 0, 0.3);
}
.view-icon {
  color: #0c0c0c;
  font-size: 32px;
  font-weight: bold;
}
.sss {
  align-items: center;
  /*margin-top: 40px;*/
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  background-color:#F3F0F0D5
}
</style>

