<template>
  <div class="geochat-app">
    <div class="geochat-mainrow d-flex h-100">
      <!-- 左侧侧栏 -->
      <aside class="geochat-left d-flex flex-column justify-content-between">
        <div class="mt-4">
          <div class="mb-3" style="padding-left: 7px;padding-right: 7px;">
            <div class="sider-card mb-3">
              <div class="sider-title">最近对话</div>
              <div class="sider-content">地质模式中什么是构型特征</div>
            </div>
            <div class="sider-card">
              <div class="sider-title">昨天</div>
              <div class="sider-content text-truncate">
                通常根据孔隙体积的大小、连通性及对流体的有效作用，孔隙度可以分为绝对孔隙度……
              </div>
            </div>
          </div>


        </div>

        <div class="mb-4 px-4">
          <div class="form-check form-switch form-check-reverse">
            <input class="form-check-input" type="checkbox" id="flexSwitchCheckReverse">
            <label class="form-check-label" for="flexSwitchCheckReverse">深色模式</label>
          </div>
          <br>
          <br>
          <button class="btn btn-outline-dark w-100 btn-sm rounded-3" style="background-color: #343a40; color: #fff; ">历史记录</button>
        </div>
      </aside>



      <!-- 主内容区 -->
      <section class="geochat-center d-flex flex-column">
        <!-- 顶部栏 -->
        <header class="d-flex align-items-center pb-0 pt-4 ps-4 pe-0">
          <span class="main-title ms-3">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-gpu-card" viewBox="0 0 16 16">
               <path d="M4 8a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Zm7.5-1.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Z"/>
               <path d="M0 1.5A.5.5 0 0 1 .5 1h1a.5.5 0 0 1 .5.5V4h13.5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5H2v2.5a.5.5 0 0 1-1 0V2H.5a.5.5 0 0 1-.5-.5Zm5.5 4a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5ZM9 8a2.5 2.5 0 1 0 5 0 2.5 2.5 0 0 0-5 0Z"/>
                <path d="M3 12.5h3.5v1a.5.5 0 0 1-.5.5H3.5a.5.5 0 0 1-.5-.5v-1Zm4 1v-1h4v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5Z"/>
            </svg>
            Geo Model Chat</span>
          <div class="flex-grow-1"></div>
        </header>
        <!-- 聊天内容 -->
        <div class="chat-area flex-grow-1 d-flex flex-column py-2 px-4">
          <!-- 用户提问 -->
          <div class="d-flex justify-content-end align-items-end mb-3">
            <div class="user-bubble shadow-sm px-4 py-3">
              请阐述孔隙度的定义及其在岩石物理参数中的重要性，并列出其主要类型及各自特征？
            </div>
            <div class="user-avatar ms-3">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-tsunami" viewBox="0 0 16 16">
                <path d="M.036 12.314a.5.5 0 0 1 .65-.278l1.757.703a1.5 1.5 0 0 0 1.114 0l1.014-.406a2.5 2.5 0 0 1 1.857 0l1.015.406a1.5 1.5 0 0 0 1.114 0l1.014-.406a2.5 2.5 0 0 1 1.857 0l1.015.406a1.5 1.5 0 0 0 1.114 0l1.757-.703a.5.5 0 1 1 .372.928l-1.758.703a2.5 2.5 0 0 1-1.857 0l-1.014-.406a1.5 1.5 0 0 0-1.114 0l-1.015.406a2.5 2.5 0 0 1-1.857 0l-1.014-.406a1.5 1.5 0 0 0-1.114 0l-1.015.406a2.5 2.5 0 0 1-1.857 0l-1.757-.703a.5.5 0 0 1-.278-.65zm0 2a.5.5 0 0 1 .65-.278l1.757.703a1.5 1.5 0 0 0 1.114 0l1.014-.406a2.5 2.5 0 0 1 1.857 0l1.015.406a1.5 1.5 0 0 0 1.114 0l1.014-.406a2.5 2.5 0 0 1 1.857 0l1.015.406a1.5 1.5 0 0 0 1.114 0l1.757-.703a.5.5 0 1 1 .372.928l-1.758.703a2.5 2.5 0 0 1-1.857 0l-1.014-.406a1.5 1.5 0 0 0-1.114 0l-1.015.406a2.5 2.5 0 0 1-1.857 0l-1.014-.406a1.5 1.5 0 0 0-1.114 0l-1.015.406a2.5 2.5 0 0 1-1.857 0l-1.757-.703a.5.5 0 0 1-.278-.65zM2.662 8.08c-.456 1.063-.994 2.098-1.842 2.804a.5.5 0 0 1-.64-.768c.652-.544 1.114-1.384 1.564-2.43.14-.328.281-.68.427-1.044.302-.754.624-1.559 1.01-2.308C3.763 3.2 4.528 2.105 5.7 1.299 6.877.49 8.418 0 10.5 0c1.463 0 2.511.4 3.179 1.058.67.66.893 1.518.819 2.302-.074.771-.441 1.516-1.02 1.965a1.878 1.878 0 0 1-1.904.27c-.65.642-.907 1.679-.71 2.614C11.076 9.215 11.784 10 13 10h2.5a.5.5 0 0 1 0 1H13c-1.784 0-2.826-1.215-3.114-2.585-.232-1.1.005-2.373.758-3.284L10.5 5.06l-.777.388a.5.5 0 0 1-.447 0l-1-.5a.5.5 0 0 1 .447-.894l.777.388.776-.388a.5.5 0 0 1 .447 0l1 .5a.493.493 0 0 1 .034.018c.44.264.81.195 1.108-.036.328-.255.586-.729.637-1.27.05-.529-.1-1.076-.525-1.495-.426-.42-1.19-.77-2.477-.77-1.918 0-3.252.448-4.232 1.123C5.283 2.8 4.61 3.738 4.07 4.79c-.365.71-.655 1.433-.945 2.16-.15.376-.301.753-.463 1.13z"/>
              </svg>
            </div>
          </div>
          <!-- AI回复 -->
          <div class="d-flex justify-content-start align-items-end mb-4">
            <div class="ai-avatar me-3">
              <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" class="bi bi-gpu-card" viewBox="0 0 16 16">
                <path d="M4 8a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Zm7.5-1.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3Z"/>
                <path d="M0 1.5A.5.5 0 0 1 .5 1h1a.5.5 0 0 1 .5.5V4h13.5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-.5.5H2v2.5a.5.5 0 0 1-1 0V2H.5a.5.5 0 0 1-.5-.5Zm5.5 4a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5ZM9 8a2.5 2.5 0 1 0 5 0 2.5 2.5 0 0 0-5 0Z"/>
                <path d="M3 12.5h3.5v1a.5.5 0 0 1-.5.5H3.5a.5.5 0 0 1-.5-.5v-1Zm4 1v-1h4v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5Z"/>
              </svg>
            </div>
            <div class="ai-bubble shadow-sm px-4 py-3">
              <div v-html="chatAnswer"></div>
            </div>
          </div>
          <!-- 底部操作栏 -->
          <div class="chat-toolbar d-flex align-items-center gap-2 mb-3 mt-auto">
            <button class="btn toolbar-btn">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-globe-asia-australia" viewBox="0 0 16 16">
              <path d="m10.495 6.92 1.278-.619a.483.483 0 0 0 .126-.782c-.252-.244-.682-.139-.932.107-.23.226-.513.373-.816.53l-.102.054c-.338.178-.264.626.1.736a.476.476 0 0 0 .346-.027ZM7.741 9.808V9.78a.413.413 0 1 1 .783.183l-.22.443a.602.602 0 0 1-.12.167l-.193.185a.36.36 0 1 1-.5-.516l.112-.108a.453.453 0 0 0 .138-.326ZM5.672 12.5l.482.233A.386.386 0 1 0 6.32 12h-.416a.702.702 0 0 1-.419-.139l-.277-.206a.302.302 0 1 0-.298.52l.761.325Z"/>
              <path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0ZM1.612 10.867l.756-1.288a1 1 0 0 1 1.545-.225l1.074 1.005a.986.986 0 0 0 1.36-.011l.038-.037a.882.882 0 0 0 .26-.755c-.075-.548.37-1.033.92-1.099.728-.086 1.587-.324 1.728-.957.086-.386-.114-.83-.361-1.2-.207-.312 0-.8.374-.8.123 0 .24-.055.318-.15l.393-.474c.196-.237.491-.368.797-.403.554-.064 1.407-.277 1.583-.973.098-.391-.192-.634-.484-.88-.254-.212-.51-.426-.515-.741a6.998 6.998 0 0 1 3.425 7.692 1.015 1.015 0 0 0-.087-.063l-.316-.204a1 1 0 0 0-.977-.06l-.169.082a1 1 0 0 1-.741.051l-1.021-.329A1 1 0 0 0 11.205 9h-.165a1 1 0 0 0-.945.674l-.172.499a1 1 0 0 1-.404.514l-.802.518a1 1 0 0 0-.458.84v.455a1 1 0 0 0 1 1h.257a1 1 0 0 1 .542.16l.762.49a.998.998 0 0 0 .283.126 7.001 7.001 0 0 1-9.49-3.409Z"/>
            </svg>
              联网搜索</button>
            <button class="btn toolbar-btn">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-collection-fill" viewBox="0 0 16 16">
                <path d="M0 13a1.5 1.5 0 0 0 1.5 1.5h13A1.5 1.5 0 0 0 16 13V6a1.5 1.5 0 0 0-1.5-1.5h-13A1.5 1.5 0 0 0 0 6v7zM2 3a.5.5 0 0 0 .5.5h11a.5.5 0 0 0 0-1h-11A.5.5 0 0 0 2 3zm2-2a.5.5 0 0 0 .5.5h7a.5.5 0 0 0 0-1h-7A.5.5 0 0 0 4 1z"/>
              </svg>
              文本导入</button>
            <button class="btn btn-accent ms-auto">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-tornado" viewBox="0 0 16 16">
              <path d="M1.125 2.45A.892.892 0 0 1 1 2c0-.26.116-.474.258-.634a1.9 1.9 0 0 1 .513-.389c.387-.21.913-.385 1.52-.525C4.514.17 6.18 0 8 0c1.821 0 3.486.17 4.709.452.607.14 1.133.314 1.52.525.193.106.374.233.513.389.141.16.258.374.258.634 0 1.011-.35 1.612-.634 2.102-.04.07-.08.137-.116.203a2.55 2.55 0 0 0-.313.809 2.938 2.938 0 0 0-.011.891.5.5 0 0 1 .428.849c-.06.06-.133.126-.215.195.204 1.116.088 1.99-.3 2.711-.453.84-1.231 1.383-2.02 1.856-.204.123-.412.243-.62.364-1.444.832-2.928 1.689-3.735 3.706a.5.5 0 0 1-.748.226l-.001-.001-.002-.001-.004-.003-.01-.008a2.142 2.142 0 0 1-.147-.115 4.095 4.095 0 0 1-1.179-1.656 3.786 3.786 0 0 1-.247-1.296A.498.498 0 0 1 5 12.5v-.018a.62.62 0 0 1 .008-.079.728.728 0 0 1 .188-.386c.09-.489.272-1.014.573-1.574a.5.5 0 0 1 .073-.918 3.29 3.29 0 0 1 .617-.144l.15-.193c.285-.356.404-.639.437-.861a.948.948 0 0 0-.122-.619c-.249-.455-.815-.903-1.613-1.43-.193-.127-.398-.258-.609-.394l-.119-.076a12.307 12.307 0 0 1-1.241-.334.5.5 0 0 1-.285-.707l-.23-.18C2.117 4.01 1.463 3.32 1.125 2.45zm1.973 1.051c.113.104.233.207.358.308.472.381.99.722 1.515 1.06 1.54.317 3.632.5 5.43.14a.5.5 0 0 1 .197.981c-1.216.244-2.537.26-3.759.157.399.326.744.682.963 1.081.203.373.302.79.233 1.247-.05.33-.182.657-.39.985.075.017.148.035.22.053l.006.002c.481.12.863.213 1.47.01a.5.5 0 1 1 .317.95c-.888.295-1.505.141-2.023.012l-.006-.002a3.894 3.894 0 0 0-.644-.123c-.37.55-.598 1.05-.726 1.497.142.045.296.11.465.194a.5.5 0 1 1-.448.894 3.11 3.11 0 0 0-.148-.07c.012.345.084.643.18.895.14.369.342.666.528.886.992-1.903 2.583-2.814 3.885-3.56.203-.116.399-.228.584-.34.775-.464 1.34-.89 1.653-1.472.212-.393.33-.9.26-1.617A6.74 6.74 0 0 1 10 8.5a.5.5 0 0 1 0-1 5.76 5.76 0 0 0 3.017-.872.515.515 0 0 1-.007-.03c-.135-.673-.14-1.207-.056-1.665.084-.46.253-.81.421-1.113l.131-.23c.065-.112.126-.22.182-.327-.29.107-.62.202-.98.285C11.487 3.83 9.822 4 8 4c-1.821 0-3.486-.17-4.709-.452-.065-.015-.13-.03-.193-.047zM13.964 2a1.12 1.12 0 0 0-.214-.145c-.272-.148-.697-.297-1.266-.428C11.354 1.166 9.769 1 8 1c-1.769 0-3.354.166-4.484.427-.569.13-.994.28-1.266.428A1.12 1.12 0 0 0 2.036 2c.04.038.109.087.214.145.272.148.697.297 1.266.428C4.646 2.834 6.231 3 8 3c1.769 0 3.354-.166 4.484-.427.569-.13.994-.28 1.266-.428A1.12 1.12 0 0 0 13.964 2z"/>
            </svg>
              开启新对话</button>
          </div>
          <!-- 输入区 -->
          <div class="chat-inputbar mb-3">
            <input class="form-control flex-grow-1 border-0 bg-transparent" placeholder="请输入您的问题..." />
            <button class="btn btn-primary send-btn ms-2">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-twitch" viewBox="0 0 16 16">
              <path d="M3.857 0 1 2.857v10.286h3.429V16l2.857-2.857H9.57L14.714 8V0H3.857zm9.714 7.429-2.285 2.285H9l-2 2v-2H4.429V1.143h9.142v6.286z"/>
              <path d="M11.857 3.143h-1.143V6.57h1.143V3.143zm-3.143 0H7.571V6.57h1.143V3.143z"/>
            </svg>
            </button>
          </div>
        </div>
      </section>





      <!-- 右侧栏 -->
      <aside class="geochat-right d-flex flex-column">
        <div class="pe-4 pt-4 d-flex justify-content-end align-items-center gap-2">
          <a href="#" class="text-muted">OLD</a>
          <span class="main-avatar ms-2">M</span>
          <span class="ms-2 fw-semibold">Michael</span>
        </div>

        <div class="px-4 mt-2 flex-grow-1 d-flex flex-column gap-3">
          <!-- 文本图谱卡片 -->
          <div class="right-card d-flex flex-column align-items-start">
            <div class="card-header section-title px-0 pt-0 pb-2 w-100" style="margin-left: 10px;">文本图谱</div>
            <div class="neo4j-container w-100 d-flex justify-content-center align-items-center">
              <div class="neo4j-wrapper">
                <Neo4j/>
              </div>
            </div>
          </div>
          <!-- 子图展示卡片 -->
          <div class="right-card d-flex flex-column align-items-start">
            <div class="card-header section-title px-0 pt-0 pb-2 w-100" style="margin-left: 10px;">子图展示</div>
            <div class="neo4j-container w-100 d-flex justify-content-center align-items-center">
              <div class="neo4j-wrapper">
                <Neo4j/>
              </div>
            </div>
          </div>
        </div>
      </aside>

    </div>
  </div>
</template>

<script>
import Neo4j from '@/components/Neo4j'
export default {
  name: 'GeoChatApp',
  components: {
    Neo4j
  },
  data() {
    return {
      chatAnswer: `<b>孔隙度：</b><br>
 是岩石中孔隙体积占总体积的百分比，是控制油气储量及储能的重要物理参数。<br>
 根据孔隙的大小、连通状况以及对流体的有效性，孔隙度通常分为以下几类：<br><br>
 <b>1. 绝对孔隙度</b><br>
 绝对孔隙度是指岩样中所有孔隙空间体积之和与岩样总体积的比值。这一指标反映了岩石中所有孔隙的总体积，通常用于评价储层的基本特性。<br>
 <b>2. 有效孔隙度</b><br>
 有效孔隙度是指那些互相连通的。在一定差异下允许流体流动的孔隙总体积与岩石总体积的比值。有效孔隙度通常小于绝对孔隙度，反映了流体在岩石中实际可流动的空间……`
    }
  },
}
</script>

<style scoped>
.geochat-app {background: #f6f7fa; height: 100vh; min-width: 1280px; font-family: 'SF Pro', 'Segoe UI', 'PingFang SC', Arial, sans-serif;}
.geochat-mainrow {height: 100vh;}
.geochat-left {
  width: 250px; background: #f1f3f8; border-right:1px solid #ededf8; min-width:210px;
  display:flex; flex-direction:column;
}
.sider-card {
  background: #222936;
  color: #fff;
  /*border-radius: 17px;*/
  padding: 1.1rem 1.1rem 0.9rem 1.2rem;
  margin-bottom: 9px;
  /*box-shadow: 0 2.5px 12px #23293618;*/
  box-shadow: 0 6px 24px #a3a3b51c, 0 1.5px 8px #23293625;
  border-radius: 20px;
  transition: box-shadow 0.22s, transform 0.15s;
}
.sider-card:hover {
  box-shadow: 0 12px 32px #63636d36, 0 3px 16px #23293630;
  transform: translateY(-2px) scale(1.015);
}
.sider-title {font-size: 1.03rem; font-weight: 600;}
.sider-content {font-size: .98rem; color:#c8d6e8; margin-top:2px; line-height:1.75;}
.geochat-center {flex:1; background: #fff; min-width:520px; display: flex; flex-direction:column;}
.main-logo {font-size: 2.1rem; color: #4361ee;}
.main-title {font-size: 1.65rem; font-weight: bold; color: #1c203a; letter-spacing:0.01em;}

/* 聊天气泡 */
.user-bubble, .ai-bubble {
  border-radius: 18px;
  text-align: left;
  min-width: 120px;
  max-width: 540px;
  font-size: 1.05rem;
  word-break: break-word;
  line-height: 1.8;
  padding: 0.95rem 1.25rem;
  box-shadow: 0 2px 12px #dfe4f31a;
}
.user-bubble {
  background: linear-gradient(96deg,#e5ecfa 60%,#f8fafc 100%);
  color: #22336c;
  border-top-right-radius: 6px;
  border-bottom-right-radius: 16px;
}
.ai-bubble {
  background: #f4f8fb;
  color: #07080a;
  border-top-left-radius: 6px;
  border-bottom-left-radius: 16px;
}
.user-avatar, .ai-avatar {
  background: #fff;
  /*border-radius: 50%;*/
  width: 38px;
  height: 38px;
  display: flex; align-items: center; justify-content: center;
  /*box-shadow: 0 2px 10px #e2eafb4a;*/
  font-size: 1.42rem;
  color: #6199ef;
  box-shadow: 0 6px 24px #88aaff22, 0 1.5px 8px #23293617;
  border-radius: 20px;
  transition: box-shadow 0.22s, transform 0.30s;

  /*background: #fff;*/
}
.user-bubble:hover,
.ai-bubble:hover {
  box-shadow: 0 14px 32px #4361ee22, 0 4px 18px #23293619;
  transform: translateY(-2px) scale(1.025);

}
.ai-avatar {background:#eaf1fc; color: #0f0f10;}
.user-avatar {background:#ecf5fd; color: #509eff;}
/* 工具栏按钮 */
.chat-toolbar .btn, .toolbar-btn {
  background: #100f0f;
  border-color: #4b4948;
  color: #fff;
  border-radius: 7px;
  font-size: 0.99rem!important;
  font-weight: 500;
  padding: 0.45rem 1.1rem;
  box-shadow: 0 1px 8px #e2e3f41a;
  transition: background 0.16s, color 0.16s, box-shadow 0.16s;
}
.chat-toolbar .btn:hover, .toolbar-btn:hover {
  background: #5a7090;
  border-color: #4361ee;
  color: #fff;
}
.btn-accent {
  background: linear-gradient(94deg, #ffe4a6 86%, #fffbe5 100%);
  color: #9d6f15;
  border: none;
  font-weight: 600;
  box-shadow: 0 1.5px 10px #ffd06316;
}
.btn-accent:hover {
  background: #ffd063;
  color: #784007;
}

/* 输入区 */
.chat-inputbar {
  background: #f8fafc;
  border-radius: 12px;
  box-shadow: 0 2px 10px #e3eaf73c;
  display: flex;
  align-items: center;
  padding: 0.4rem 1rem;
  border: 1.1px solid #e3e9f8;
}
.chat-inputbar input {
  background: transparent;
  border: none;
  outline: none;
  font-size: 1.07rem;
  padding-left: 0;
  box-shadow: none;
}

.chat-inputbar input:focus {box-shadow: none;}
.send-btn {
  background: #4255af;
  color: #fff;
  border: none;
  border-radius: 9px;
  font-size: 1.23rem;
  width: 40px; height: 36px;
  display: flex; align-items: center; justify-content: center;
  transition: background .18s;
  box-shadow: 0 1.6px 8px #d8dfff2a;
}
.send-btn:hover {background: #3d8787;}
/* 聊天主区滚动 */
.chat-area {
  min-height: 93%;
  max-height: 64vh;
  overflow-y: auto;
}

/* 右栏顶部与卡片 */
.geochat-right {
  min-width: 380px;
  max-width: 440px;
  background: #f8f7fb;
  border-left: 1.3px solid #eeeff6;
  display: flex;
  flex-direction: column;
  height: 100vh;
}
.right-card {
  background: #fff;
  border-radius: 17px;
  box-shadow: 0 3px 14px #bfd6fd25;
  padding: 0 0 18px 0;
  width: 100%;
  border: 1.1px solid #edf1f9;
  min-height: 400px;
  max-height: 410px;
  display: flex;
  flex-direction: column;
  /* 保证卡片内容撑满 */
}
.section-title, .card-header {
  font-size: 1.25rem;
  font-weight: 600;
  color: #232836;
  background: transparent;
  border-bottom: 1px solid #eaeaea;
  text-align: left;
  width: 100%;
  padding-left: 16px;
  padding-top: 17px;
  padding-bottom: 9px;
  margin-bottom: 0;
  border-radius: 0;
}
.neo4j-container {
  flex: 1 1 0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 0;
  min-width: 0;
  /* 容器撑满卡片主体 */
}
.neo4j-wrapper {
  width: 95%;
  height: 95%;
  display: flex;
  justify-content: center;
  align-items: center;
  /* 若Neo4j为svg/canvas，建议这里overflow:hidden */
}

.link-upgrade {
  background: #fff2d1;
  color: #b17b10;
  border-radius: 8px;
  font-weight: 700;
  padding: 4px 14px;
  text-decoration: none;
  box-shadow: 0 1px 8px #faefb730;
  font-size: 1rem;
}

.main-avatar {
  background: #4255af;
  color: #fff;
  width: 32px; height: 32px;
  border-radius: 50%;
  display: inline-flex; align-items: center; justify-content: center;
  font-family: 'Montserrat', Arial, sans-serif;
  font-size: 1.03rem;
  font-weight: 700;
  letter-spacing: 2px;
  margin-right: 2px;
  box-shadow: 0 1.5px 7px #18225c19;
}

.right-card img {border-radius: 14px;}
/* 响应式适配 */
@media (max-width: 1400px) {
  .geochat-left {min-width:160px;}
  .geochat-right {min-width:220px;}
}
</style>
