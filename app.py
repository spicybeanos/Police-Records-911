import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

df = pd.read_csv("data\\911.csv")

print(df.head())
print(df.info())

top = df['zip'].value_counts().head(10)
print('top zip codes:')
print(top)

town = df['twp'].value_counts().head(4)
print('top townships for 911 calls')
print(town)

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df['reason'] = df['title'].apply(lambda x: x.split(':')[0])

df['day'] = df['timeStamp'].dt.day_of_week

day_map = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
df['day'] = df['day'].map(day_map)

reason = df['reason'].value_counts().head(10)
reason_ctr = df['reason'].value_counts()
print(reason)

ems_calls = df[df['reason'] == 'EMS']
ems_day_ctr = ems_calls['day'].value_counts()
print(ems_day_ctr)


reason_ctr.plot(kind='bar', figsize=(6,4), color=['skyblue','orange','red'])
plt.title('Reason frequency')
plt.xlabel('Reason')
plt.ylabel('Count')
plt.show()


