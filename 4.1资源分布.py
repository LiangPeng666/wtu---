import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
data_csv = pd.read_csv('传统茶饮数据集_页码处理后.csv')

print('数据基本信息：')
data_csv.info()

# 查看数据集行数和列数
rows, columns = data_csv.shape

if rows < 100 and columns < 20:
    # 短表数据（行数少于100且列数少于20）查看全量数据信息
    print('数据全部内容信息：')
    print(data_csv.to_csv(sep='\t', na_rep='nan'))
else:
    # 长表数据查看数据前几行信息
    print('数据前几行内容信息：')
    print(data_csv.head().to_csv(sep='\t', na_rep='nan'))

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置中文字体为宋体
plt.rcParams['font.sans-serif'] = ['SimSun']

# 计算来源库分布
source_distribution = data_csv['SrcDatabase-来源库'].value_counts()

# 绘制来源库分布饼图
plt.pie(source_distribution, labels=source_distribution.index, autopct='%1.1f%%')
plt.axis('equal')
plt.title('来源库分布')
plt.show()

# 重新设定页码分布区间，步长大概为25，上限为150及以上
bins = [0, 25, 50, 75, 100, 125, 150, float('inf')]
labels = ['0-25', '26-50', '51-75', '76-100', '101-125', '126-150', '150及以上']
page_distribution = pd.cut(data_csv['PageCount-页码'], bins=bins, labels=labels, right=False).value_counts().sort_index()

# 绘制页码分布柱状图
plt.bar(page_distribution.index, page_distribution)
plt.xlabel('页码区间')
plt.ylabel('数量')
plt.title('页码分布')
plt.xticks(rotation=45)
plt.show()