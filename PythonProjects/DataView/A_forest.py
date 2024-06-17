# feature_importance_visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取线性回归特征重要性结果
print("正在读取线性回归特征重要性结果...")
linear_importance_df = pd.read_csv('../pythonProject/linear_regression_feature_importance.csv')
print("线性回归特征重要性结果读取完成！")

# 生成线性回归特征重要性可视化图
print("生成线性回归特征重要性可视化图...")
plt.figure(figsize=(10, 8))
sns.barplot(x='Importance', y='Feature', data=linear_importance_df)
plt.title('Feature Importance from Linear Regression')
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.savefig('feature.png')  # 替换为适当的文件名和路径
plt.show()
print("线性回归特征重要性可视化图生成完成！")

# 读取随机森林特征重要性结果
print("正在读取随机森林特征重要性结果...")
rf_importance_df = pd.read_csv('../pythonProject/random_forest_feature_importance.csv')
print("随机森林特征重要性结果读取完成！")

# 生成随机森林特征重要性可视化图
print("生成随机森林特征重要性可视化图...")
plt.figure(figsize=(10, 8))
sns.barplot(x='Importance', y='Feature', data=rf_importance_df)
plt.title('Feature Importance from Random Forest')
plt.xlabel('Importance')
plt.ylabel('Feature')

plt.savefig('forest.png')  # 替换为适当的文件名和路径

plt.show()
print("随机森林特征重要性可视化图生成完成！")
