<template>
  <div>
    <div id="txtgra" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'TxtGra',
  data() {



    return {
      graphData: {
        nodes: [
          { id: 0, label: '原始文本' },  // 父节点
          { id: 1, label: '构型特征.txt' },
          { id: 2, label: '沉积相.txt' },
          { id: 3, label: '湖泊相.txt' },
          { id: 4, label: '沙漠相.txt' },
          { id: 5, label: '时空格架.txt' },
          { id: 6, label: '地质模式.txt' },
          { id: 7, label: '沉积相与体系.txt' },
          { id: 8, label: '物性特征.txt' },
          { id: 9, label: '岩相特征.txt' },
          { id: 10,label: '地质构造.txt' },
          { id: 11,label: '三角洲相.txt' },
        ],
        edges: [
          { source: 0, target: 1, label: { show: true, formatter: '属于', color: '#000', fontSize: 10 } },
          { source: 0, target: 2, label: { show: true, formatter: '属于', color: '#000', fontSize: 10 } },
          { source: 0, target: 3, label: { show: true, formatter: '属于', color: '#000', fontSize: 10 } },
          { source: 0, target: 4, label: { show: true, formatter: '属于', color: '#000', fontSize: 10 } },
          { source: 0, target: 5, label: { show: true, formatter: '属于', color: '#000', fontSize: 10 } },
          { source: 0, target: 6, label: { show: true, formatter: '属于', color: '#000', fontSize: 10 } },
          { source: 0, target: 7, label: { show: true, formatter: '属于', color: '#000', fontSize: 10 } },
          { source: 0, target: 8, label: { show: true, formatter: '属于', color: '#000', fontSize: 10 } },
          { source: 0, target: 9, label: { show: true, formatter: '属于', color: '#000', fontSize: 10 } },
          { source: 0, target: 10, label: { show: true, formatter: '属于', color: '#000', fontSize: 10 } },
          { source: 0, target: 11, label: { show: true, formatter: '属于', color: '#000', fontSize: 10 } },
        ]
      }
    };
  },
  mounted() {
    this.initializeECharts();
  },
  methods: {
    initializeECharts() {
      const container = document.getElementById('txtgra');
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
              formatter: '{b}',
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
                symbolSize: node.id === 0 ? 55 : 75,
                itemStyle: {
                  color: node.id === 0 ? 'rgb(224,109,7)' : '#7bc11b',
                }
              };
            }),
            force: {
              edgeLength: 100,
              repulsion: 80,
              gravity: 0.1,
            },
            edges: this.graphData.edges.map(edge => ({
              ...edge,
              lineStyle: {
                color: '#888',
                width: 2,
                type: 'solid'
              },
              label: {
                show: true,
                formatter: edge.label.formatter,
                color:'#0e0101',
                fontSize:10,
                position: 'middle', // 标签位置设置为中间
              }
            }))
          },
        ],
      };

      this.myChart.setOption(option);
      this.myChart.hideLoading();
    }
  }
};
</script>

<style scoped>
</style>
