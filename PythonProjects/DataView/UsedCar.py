import pandas as pd

# 读取数据集
df = pd.read_csv('X:\\data\\PythonData\\used_car_train_20200313.csv')

# 查看数据集的基本信息
print(df.info())

# 显示前几行数据
print(df.head())

# 处理日期字段，例如 'regDate' 和 'creatDate'
df['regDate'] = pd.to_datetime(df['regDate'], format='%Y%m%d')
df['creatDate'] = pd.to_datetime(df['creatDate'], format='%Y%m%d')

# 处理一些分类字段，例如 'bodyType', 'fuelType', 'gearbox', 'notRepairedDamage'
# 可以将这些字段转换为分类类型
df['bodyType'] = df['bodyType'].astype('category')
df['fuelType'] = df['fuelType'].astype('category')
df['gearbox'] = df['gearbox'].astype('category')
df['notRepairedDamage'] = df['notRepairedDamage'].astype('category')

# 检查空值
print(df.isnull().sum())

# 如果需要，可以填充或删除空值。例如：
df = df.fillna(method='ffill')

# 显示处理后的数据集信息
print(df.info())

# 保存处理后的数据到新的 CSV 文件
df.to_csv('processed_dataset.csv', index=False)
