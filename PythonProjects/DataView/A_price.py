import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体路径，根据你的系统和字体文件路径进行修改
font_path = 'C:/Windows/Fonts/msyh.ttc'  # 示例中使用微软雅黑字体

# 设置字体属性
plt.rcParams['font.family'] = 'Microsoft YaHei'  # 设置全局字体为微软雅黑
plt.rcParams['font.size'] = 12  # 设置全局字体大小

# 文件路径
file_path = 'X:\\data\\PythonData\\used_car_train_20200313_cleaned.xlsx'

# 加载数据集
df = pd.read_excel(file_path)

# 为品牌取别名
brand_aliases = {
    0: '哦迪', 1: '笨驰', 2: '短安', 3: '蜂田', 4: '包骂', 5: '扶特', 6: '学佛兰', 7: '鹿虎', 8: '骂自打', 9: '日崇',
    10: '汽鸭', 11: '死爬虫', 12: '现台', 13: '类可三思', 14: '握尔沃', 15: '非亚特', 16: '灵蛇', 17: '别哭',
    18: '打重',
    19: '表智', 20: '学铁笼', 21: '接抱', 22: '压马哈', 23: '残利', 24: '鹿特司', 25: '发辣哩', 26: '握口哦号',
    27: '啊三顿·骂丁', 28: '不加底', 29: '啊尔发·罗迷瓯', 30: '懒薄基尼', 31: '啊三顿·骂丁', 32: '发辣哩',
    33: '握尔沃', 34: '扶特', 35: '笨驰', 36: '包骂', 37: '打重', 38: '狂犬', 39: '飞火'
}

# 替换品牌列为别名
df['brand'] = df['brand'].map(brand_aliases)

# 计算每个品牌的平均价格
brand_avg_prices = df.groupby('brand')['price'].mean()

# 绘制价格图
plt.figure(figsize=(12, 6))
plt.bar(brand_avg_prices.index, brand_avg_prices.values, align='center', alpha=0.7)
plt.xlabel('品牌')
plt.ylabel('平均价格')
plt.title('各品牌平均价格')
plt.xticks(rotation=45, ha='right')  # 旋转品牌名，使其不重叠显示
plt.grid(True)
plt.tight_layout()

plt.savefig('brand_distribution.png', dpi=300)  # dpi参数可以设置图片的分辨率
plt.show()
