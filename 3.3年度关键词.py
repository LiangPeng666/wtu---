import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('2.3关键词清洗_去除新关键词.csv')

# 填充缺失值，使用中位数填充
median_year = df['Year-年'].median()
df['Year-年'].fillna(median_year, inplace=True)

# 统计关键词出现的频率
keyword_counts = df['Keyword-关键词'].str.split(';;').explode().value_counts().reset_index(name='频率')

# 提取频率最高的前九个关键词
top_9_keywords = keyword_counts.nlargest(9, '频率')['Keyword-关键词'].tolist()

# 创建有向图
G = nx.DiGraph()

# 添加节点
for _, row in df.iterrows():
    year = int(row['Year-年'])
    keywords = row['Keyword-关键词'].split(';;')
    for keyword in keywords:
        if keyword in top_9_keywords:
            G.add_node(keyword)
            G.add_node(year)

# 添加边
for _, row in df.iterrows():
    year = int(row['Year-年'])
    keywords = row['Keyword-关键词'].split(';;')
    for keyword in keywords:
        if keyword in top_9_keywords:
            G.add_edge(keyword, year)

# 统计关键词每年出现的次数
yearly_keyword_counts = {}
for _, row in df.iterrows():
    year = int(row['Year-年'])
    keywords = row['Keyword-关键词'].split(';;')
    for keyword in keywords:
        if keyword in top_9_keywords:
            if year not in yearly_keyword_counts:
                yearly_keyword_counts[year] = {}
            if keyword not in yearly_keyword_counts[year]:
                yearly_keyword_counts[year][keyword] = 0
            yearly_keyword_counts[year][keyword] += 1

# 设置中文字体为宋体
plt.rcParams['font.sans-serif'] = ['SimSun']
# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 绘制线图
for keyword in top_9_keywords:
    years = []
    counts = []
    for year in sorted(yearly_keyword_counts.keys()):
        if keyword in yearly_keyword_counts[year]:
            years.append(year)
            counts.append(yearly_keyword_counts[year][keyword])
        else:
            years.append(year)
            counts.append(0)
    plt.plot(years, counts, label=keyword)

plt.xlabel('年')
plt.ylabel('关键词数量')
plt.title('每年频率最高的九个关键词')
plt.legend()
plt.show()