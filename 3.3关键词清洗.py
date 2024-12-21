import pandas as pd

# 读取数据
df = pd.read_csv('传统茶饮数据集_预处理后.csv')

# 定义要保留的关键词列表
keywords = ['新式茶饮', '营销策略', '茶饮品牌', '新茶饮', '中药代茶饮', '喜茶', '包装设计', '茶文化', '代茶饮', '蜜雪冰城', '品牌形象设计', '茶饮', '品牌传播', '品牌', 'SWOT分析', '品牌定位', '市场定位', '奈雪的茶']

# 提取关键词列并转换为字符串类型
df['Keyword-关键词'] = df['Keyword-关键词'].astype(str)

# 过滤出包含指定关键词的行
df = df[df['Keyword-关键词'].apply(lambda x: any(keyword in x for keyword in keywords))]

# 保留关键词列和年列
df = df[['Year-年', 'Keyword-关键词']]

# 将结果保存为新的CSV文件
df.to_csv('3.3关键词清洗.csv', index=False)

