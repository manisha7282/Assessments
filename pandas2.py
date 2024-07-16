import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\ManishaBheemanpally\\Downloads\\data.csv')
x=df.corr()
print(x)
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()