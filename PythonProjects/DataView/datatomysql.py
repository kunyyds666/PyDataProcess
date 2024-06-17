import pandas as pd
from sqlalchemy import create_engine

# 加载 Excel 文件
excel_file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'
df = pd.read_excel(excel_file_path)

# 连接到 MySQL 数据库
# 请根据实际情况修改数据库连接参数
username = 'root'
password = 'root'
host = 'localhost'
database = 'python_usedcars'
table_name = 'used_car_train'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')

# 将数据写入 MySQL 数据库
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

print("数据已成功写入 MySQL 数据库。")
