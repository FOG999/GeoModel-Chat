<template>
  <el-container style="height: 100vh; border: 1px solid #ebebeb;">
    <!-- 左侧历史记录 -->
    <el-aside width="300px" style="background-color: #f2f2f2;">
      <el-menu default-active="1" class="el-menu-vertical-demo">
        <el-menu-item index="1">
          <i class="el-icon-message"></i>
          <span slot="title">历史记录</span>
        </el-menu-item>
      </el-menu>
      <el-list>
        <el-list-item v-for="(history, index) in historyList" :key="index" class="history-item">
          <el-card shadow="hover">{{ history }}</el-card>
        </el-list-item>
      </el-list>
    </el-aside>




    <!-- 右侧聊天框 -->
    <el-container>
      <el-header style="background-color: #fff;">
        <h3>ChatGPT 聊天界面</h3>
      </el-header>
      <el-main style="padding: 20px; overflow-y: auto; background-color: #f7f7f7;">
        <el-timeline>
          <el-timeline-item v-for="(message, index) in messages" :key="index" :timestamp="message.timestamp" placement="top">
            <template v-slot:dot>
              <el-avatar size="medium" :icon="message.user === 'ChatGPT' ? 'el-icon-s-custom' : 'el-icon-user-solid'" />
            </template>
            <el-card shadow="hover" style="margin-bottom: 20px;">
              <div>{{ message.user }}: {{ message.text }}</div>
            </el-card>
          </el-timeline-item>
        </el-timeline>
      </el-main>

      <!-- 输入框 -->
      <el-footer style="background-color: #fff; padding: 10px;">
        <el-input v-model="inputMessage" placeholder="输入消息..." @keyup.enter="sendMessage" clearable style="width: 80%;" />
        <el-button type="primary" @click="sendMessage" style="margin-left: 10px;">发送</el-button>
      </el-footer>
    </el-container>
  </el-container>
</template>
<script>
export default {
  name: 'BaseChat',
  data() {
    return {
      messages: [], // 聊天记录
      inputMessage: '', // 当前输入的消息
      historyList: ["Vue聊天室实现", "缺少chromadb包错误", "LangChain导入错误解决"], // 左侧历史记录
    };
  },
  methods: {
    sendMessage() {
      if (this.inputMessage.trim()) {
        const timestamp = new Date().toLocaleTimeString();
        // 添加用户输入的消息
        this.messages.push({ user: 'User', text: this.inputMessage, timestamp });

        // 模拟API请求
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
            this.messages.push({ user: 'ChatGPT', text: data.response, timestamp: new Date().toLocaleTimeString() });
          });

        // 清空输入框
        this.inputMessage = '';
      }
    },
  },
}
</script>

<style scoped>
./* 自定义样式 */
.history-item {
  margin: 10px 0;
}
</style>
