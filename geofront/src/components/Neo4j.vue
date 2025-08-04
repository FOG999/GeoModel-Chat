<template>
  <div class="knowledge-graph">
    <div ref="chart" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import { onMounted, ref } from 'vue';




export default {
  name: "Neo4j",
  setup() {

    const chart = ref(null);

    // 生成随机名称
    const generateName = (type, index) => {
      const regions = ['东海', '塔里木', '松辽', '渤海', '南海', '鄂尔多斯 ', '四川', '准噶尔'];
      const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
      const formations = ['新生界', '古生界', '中生界', '元古界', '太古界'];
      const facies = ['砂岩', '泥岩', '碳酸盐岩', '页岩', '砾岩', '粉砂岩', '煤'];

      if (type === 'well') {
        const region = regions[index % regions.length];
        const letter = letters[index % letters.length];
        return `${region}${letter}-${index+1}井`;
      } else if (type === 'formation') {
        return formations[index % formations.length];
      } else {
        return facies[index % facies.length];
      }
    };

    // 虚拟数据生成函数
    const generateVirtualData = () => {
      const nodes = [];
      const edges = [];
      let idCounter = 1;

      // 1. 生成20个井节点
      for (let i = 0; i < 20; i++) {
        nodes.push({
          id: `well${i+1}`,
          name: generateName('well', i),
          category: 0,
          symbolSize: 40 + Math.random() * 10
        });
      }

      // 2. 生成40个地层节点
      for (let i = 0; i < 40; i++) {
        nodes.push({
          id: `formation${i+1}`,
          name: generateName('formation', i),
          category: 1,
          symbolSize: 25 + Math.random() * 10
        });
      }

      // 3. 生成40个岩相节点
      for (let i = 0; i < 40; i++) {
        nodes.push({
          id: `facies${i+1}`,
          name: generateName('facies', i),
          category: 2,
          symbolSize: 15 + Math.random() * 10
        });
      }

      // 4. 创建关联关系
      // 井与地层关联 (每个井关联2-4个地层)
      for (let i = 1; i <= 20; i++) {
        const formationCount = 2 + Math.floor(Math.random() * 3);
        for (let j = 0; j < formationCount; j++) {
          edges.push({
            source: `well${i}`,
            target: `formation${1 + Math.floor(Math.random() * 40)}`
          });
        }
      }

      // 地层与岩相关联 (每个地层关联1-3个岩相)
      for (let i = 1; i <= 40; i++) {
        const faciesCount = 1 + Math.floor(Math.random() * 3);
        for (let j = 0; j < faciesCount; j++) {
          edges.push({
            source: `formation${i}`,
            target: `facies${1 + Math.floor(Math.random() * 40)}`
          });
        }
      }

      return { nodes, edges };
    };

    onMounted(() => {
      const myChart = echarts.init(chart.value);
      myChart.showLoading();

      // 使用虚拟数据
      const graphData = generateVirtualData();

      myChart.hideLoading();
      myChart.setOption({
        title: {
          // text: '石油地质知识图谱 (100节点)',
          // subtext: '包含20口井、40个地层单元和40种岩相',
          left: 'center',
          textStyle: {
            fontSize: 18,
            fontWeight: 'bold'
          }
        },
        tooltip: {},
        legend: {
          data: ['井', '地层', '岩相'],
          orient: 'horizontal',
          top: 5,
          left: 'center',
          itemWidth: 20,
          itemHeight: 14,
          textStyle: {
            fontSize: 12
          }
        },
        animationDuration: 2000,
        animationEasingUpdate: 'quinticInOut',
        series: [{
          type: 'graph',
          layout: 'force',
          force: {
            repulsion: 150,
            edgeLength: 80,
            gravity: 0.1
          },
          data: graphData.nodes.map(node => ({
            ...node,
            itemStyle: {
              color: getColorByCategory(node.category)
            },
            label: {
              show: node.category === 0, // 默认只显示井名
              position: 'right',
              fontSize: 10
            }
          })),
          edges: graphData.edges,
          categories: [
            { name: '井' },
            { name: '地层' },
            { name: '岩相' }
          ],
          emphasis: {
            focus: 'adjacency',
            label: {
              show: true
            }
          },
          roam: true,
          lineStyle: {
            width: 0.8,
            curveness: 0.2,
            opacity: 0.6
          },
          focusNodeAdjacency: true
        }],
        toolbox: {
          feature: {
            saveAsImage: {
              title: '保存图片',
            },
            restore: {
              title: '重置视图'
            }
          },
          right: 20,
          top:25
        }
      });

      // 点击图例切换显示
      myChart.on('legendselectchanged', function(params) {
        const option = myChart.getOption();
        const selected = params.selected;
        const series = option.series[0];

        series.data.forEach(node => {
          node.label.show = selected[node.category];
        });

        myChart.setOption(option);
      });

      window.addEventListener('resize', function() {
        myChart.resize();
      });
    });

    // 根据节点类别返回颜色
    const getColorByCategory = (category) => {
      const colors = ['#5470C6', '#91CC75', '#e8b25d'];
      return colors[category] || '#73C0DE';
    };

    return { chart };
  }
}
</script>

<style scoped>
.knowledge-graph {
  width: 100%;
  height: 100%;
  background-color: #f5f7fa;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  padding: 0px;

}
</style>














<!--<template>-->
<!--  <div class="knowledge-graph">-->
<!--    <div ref="chart" style="width: 100%; height: 520px;"></div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import * as echarts from 'echarts';-->
<!--import { onMounted, ref } from 'vue';-->

<!--export default {-->
<!--  name: "Neo4j",-->
<!--  setup() {-->
<!--    const chart = ref(null);-->

<!--    // 虚拟数据生成函数-->
<!--    const generateVirtualData = () => {-->
<!--      // 节点数据-->
<!--      const nodes = [-->
<!--        // 井数据-->
<!--        { id: 'well1', name: '东海A-1井', category: 0, symbolSize: 50 },-->
<!--        { id: 'well2', name: '塔里木B-3井', category: 0, symbolSize: 45 },-->
<!--        { id: 'well3', name: '松辽C-5井', category: 0, symbolSize: 40 },-->

<!--        // 地层数据-->
<!--        { id: 'formation1', name: '新生界', category: 1, symbolSize: 35 },-->
<!--        { id: 'formation2', name: '古生界', category: 1, symbolSize: 30 },-->
<!--        { id: 'formation3', name: '白垩系', category: 1, symbolSize: 30 },-->

<!--        // 岩相数据-->
<!--        { id: 'facies1', name: '砂岩', category: 2, symbolSize: 25 },-->
<!--        { id: 'facies2', name: '泥岩', category: 2, symbolSize: 25 },-->
<!--        { id: 'facies3', name: '碳酸盐岩', category: 2, symbolSize: 25 },-->
<!--        { id: 'facies4', name: '页岩', category: 2, symbolSize: 25 }-->
<!--      ];-->

<!--      // 关系数据-->
<!--      const edges = [-->
<!--        // 井与地层关系-->
<!--        { source: 'well1', target: 'formation1' },-->
<!--        { source: 'well2', target: 'formation2' },-->
<!--        { source: 'well3', target: 'formation3' },-->

<!--        // 地层与岩相关系-->
<!--        { source: 'formation1', target: 'facies1' },-->
<!--        { source: 'formation1', target: 'facies2' },-->
<!--        { source: 'formation2', target: 'facies3' },-->
<!--        { source: 'formation3', target: 'facies1' },-->
<!--        { source: 'formation3', target: 'facies4' }-->
<!--      ];-->

<!--      return { nodes, edges };-->
<!--    };-->

<!--    onMounted(() => {-->
<!--      const myChart = echarts.init(chart.value);-->
<!--      myChart.showLoading();-->

<!--      // 使用虚拟数据替代AJAX请求-->
<!--      const graphData = generateVirtualData();-->

<!--      myChart.hideLoading();-->
<!--      myChart.setOption({-->
<!--        title: {-->
<!--          text: ' ',-->
<!--          subtext: '',-->
<!--          left: 'center'-->
<!--        },-->
<!--        tooltip: {},-->
<!--        legend: {-->
<!--          data: ['井', '地层', '岩相'],-->
<!--          orient: 'horizontal', // 改为水平布局-->
<!--          top: 40, // 距离顶部40px-->
<!--          left: 'center', // 水平居中-->
<!--        },-->
<!--        animationDuration: 1500,-->
<!--        animationEasingUpdate: 'quinticInOut',-->
<!--        series: [{-->
<!--          type: 'graph',-->
<!--          layout: 'force',-->
<!--          force: {-->
<!--            repulsion: 200,-->
<!--            edgeLength: 120-->
<!--          },-->
<!--          data: graphData.nodes.map(node => ({-->
<!--            ...node,-->
<!--            itemStyle: {-->
<!--              color: getColorByCategory(node.category)-->
<!--            },-->
<!--            label: {-->
<!--              show: true,-->
<!--              position: 'right'-->
<!--            }-->
<!--          })),-->
<!--          edges: graphData.edges,-->
<!--          categories: [-->
<!--            { name: '井' },-->
<!--            { name: '地层' },-->
<!--            { name: '岩相' }-->
<!--          ],-->
<!--          emphasis: {-->
<!--            focus: 'adjacency',-->
<!--            label: {-->
<!--              show: true-->
<!--            }-->
<!--          },-->
<!--          roam: true,-->
<!--          lineStyle: {-->
<!--            width: 1,-->
<!--            curveness: 0.2,-->
<!--            opacity: 0.8-->
<!--          }-->
<!--        }]-->
<!--      });-->

<!--      // 响应式调整-->
<!--      window.addEventListener('resize', function() {-->
<!--        myChart.resize();-->
<!--      });-->
<!--    });-->

<!--    // 根据节点类别返回颜色-->
<!--    const getColorByCategory = (category) => {-->
<!--      const colors = ['#5470C6', '#91CC75', '#EE6666'];-->
<!--      return colors[category] || '#73C0DE';-->
<!--    };-->

<!--    return { chart };-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--.knowledge-graph {-->
<!--  width: 100%;-->
<!--  height: 100%;-->
<!--  background-color: #f5f7fa;-->
<!--  border-radius: 8px;-->
<!--  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);-->
<!--  padding:0px;-->
<!--}-->
<!--</style>-->
