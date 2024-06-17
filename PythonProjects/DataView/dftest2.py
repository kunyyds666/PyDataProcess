import pandas as pd

# 加载 Excel 文件
excel_file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'
df = pd.read_excel(excel_file_path)

# 删除 seller 和 offerType 列
columns_to_drop = ['seller', 'offerType']
df.drop(columns=columns_to_drop, inplace=True)

# 保存更新后的 Excel 文件
updated_excel_file_path = 'X:\\data\\PythonData\\used_car_train_20200313_updated.xlsx'
df.to_excel(updated_excel_file_path, index=False)

print("seller 和 offerType 列已成功删除，并保存到更新后的 Excel 文件中。")
