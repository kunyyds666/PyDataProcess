import matplotlib.pyplot as plt

# 创建主图形布局
fig, axes = plt.subplots(3, 3, figsize=(18, 12))


# 加载并显示生成的图表
img1 = plt.imread('hot.png')
axes[1, 1].imshow(img1)
axes[1, 1].axis('off')

img2 = plt.imread('forest.png')
axes[0, 2].imshow(img2)
axes[0, 2].axis('off')

img3 = plt.imread('feature.png')
axes[0, 0].imshow(img3)
axes[0, 0].axis('off')

img4 = plt.imread('body_type.png')
axes[1, 0].imshow(img4)
axes[1, 0].axis('off')

img5 = plt.imread('brand_distribution.png')
axes[1, 2].imshow(img5)
axes[1, 2].axis('off')

img6 = plt.imread('kilo.png')
axes[2, 0].imshow(img6)
axes[2, 0].axis('off')

img7 = plt.imread('fuel_type_distribution.png')
axes[2, 2].imshow(img7)
axes[2, 2].axis('off')

axes[0,1].axis('off')
axes[2,1].axis('off')
# 留空最后一个子图位置

# 调整子图之间的间距
plt.tight_layout()

# 显示主图
plt.show()
