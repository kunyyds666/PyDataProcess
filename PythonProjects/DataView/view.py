import pandas as pd

# 加载 Excel 文件
excel_file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'
train_data = pd.read_excel(excel_file_path)

# 使用 .info() 方法查看数据类型和数据量
train_data.info()
