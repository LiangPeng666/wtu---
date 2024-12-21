import pandas as pd

# 读取数据
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
from pyecharts import options as opts
from pyecharts.charts import Line

# 将Year-年列中的缺失值填充为0
df['Year-年'] = df['Year-年'].fillna(0)

# 将Year-年列的数据类型转换为整数型
df['Year-年'] = df['Year-年'].astype(int)

# 统计每年发表的论文数量
yearly_counts = df['Year-年'].value_counts().sort_index().reset_index(name='论文数量')

# 创建折线图
line = (
    Line()
    .add_xaxis(yearly_counts['Year-年'].astype(str).tolist())
    .add_yaxis("论文数量", yearly_counts['论文数量'].tolist(),
               label_opts=opts.LabelOpts(is_show=False),
               markpoint_opts=opts.MarkPointOpts(
                   data=[opts.MarkPointItem(type_="max", name="最大值"), opts.MarkPointItem(type_="min", name="最小值")]
               ),
               markline_opts=opts.MarkLineOpts(
                   data=[opts.MarkLineItem(type_="average", name="平均值")]
               ))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="论文发表时间趋势"),
        xaxis_opts=opts.AxisOpts(name="年份"),
        yaxis_opts=opts.AxisOpts(name="论文数量"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        datazoom_opts=[opts.DataZoomOpts(type_="slider")]
    )
)

# 渲染图表到HTML文件
line.render("论文发表时间.html")