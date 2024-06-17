import pandas as pd

# 加载 CSV 文件，指定空格作为分隔符
file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.csv'
df = pd.read_csv(file_path, sep=' ')

# 进行任何需要的数据处理，例如添加列、转换数据类型等
# 这里假设进行简单的处理示例
# df['new_column'] = df['old_column'] * 2

# 保存为 Excel 文件
excel_file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'
df.to_excel(excel_file_path, index=False)

print("处理后的数据已保存到 Excel 文件中。")
