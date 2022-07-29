# 开发时间：2022/7/29 9:30
from Die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline
# 创建一个D6
die = Die()

# 掷骰子并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequences = []
for value in range(1, die.num_sides+1):
    frequence = results.count(value)
    frequences.append(frequence)

# 可视化
x_value = list(range(1, die.num_sides+1))
data = [Bar(x=x_value, y=frequences)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个D6 1000次的结果', xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='D6.html')










