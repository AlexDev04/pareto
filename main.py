import pandas as pd
import matplotlib.pyplot as plot
from matplotlib.ticker import PercentFormatter

#asking for input

defects_cuantity = int(input('Enter number of defects: '))

#initing the  lists of defects

defects = []

list_counts = []
list_names = []

#adding defect class for better dev experience

class Defect:

    def __init__(self, number):
        self.number = number
    
    def ask_for_name(self):
        n = input(f'Enter name of {self.number} defects: ')
        self.name = n

    def ask_for_count(self):
        c = int(input(f'Enter count of {self.number} defects: '))
        self.count = c

#adding elements to defects list

for i in range (0, defects_cuantity):
    el = Defect(i+1)
    el.ask_for_name()
    el.ask_for_count()
    defects.append(el)
    list_names.append(el.name)
    list_counts.append(el.count)

defects.sort(key=lambda el: el.count)

#creating dataframe

df = pd.DataFrame({'count': list_counts})
df.index = list_names

#sorting values

df = df.sort_values(by='count', ascending=False)

#adding cumperc

df['cumperc'] = df['count'].cumsum()/df['count'].sum()*100

print(df)

#coloring the chart
color1 = 'green'
color2 = 'red'
line_size = 2

#create axis
fig, ax = plot.subplots()
ax.bar(df.index, df['count'], color=color1)

#adding cumperc line
ax2 = ax.twinx()
ax2.plot(df.index, df['cumperc'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())

#addind axis colors
ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)

#printing the chart
plot.show()