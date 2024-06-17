import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体路径，根据你的系统和字体文件路径进行修改
font_path = 'C:/Windows/Fonts/msyh.ttc'  # 示例中使用微软雅黑字体，根据实际情况修改

# 设置字体属性
plt.rcParams['font.family'] = 'Microsoft YaHei'  # 设置全局字体为微软雅黑
plt.rcParams['font.size'] = 12  # 设置全局字体大小

# 文件路径
file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'

# 加载数据集
df = pd.read_excel(file_path)

# 设置公里数区间和步长
bins = [0, 3, 6, 9, 12, 15]

# 划分公里数区间并计算每个区间的价格均值
df['kilometer_bin'] = pd.cut(df['kilometer'], bins=bins)
kilometer_avg_prices = df.groupby('kilometer_bin')['price'].mean()

# 绘制公里数与价格的关系图
plt.figure(figsize=(8, 6))
plt.plot(kilometer_avg_prices.index.astype(str), kilometer_avg_prices.values, marker='o')
plt.xlabel('公里数区间')
plt.ylabel('平均价格')
plt.title('不同公里数区间的平均价格')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('kilo.png')  # 替换为适当的文件名和路径
plt.show()



