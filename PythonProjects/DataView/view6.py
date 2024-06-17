# feature_importance_calculation.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# 文件路径
file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'

# 检查文件是否存在并加载
print("正在加载文件...")
try:
    df = pd.read_excel(file_path)
    print("文件加载成功！")
except FileNotFoundError:
    print(f"文件未找到，请检查路径: {file_path}")
    exit()

# 分离特征和目标变量
print("正在分离特征和目标变量...")
X = df.drop(columns=['price'])
y = df['price']
print("分离完成！")

# 标准化特征数据
print("正在标准化特征数据...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("标准化完成！")

# 线性回归模型
print("正在训练线性回归模型...")
model = LinearRegression()
model.fit(X_scaled, y)
print("线性回归模型训练完成！")

# 获取特征的重要性（即系数）
print("获取线性回归模型特征的重要性...")
feature_importance = model.coef_

# 将特征名称和其对应的重要性值结合起来
feature_names = X.columns
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': feature_importance
})

# 按重要性值绝对值排序
importance_df['AbsImportance'] = importance_df['Importance'].abs()
importance_df = importance_df.sort_values(by='AbsImportance', ascending=False).drop(columns=['AbsImportance'])

# 保存线性回归特征重要性结果
importance_df.to_csv('linear_regression_feature_importance.csv', index=False)
print("线性回归特征重要性结果已保存到 'linear_regression_feature_importance.csv'")

# 随机森林回归模型
print("正在训练随机森林回归模型...")
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X, y)
print("随机森林回归模型训练完成！")

# 获取特征重要性
print("获取随机森林模型特征的重要性...")
rf_importance = rf_model.feature_importances_

# 将特征名称和其对应的重要性值结合起来
rf_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': rf_importance
})

# 按重要性值排序
rf_importance_df = rf_importance_df.sort_values(by='Importance', ascending=False)

# 保存随机森林特征重要性结果
rf_importance_df.to_csv('random_forest_feature_importance.csv', index=False)
print("随机森林特征重要性结果已保存到 'random_forest_feature_importance.csv'")
