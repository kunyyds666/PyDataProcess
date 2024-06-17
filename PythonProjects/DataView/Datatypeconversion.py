import pandas as pd
import numpy as np

# 加载 Excel 文件
excel_file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'
df = pd.read_excel(excel_file_path)

# 确保 bodyType 列的值在 0-7 之间
valid_body_types = set('01234567')
df['bodyType'] = df['bodyType'].apply(lambda x: x if x in valid_body_types else None)

# 将 notRepairedDamage 列的 '-' 值替换为随机 0 或 1
df['notRepairedDamage'] = df['notRepairedDamage'].apply(lambda x: np.random.choice(['0', '1']) if x == '-' else x)

# 将 bodyType 和 notRepairedDamage 列转换为整数类型
df['bodyType'] = df['bodyType'].astype('int64', errors='ignore')
df['notRepairedDamage'] = df['notRepairedDamage'].astype('int64', errors='ignore')

# 保存更新后的 Excel 文件
processed_excel_file_path = 'X:\\data\\PythonData\\used_car_train_20200313_final_processed.xlsx'
df.to_excel(processed_excel_file_path, index=False)

print("已将 object 类型的列转换为整数类型，并保存到更新后的 Excel 文件中。")
