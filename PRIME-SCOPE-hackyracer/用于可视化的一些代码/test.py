import matplotlib.pyplot as plt
import numpy as np

# 示例数据
repeat_nums = np.arange(1250, 20001, 986)
print(repeat_nums)
timing_differences = [6.7, 11.3, 15.4, 20.1, 26.8, 31.5, 34.5, 40.2, 41.5, 46.9, 50.2, 53.6, 59.6, 62.3, 67.0, 71.2, 73.7, 70.4, 69.8, 67.5]
errors = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]

# 创建图形和轴
fig, ax = plt.subplots()

# 绘制折线图
ax.errorbar(repeat_nums, timing_differences, fmt='-o', ecolor='red', capsize=5)

# 设置标签和标题
ax.set_xlabel('重复次数')
ax.set_ylabel('时间差异 (μs)')

# 显示图形
plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # 数据准备
# labels = ['0.05', '0.1', '0.15', '0.2', '0.25']
# values1 = [0.2, 0.4, 0.1, 0.03, 0.1]
# values2 = [0.7, 0.45, 0.23, 0.015, 0.02]

# # 设置柱形宽度
# bar_width = 0.35
# index = np.arange(len(labels))

# # 创建柱形图
# plt.bar(index, values1, bar_width, label='transmit0', color='skyblue')
# plt.bar(index + bar_width, values2, bar_width, label='transmit1', color='blue')

# # 添加标题和标签
# plt.title('Double Bar Chart Example')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.xticks(index + bar_width / 2, labels)  # 设置x轴标签的位置
# plt.legend()

# # 显示图形
# plt.show()

