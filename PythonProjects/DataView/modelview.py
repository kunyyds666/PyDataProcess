import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

# 读取线性回归特征重要性结果
linear_importance_df = pd.read_csv('../pythonProject/linear_regression_feature_importance.csv')

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
rf_importance_df = pd.read_csv('../pythonProject/random_forest_feature_importance.csv')

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
rf_bar.render("random_forest_feature_importance.html")
