import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data\\911.csv")

print(df.head())
print(df.info())

top = df['zip'].value_counts().head()
print('top zip codes:')
print(top)