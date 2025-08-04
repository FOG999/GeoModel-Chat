<template>
  <div>
    <div id="txt-graph" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import axios from 'axios';

export default {



  name: 'TxtGraph',
  data() {
    return {
      myChart: null, // ECharts 实例
      graphData: null, // 图谱数据
    };
  },
  async mounted() {
    await this.loadGraphData();
  },
  methods: {
    async loadGraphData() {
      try {
        const response = await axios.get('http://localhost:5000/api/getTxtGraph');
        this.graphData = response.data;
        if (this.graphData.nodes && this.graphData.nodes.length > 0) {
          this.initializeECharts();
        } else {
          console.warn('The graph data contains no nodes.');
        }
      } catch (error) {
        console.error('Error retrieving graph data:', error);
      }
    },
    initializeECharts() {
      const container = document.getElementById('txt-graph');
      if (!container || container.offsetWidth === 0) {
        setTimeout(() => this.initializeECharts(), 100);
        return;
      }
      this.myChart = echarts.init(container);
      this.myChart.showLoading();

      const option = {
        series: [
          {
            type: 'graph',
            layout: 'force',
            animation: false,
            label: {
              position: 'inside',
              show: true,
              formatter: '{b}', // 使用节点的 'label' 显示
              fontSize: 13,
              color: '#000',
              fontWeight: 'bold',
            },
            draggable: true,
            data: this.graphData.nodes.map((node) => {
              return {
                id: node.id,
                name: node.label,
                value: node.label,
                symbolSize: 60,
                itemStyle: {
                  color: '#db9834', // 设置节点颜色 (可以根据需要修改颜色)
                }
              };
            }),
            force: {
              edgeLength: 100,
              repulsion: 80,
              gravity: 0.1,
            },
            edges: this.graphData.edges // 确保边数据格式正确
          },
        ],
      };

      this.myChart.setOption(option);
      this.myChart.hideLoading();
    },
  },
};
</script>

<style scoped>
#txt-graph {
  width: 100%;
  height: 100%;
  max-width: 440px; /* 确保宽度不超过容器 */
  box-sizing: border-box; /* 避免边框影响布局 */
}
</style>
