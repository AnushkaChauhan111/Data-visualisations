import plotly.graph_objects as go
from random import randint
import plotly.offline
from d8_d8 import Die

#3 D6 dice
die1 = Die(6)
die2 = Die(6)
die3 = Die(6)
max_value = die1.num_sides+die2.num_sides+die3.num_sides
min_value = 3
sum_result = []
for x in range(1000):
    add = die1.roll()+die2.roll()+die3.roll()
    sum_result.append(add)

frequency = [0]*(max_value-min_value+1) # creates a list of 0 occuring 16 times( for 3 to 18 sums)
for x in sum_result: 
    if min_value<=x<=max_value:
        frequency[x-min_value] += 1

data = [go.Bar(x=sum_result,y=frequency)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = go.Layout(title = 'Result of rolling 3 D6 dice 1000 times',xaxis = x_axis_config,yaxis = y_axis_config)
plotly.offline.plot({'data':data,'layout': my_layout},filename = 'd6_3.html')

