import plotly.graph_objects as go
from random import randint
import plotly.offline

class Die:
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1,self.num_sides+1)

die_1 = Die(8)
die_2 = Die(8)
max_result = die_1.num_sides + die_2.num_sides
min_result = 2
sum = []
for x in range(1000):
    ret = die_1.roll()+die_2.roll()
    sum.append(ret)

frequency = [0]* (max_result - min_result+1)
for x in sum:
    if min_result<=x<=max_result:
        frequency[x-2] += 1

data = [go.Bar(x=sum,y=frequency)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = go.Layout(title='Results of rolling a D8 and a D8 1000 times',
 xaxis=x_axis_config, yaxis=y_axis_config)
plotly.offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
