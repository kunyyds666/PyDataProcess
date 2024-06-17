import pandas as pd
import joblib

# 加载模型
model_file = 'linear_regression_car_price_prediction_model.pkl'
model = joblib.load(model_file)

# 准备输入数据
print("请输入多组数据（每行输入一个样本，以空行结束输入）：")
input_data = []
while True:
    line = input().strip()
    if line == "":
        break
    input_data.append(line)

# 将输入数据转换为DataFrame
data = []
for line in input_data:
    values = line.split()
    data.append(values)
df = pd.DataFrame(data, columns=['SaleID', 'name', 'regDate', 'model', 'brand',
                                 'bodyType', 'fuelType', 'gearbox', 'power',
                                 'kilometer', 'notRepairedDamage', 'regionCode', 'creatDate'])

# 数据预处理（假设需要进行与训练集相同的预处理）

# 特征工程（假设需要进行与训练集相同的特征工程处理）

# 进行预测
X = df.drop(columns=['SaleID', 'name'])  # 排除 SaleID 和 name 列
predicted_prices = model.predict(X)

# 输出预测结果
print("预测结果：")
for i, price in enumerate(predicted_prices):
    print(f"样本 {i+1}: 预测价格为 {price}")
