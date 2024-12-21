import pandas as pd
import networkx as nx
from pyvis.network import Network

# 读取CSV文件
data_csv = pd.read_csv('传统茶饮数据集_预处理后.csv')

# 创建空的有向图
G = nx.DiGraph()

# 添加节点（作者）
for author in data_csv['Author-作者'].unique():
    G.add_node(author)

# 添加边（基于单位）
for index, row in data_csv.iterrows():
    author1 = row['Author-作者']
    unit1 = row['Organ-单位']
    for other_index, other_row in data_csv.iterrows():
        author2 = other_row['Author-作者']
        unit2 = other_row['Organ-单位']
        if author1!= author2 and unit1 == unit2:
            G.add_edge(author1, author2)

# 使用Pyvis创建交互式网络可视化
nt = Network(notebook=True)

# 将NetworkX图转换为Pyvis图
for node in G.nodes:
    nt.add_node(node)
for edge in G.edges:
    nt.add_edge(edge[0], edge[1])

# 保存为HTML文件
nt.save_graph('作者关系网络.html')