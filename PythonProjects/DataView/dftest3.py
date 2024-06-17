import pandas as pd
import numpy as np

# 加载 Excel 文件
excel_file_path = 'X:\\data\\PythonData\\used_car_train_20200313_updated.xlsx'
df = pd.read_excel(excel_file_path)

# 删除包含空数据的行
df.dropna(inplace=True)


# 保存更新后的 Excel 文件
cleaned_excel_file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'
df.to_excel(cleaned_excel_file_path, index=False)

print("数据清洗完成，已保存到更新后的 Excel 文件中。")
