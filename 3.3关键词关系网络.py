import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('2.3关键词清洗_去除新关键词.csv')

# 统计关键词出现的频率
keyword_counts = df['Keyword-关键词'].str.split(';;').explode().value_counts().reset_index(name='频率')

# 提取频率最高的前九个关键词
top_9_keywords = keyword_counts.nlargest(9, '频率')['Keyword-关键词'].tolist()

# 创建有向图
G = nx.DiGraph()

# 添加节点
for _, row in df.iterrows():
    year = row['Year-年']
    keywords = row['Keyword-关键词'].split(';;')
    for keyword in keywords:
        if keyword in top_9_keywords:
            G.add_node(keyword)
            G.add_node(year)

# 添加边
for _, row in df.iterrows():
    year = row['Year-年']
    keywords = row['Keyword-关键词'].split(';;')
    for keyword in keywords:
        if keyword in top_9_keywords:
            G.add_edge(keyword, year)

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 使用spring_layout布局
pos = nx.spring_layout(G, k=3)  # k控制节点之间的距离，值越大距离越大

# 设置字体为宋体
plt.rcParams['font.sans-serif'] = ['SimSun']
# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 绘制图形
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=10)

# 生成表示关系的表格数据
table_data = []
for edge in G.edges():
    source = edge[0]
    target = edge[1]
    table_data.append([source, target])

# 创建DataFrame并打印表格
table_df = pd.DataFrame(table_data, columns=['源节点', '目标节点'])
print(table_df)

plt.show()