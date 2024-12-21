from pyecharts import options as opts
from pyecharts.charts import WordCloud, Line
from pyecharts.globals import SymbolType
import pandas as pd

# 读取数据
df = pd.read_csv('传统茶饮数据集_预处理后.csv')

# 提取关键词列
keywords = df['Keyword-关键词']

# 将关键词列转换为字符串类型
keywords = keywords.astype(str)

# 统计关键词出现的频率
keyword_counts = keywords.str.split(';').explode().value_counts().reset_index(name='频率')

# 提取频率前20的关键词，并删去频率最高的前两项，由于前两项数据为无效数据
top_20_keywords = keyword_counts.nlargest(20, '频率')[2:]

# 创建关键词云图
wordcloud = (
    WordCloud()
    .add("", [list(z) for z in zip(top_20_keywords['Keyword-关键词'], top_20_keywords['频率'])],
         word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="关键词云图"),
                     toolbox_opts=opts.ToolboxOpts(is_show=True))
)

# 创建关键词折线图
line = (
    Line()
    .add_xaxis(top_20_keywords['Keyword-关键词'].tolist())
    .add_yaxis("频率", top_20_keywords['频率'].tolist(),
               label_opts=opts.LabelOpts(is_show=False),
               markpoint_opts=opts.MarkPointOpts(
                   data=[opts.MarkPointItem(type_="max", name="最大值"), opts.MarkPointItem(type_="min", name="最小值")]
               ),
               markline_opts=opts.MarkLineOpts(
                   data=[opts.MarkLineItem(type_="average", name="平均值")]
               ))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="关键词频率折线图"),
        xaxis_opts=opts.AxisOpts(name="关键词", axislabel_opts=opts.LabelOpts(rotate=45, font_size=9)),
        yaxis_opts=opts.AxisOpts(name="频率"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=True)
    )
)

# 渲染图表到HTML文件
wordcloud.render("关键词云.html")
line.render("关键词折线图.html")