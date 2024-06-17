import joblib
import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Page, Line, HeatMap, Pie
from pyecharts.globals import ThemeType
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# 文件路径
file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'

# 加载数据集
df = pd.read_excel(file_path)

# #############################创建模型################################################
# 分离特征和目标变量
X = df.drop(columns=['price', 'SaleID', 'name'])  # 排除 SaleID 和 name 列
y = df['price']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 计算均方根误差（RMSE）
rmse = mean_squared_error(y_test, y_pred)
print(f"Root Mean Squared Error (RMSE): {rmse}")

# 保存模型
model_file = 'linear_regression_car_price_prediction_model.pkl'
joblib.dump(model, model_file)
print(f"模型已保存到 {model_file}")

# #######################################创建车身类型平均价格柱状图#####################################
# 车身类型映射
body_type_mapping = {
    0: '豪华轿车', 1: '微型车', 2: '厢型车', 3: '大巴车', 4: '敞篷车', 5: '双门汽车', 6: '商务车', 7: '搅拌车'
}

# 替换bodyType列为车身类型名称
df['bodyType'] = df['bodyType'].map(body_type_mapping)

# 计算每种车身类型的平均价格
body_type_avg_prices = df.groupby('bodyType')['price'].mean().sort_values()

bar_body_type = (
    Bar()
    .add_xaxis(body_type_avg_prices.index.tolist())
    .add_yaxis("平均价格", body_type_avg_prices.values.tolist())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="不同车身类型的平均价格"),
        xaxis_opts=opts.AxisOpts(name="车身类型", axislabel_opts={"rotate": 45}),
        yaxis_opts=opts.AxisOpts(name="平均价格"),
        datazoom_opts=opts.DataZoomOpts()
    )
)

# ##############################创建品牌平均价格柱状图#######################################
# 品牌取别名
brand_aliases = {
    0: '哦迪', 1: '笨驰', 2: '短安', 3: '蜂田', 4: '包骂', 5: '扶特', 6: '学佛兰', 7: '鹿虎', 8: '骂自打', 9: '日崇',
    10: '汽鸭', 11: '死爬虫', 12: '现台', 13: '类可三思', 14: '握尔沃', 15: '非亚特', 16: '灵蛇', 17: '别哭',
    18: '打重', 19: '表智', 20: '学铁笼', 21: '接抱', 22: '压马哈', 23: '残利', 24: '鹿特司', 25: '发辣哩',
    26: '握口哦号', 27: '啊三顿·骂丁', 28: '不加底', 29: '啊尔发·罗迷瓯', 30: '懒薄基尼', 31: '啊三顿·骂丁',
    32: '发辣哩', 33: '握尔沃', 34: '扶特', 35: '笨驰', 36: '包骂', 37: '打重', 38: '狂犬', 39: '飞火'
}

# 替换品牌列为别名
df['brand'] = df['brand'].map(brand_aliases)

# 计算每个品牌的平均价格
brand_avg_prices = df.groupby('brand')['price'].mean().sort_values()

bar_brand = (
    Bar()
    .add_xaxis(brand_avg_prices.index.tolist())
    .add_yaxis("平均价格", brand_avg_prices.values.tolist())
    .set_global_opts(

        title_opts=opts.TitleOpts(title="各品牌平均价格"),
        xaxis_opts=opts.AxisOpts(name="品牌", axislabel_opts={"rotate": 45}),
        yaxis_opts=opts.AxisOpts(name="平均价格"),
        datazoom_opts=opts.DataZoomOpts(),

    )
)

# #######################################创建公里数和价格的折线图######################################
# 设置公里数区间和步长
bins = [0, 3, 6, 9, 12, 15]

# 划分公里数区间并计算每个区间的价格均值
df['kilometer_bin'] = pd.cut(df['kilometer'], bins=bins)
kilometer_avg_prices = df.groupby('kilometer_bin', observed=False)['price'].mean()

# 转换索引为字符串格式
kilometer_avg_prices.index = kilometer_avg_prices.index.astype(str)

# 创建折线图
line = (
    Line()
    .add_xaxis(kilometer_avg_prices.index.tolist())
    .add_yaxis("平均价格", kilometer_avg_prices.values.tolist(), symbol='circle', symbol_size=8)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="不同公里数区间的平均价格"),
        xaxis_opts=opts.AxisOpts(type_="category", name="公里数区间", axislabel_opts=opts.LabelOpts(rotate=45)),
        yaxis_opts=opts.AxisOpts(name="平均价格"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
    )
    .set_series_opts(
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(type_="max", name="最大值"),
                  opts.MarkPointItem(type_="min", name="最小值")]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        )
    )
)
# ########################################相关系数矩阵热力图#################################
# 选择数值列
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# 计算相关系数矩阵
correlation_matrix = df[numeric_cols].corr()

# 准备热力图数据
x_axis = correlation_matrix.columns.tolist()
y_axis = correlation_matrix.index.tolist()
data = [
    [i, j, correlation_matrix.iloc[i, j]]
    for i in range(len(y_axis))
    for j in range(len(x_axis))
]

# 创建热力图
heatmap = (
    HeatMap()
    .add_xaxis(x_axis)
    .add_yaxis(
        "相关系数",
        y_axis,
        data,
        label_opts=opts.LabelOpts(is_show=True, position="inside", formatter="{c:.2f}")
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Correlation Heatmap of Car Features"),
        visualmap_opts=opts.VisualMapOpts(min_=-1, max_=1, range_color=['#d73027', '#fee08b', '#1a9850']),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=0)),
    )
)

# ##############################饼图####################################
# 定义燃油类型映射
fuel_type_mapping1 = {0: '汽油', 1: '柴油', 2: '其他'}
fuel_type_mapping2 = {3: '天然气', 4: '混合动力', 5: '其他', 6: '电动'}

# 替换fuelType列为燃油类型名称
df['fuelType1'] = df['fuelType'].map(fuel_type_mapping1)
df['fuelType2'] = df['fuelType'].map(fuel_type_mapping2)

# 计算第一个饼状图数据：汽油、柴油和其他
fuel_type_counts1 = df[df['fuelType1'].isin(['汽油', '柴油', '其他'])]['fuelType1'].value_counts()

# 计算第二个饼状图数据：天然气、混合动力、其他和电动
fuel_type_counts2 = df[df['fuelType2'].isin(['天然气', '混合动力', '其他', '电动'])]['fuelType2'].value_counts()

# 绘制第一个饼状图
pie1 = (
    Pie()
    .add("", [list(z) for z in zip(fuel_type_counts1.index.tolist(), fuel_type_counts1.values.tolist())])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="汽油、柴油和其他燃油类型分布", pos_left="center"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="left", pos_bottom="bottom"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)

# 绘制第二个饼状图
pie2 = (
    Pie()
    .add("", [list(z) for z in zip(fuel_type_counts2.index.tolist(), fuel_type_counts2.values.tolist())])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="天然气、混合动力、其他和电动燃油类型分布", pos_left="center"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="left", pos_bottom="bottom"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)

# ###########################随机森林#############################################
# 读取线性回归特征重要性结果
linear_importance_df = pd.read_csv('linear_regression_feature_importance.csv')

# 生成线性回归特征重要性可视化图
linear_bar = (
    Bar()
    .add_xaxis(linear_importance_df['Feature'].tolist())
    .add_yaxis('Feature Importance', linear_importance_df['Importance'].tolist())
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Feature Importance from Linear Regression"),
        yaxis_opts=opts.AxisOpts(name='Feature'),
        xaxis_opts=opts.AxisOpts(name='Coefficient Value')
    )
)
linear_bar.render("linear_regression_feature_importance.html")

# 读取随机森林特征重要性结果
rf_importance_df = pd.read_csv('random_forest_feature_importance.csv')

# 生成随机森林特征重要性可视化图
rf_bar = (
    Bar()
    .add_xaxis(rf_importance_df['Feature'].tolist())
    .add_yaxis('Feature Importance', rf_importance_df['Importance'].tolist())
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Feature Importance from Random Forest"),
        yaxis_opts=opts.AxisOpts(name='Feature'),
        xaxis_opts=opts.AxisOpts(name='Importance')
    )
)

# 创建 Page 并添加图表
page = Page(layout=Page.SimplePageLayout)
page.add(bar_body_type, bar_brand, line, pie1, heatmap, pie2, linear_bar, rf_bar)

# 保存为 HTML 文件
page.render("draggable_combined_chart.html")
