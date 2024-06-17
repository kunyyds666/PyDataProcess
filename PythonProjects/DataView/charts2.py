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


