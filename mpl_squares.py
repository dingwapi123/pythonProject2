# 开发时间：2022/7/23 10:19

import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

print(plt.style.available)

# 设置图表标题并给坐标轴加上标签
ax.set_title("1", fontsize=24)
ax.set_xlabel("2", fontsize=19)
ax.set_ylabel("3", fontsize=13)
 
plt.show()
