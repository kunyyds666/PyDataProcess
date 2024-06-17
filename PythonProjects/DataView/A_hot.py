import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据文件
file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'
df = pd.read_excel(file_path)

# 计算相关系数矩阵
correlation_matrix = df.corr()

# 生成热力图
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlation Heatmap of Car Features')
plt.savefig('hot.png')  # 替换为适当的文件名和路径
plt.show()


plt.close()  # 关闭当前图形，确保不会重叠显示
