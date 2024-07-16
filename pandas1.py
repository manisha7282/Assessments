import pandas as pd
df = pd.read_csv('C:\\Users\\ManishaBheemanpally\\Downloads\\data.csv')


print(df.head())
print(df.tail())
print(df.info())
df.dropna(inplace=True)
df.loc[7,'Duration'] = 45
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
df.drop_duplicates(inplace = True)    
print(df.to_string())

