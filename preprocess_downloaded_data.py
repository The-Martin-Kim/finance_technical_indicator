import pandas as pd

df = pd.read_csv('NASDAQ.csv')

df = df.drop(index=[0, 1])
df.reset_index(drop=True, inplace=True)

df.rename(columns={'Price':'Date'}, inplace=True)

df.to_csv('NASDAQ.csv', index=False)
