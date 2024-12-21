import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

# 读取CSV文件
data_csv = pd.read_csv('传统茶饮数据集_预处理后.csv')

# 统计单位的论文发表数量
unit_count = data_csv['Organ-单位'].value_counts()

# 找到出现次数最多的单位
max_count_unit = unit_count.idxmax()

# 去除出现次数最多的单位
filtered_unit_count = unit_count.drop(max_count_unit)

# 将数据转换为适合Echarts的格式
units = filtered_unit_count.index.tolist()
counts = filtered_unit_count.values.tolist()

# 创建柱状图
bar = (
    Bar()
   .add_xaxis(units)
   .add_yaxis("论文发表数量", counts)
   .set_global_opts(
        title_opts=opts.TitleOpts(title="单位论文发表数量统计（去除出现次数最多的单位）"),
        xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45}),
        yaxis_opts=opts.AxisOpts(name="数量"),
        toolbox_opts=opts.ToolboxOpts(is_show=True)
    )
)

# 渲染图表并保存为HTML文件
bar.render("论文发表单位.html")