import plotly.graph_objects as go
from random import randint

class Die:
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1,self.num_sides+1)

values = []
for x in range(100):
    die_1 = Die(6)
    value = die_1.roll()
    values.append(value)

frequencies = []
for x in range(1,die_1.num_sides+1):
    freq = values.count(x)
    frequencies.append(freq)
print(frequencies)