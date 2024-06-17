import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# 加载处理后的 Excel 文件
file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'
df = pd.read_excel(file_path)

# 检查数据
print(df.head())

# 分离特征和目标变量
X = df.drop(columns=['price'])
y = df['price']

# 标准化特征数据
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 创建和训练线性回归模型
model = LinearRegression()
model.fit(X_scaled, y)

# 获取特征的重要性（即系数）
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

# 打印特征重要性
print(importance_df)


from sklearn.ensemble import RandomForestRegressor

# 创建和训练随机森林回归模型
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# 获取特征重要性
rf_importance = rf_model.feature_importances_

# 将特征名称和其对应的重要性值结合起来
rf_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': rf_importance
})

# 按重要性值排序
rf_importance_df = rf_importance_df.sort_values(by='Importance', ascending=False)

# 打印特征重要性
print(rf_importance_df)
