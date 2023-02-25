import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so


path_to_file = '3_taxi_peru.csv'
taxi = pd.read_csv(path_to_file, sep=';',  parse_dates=['start_at', 'end_at', 'arrived_at'])

print(taxi.dtypes)
print(taxi.shape)
print((taxi.groupby('source')['journey_id'].count()/taxi.journey_id.count()*100).round(0))
# print((taxi.source.value_counts()/taxi.journey_id.count()*100).round(0))
# normal way to count percent of sources
# print(taxi.groupby('source'))
print(taxi.value_counts('icon').to_frame('value'))

# sns.histplot(taxi, x='icon', hue='icon', shrink=.8)
# plt.show() #Вывод графика

# plt.figure(figsize=(16, 9))  # указываем размер графика, чтобы он был побольше
# sns.countplot(data=taxi, hue='end_state', x='source')  # строим график с нужными параметрами
# plt.show()

driver_score_counts = ((taxi.driver_score.value_counts()/taxi.driver_score.count()*100).round(2))\
    .reset_index()

driver_score_counts = driver_score_counts.rename(columns={'index': 'driver_score', 'driver_score': 'percentage'})
driver_score_counts = driver_score_counts.sort_values('driver_score')
print(driver_score_counts)

ax = sns.barplot(x='driver_score', y='percentage', data=driver_score_counts, color='blue', alpha=0.5)
ax.set(xlabel='Driver score', ylabel='Percentage')
sns.despine()  # убрать часть рамки графика
plt.show()

rider_score_counts = ((taxi.rider_score.value_counts()/taxi.rider_score.count()*100).round(2))\
    .reset_index()

rider_score_counts = rider_score_counts.rename(columns={'index': 'rider_score', 'rider_score': 'percentage'})
driver_score_counts = rider_score_counts.sort_values('rider_score')
print(rider_score_counts)

ax = sns.barplot(x='rider_score', y='percentage', data=rider_score_counts, color='blue', alpha=0.5)
ax.set(xlabel='Rider score', ylabel='Percentage')
sns.despine()  # убрать часть рамки графика
plt.show()
