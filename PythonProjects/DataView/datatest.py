import pandas as pd

# 文件路径
file_path = 'X:\\data\\PythonData\\used_car_train_20200313.csv'

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 处理数据：按空格分割每行数据，构建DataFrame
data = []
for line in lines:
    line = line.strip()  # 去除行尾的换行符
    if line:
        row = line.split()  # 按空格分割每行数据
        data.append(row)

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 可选：为DataFrame设置列名
# 假设列名已知或从数据集文档中获取，这里只是示例，需要根据实际情况调整
column_names = ['SaleID', 'name', 'regDate', 'model', 'brand', 'bodyType', 'fuelType', 'gearbox', 'power',
                'kilometer', 'notRepairedDamage', 'regionCode', 'seller', 'offerType', 'creatDate', 'price']
df.columns = column_names[:len(df.columns)]  # 根据数据列的数量设置列名

# 保存为 Excel 文件
excel_file_path = 'X:\\data\\PythonData\\used_car_train_20200313_processed.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"处理后的数据已保存到 {excel_file_path}")
