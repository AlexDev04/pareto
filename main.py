import pandas as pd
import matplotlib.pyplot as plot
from matplotlib.ticker import PercentFormatter

#asking for input

defects = int(input('Enter number of bugs: '))

list_counts = []
list_names = []

for i in range (0, defects):
    el_name = input(f'Enter name of {i+1} defects: ')
    list_names.append(el_name)
    el_count = int(input(f'Enter count of {i+1} defects: '))
    list_counts.append(el_count)

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