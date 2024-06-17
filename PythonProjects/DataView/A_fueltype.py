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

# 定义燃油类型映射
fuel_type_mapping1 = {0: '汽油', 1: '柴油', 2: '其他'}
fuel_type_mapping2 = {3: '天然气', 4: '混合动力', 5: '其他', 6: '电动'}

# 替换fuelType列为燃油类型名称
df['fuelType1'] = df['fuelType'].map(fuel_type_mapping1)
df['fuelType2'] = df['fuelType'].map(fuel_type_mapping2)

# 创建子图，一行两列
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 第一个饼状图：汽油、柴油和其他
fuel_type_counts1 = df[df['fuelType1'].isin(['汽油', '柴油', '其他'])]['fuelType1'].value_counts()
axes[0].pie(fuel_type_counts1, labels=fuel_type_counts1.index, autopct='%1.1f%%', startangle=140)
axes[0].set_title('汽油、柴油和其他燃油类型分布')
axes[0].axis('equal')  # 保证饼状图是圆形

# 第二个饼状图：液化石油气、天然气、混合动力、其他和电动
fuel_type_counts2 = df[df['fuelType2'].isin(['天然气', '混合动力', '其他', '电动'])]['fuelType2'].value_counts()
axes[1].pie(fuel_type_counts2, labels=fuel_type_counts2.index, autopct='%1.1f%%', startangle=140)
axes[1].set_title('天然气、混合动力、其他和电动燃油类型分布')
axes[1].axis('equal')  # 保证饼状图是圆形

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
plt.savefig('fuel_type_distribution.png', dpi=300)  # dpi参数可以设置图片的分辨率
plt.show()