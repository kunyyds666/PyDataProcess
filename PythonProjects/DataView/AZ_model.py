import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# 文件路径
file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'

# 读取数据
df = pd.read_excel(file_path)

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
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"Root Mean Squared Error (RMSE): {rmse}")

# 保存模型
model_file = 'linear_regression_car_price_prediction_model.pkl'
joblib.dump(model, model_file)
print(f"模型已保存到 {model_file}")
