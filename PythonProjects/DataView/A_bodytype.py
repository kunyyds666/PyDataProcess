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

# 车身类型映射
body_type_mapping = {
    0: '豪华轿车', 1: '微型车', 2: '厢型车', 3: '大巴车', 4: '敞篷车', 5: '双门汽车', 6: '商务车', 7: '搅拌车'
}

# 替换bodyType列为车身类型名称
df['bodyType'] = df['bodyType'].map(body_type_mapping)

# 计算每种车身类型的平均价格
body_type_avg_prices = df.groupby('bodyType')['price'].mean()

# 绘制价格图
plt.figure(figsize=(10, 6))
plt.bar(body_type_avg_prices.index, body_type_avg_prices.values, align='center', alpha=0.7)
plt.xlabel('车身类型')
plt.ylabel('平均价格')
plt.title('不同车身类型的平均价格')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('body_type.png', dpi=300)  # dpi参数可以设置图片的分辨率
plt.show()




