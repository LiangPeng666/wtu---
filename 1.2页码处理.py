import pandas as pd

# 读取csv文件
df = pd.read_csv('传统茶饮数据集_预处理后.csv')

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


# 定义一个函数来提取页码
def extract_page_count(page_count_str):
    try:
        # 尝试使用正则表达式提取数字部分
        match = pd.to_numeric(page_count_str, errors='coerce')
        if pd.notnull(match):
            return int(match)
    except Exception as e:
        print(f"提取页码时出错: {e}")
    return None


# 将PageCount-页码列转换为整数型
df['PageCount-页码'] = df['PageCount-页码'].apply(extract_page_count)

# 将结果保存为csv文件
csv_path = '传统茶饮数据集_页码处理后.csv'
df.to_csv(csv_path)