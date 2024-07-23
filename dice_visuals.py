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
sum = []
for x in range(1000):
    ret = die_1.roll()+die_2.roll()
    sum.append(ret)

rep = []
for x in range(2,max_result+1):
    freq = sum.count(x)
    rep.append(freq)

data = [go.Bar(x=sum,y=rep)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = go.Layout(title='Results of rolling a D8 and a D8 1000 times',
 xaxis=x_axis_config, yaxis=y_axis_config)
plotly.offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')