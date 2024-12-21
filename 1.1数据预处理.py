import pandas as pd

# 读取文件
excel_file = pd.ExcelFile('传统茶饮数据集.xlsx')

# 获取所有表名
sheet_names = excel_file.sheet_names
sheet_names
# 获取指定工作表中的数据
df = excel_file.parse('339篇传统茶饮')

# 查看数据的基本信息和前几行
print('数据基本信息：')
df.info()

# 查看数据集行数和列数
rows, columns = df.shape

if rows < 100 and columns < 20:
    # 短表数据（行数少于100且列数少于20）查看全量数据信息
    print('数据全部内容信息：')
    print(df.to_csv(sep='\t', na_rep='nan'))
else:
    # 长表数据查看数据前几行信息
    print('数据前几行内容信息：')
    print(df.head().to_csv(sep='\t', na_rep='nan'))
# 1. 处理缺失值：使用'未知'填充缺失值
df = df.fillna('未知')

# 2. 转换数据类型：将Year-年列转换为数值类型
df['Year-年'] = pd.to_numeric(df['Year-年'], errors='coerce')

# 3. 对数据进行排序：按Year-年列降序排列
df = df.sort_values(by='Year-年', ascending=False)

# 将结果保存为csv文件
csv_path = '传统茶饮数据集_预处理后.csv'
df.to_csv(csv_path)