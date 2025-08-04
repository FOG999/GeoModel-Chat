<template>
  <div>
    <div id="nodes-graph" style="width: 100%; height: 500px;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import axios from 'axios';

export default {
  name: 'NodesGraph',
  data() {
    return {
      myChart: null,
      graphData: null, // 图谱数据
    };


  },
  async mounted() {
    await this.loadGraphData();
  },
  methods: {
    async loadGraphData() {
      try {
        const response = await axios.get('http://localhost:5000/api/getNodesGraph');
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
      const container = document.getElementById('nodes-graph');
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
              position: 'inside', // 标签在节点右侧显示
              show: true, // 显示标签
              formatter: '{b}', // 使用节点的 'name' 作为标签
              fontSize: 12,
              color: '#000',
              fontWeight: 'bold',
            },
            draggable: true,
            data: this.graphData.nodes.map((node) => {
              return {
                id: node.id.toString(), // 转换为字符串以确保兼容
                name: node.label, // 使用 label 作为节点显示名
                symbolSize: 50, // 设置节点大小
              };
            }),
            force: {
              edgeLength: 100, // 边长度影响节点间距
              repulsion: 60, // 斥力影响节点分散程度
              gravity: 0.1, // 重力影响整体布局
            },
            edges: this.graphData.edges.map((edge) => {
              return {
                source: edge.source.toString(), // 转换为字符串
                target: edge.target.toString(), // 转换为字符串
                label: {
                  show: false, // 显示边标签
                  formatter: edge.label, // 边的标签
                },
                lineStyle: {
                  width: 2,
                  curveness: 0.3, // 边的曲率
                },
              };
            }),
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
#nodes-graph {
  width: 100%;
  height: 300px;
  max-width: 100%; /* 确保宽度自适应 */
  box-sizing: border-box;
}
</style>
