import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


header = ['action', 'date_y_m', 'count_friday_6', 'count_friday_13', 'supermarket']
df = pd.read_csv('D:\\Users\\Misha\\Python\\Stat\\Tsk3\\13_6', encoding='utf-8', sep="\t", names=header)
print(df)
print(df.shape)

# ddof=0, нормировка дисперсии на N, а не на N-1, чтобы на N-1 надо убрать аргумент
print('Выброчное среднее: ' + str(df['count_friday_13'].mean()) +
      ', выборочная медиана: ' + str(df['count_friday_13'].median()) +
      ', выборочная дисперсия: ' + str(df['count_friday_13'].var(ddof=0).round(1)))

# Дисперсия ручками:
# df['deviation_13'] = (df['count_friday_13'] - df['count_friday_13'].mean()) ** 2
# print((df['deviation_13'].sum()/df['deviation_13'].count()).round(1))
df['count_13-count_6'] = df['count_friday_13'] - df['count_friday_6']

count_13count_6_count = df['count_13-count_6'].count()
count_13count_6_mean = df['count_13-count_6'].mean()
count_13count_6_var = df['count_13-count_6'].var(ddof=0)

print(df)
df['deviation^3_count_13-count_6'] = (df['count_13-count_6'] - count_13count_6_mean) ** 3
df['deviation^4_count_13-count_6'] = (df['count_13-count_6'] - count_13count_6_mean) ** 4

print('Выброчное среднее: ' + str(count_13count_6_mean.round(3)) +
      ', выборочная медиана: ' + str(df['count_13-count_6'].median()) +
      ', выборочная дисперсия: ' + str(count_13count_6_var.round(1)) +
      ', коэффициент ассиметрии: ' +
      str((df['deviation^3_count_13-count_6'].sum() / count_13count_6_count / (np.sqrt(count_13count_6_var) ** 3)).round(3)) +
      ', коэффициент эксцесса: ' +
      str(((df['deviation^4_count_13-count_6'].sum() / count_13count_6_count / (count_13count_6_var ** 2)) - 3).round(3)))

plt.xlabel('points')
plt.ylabel('Вероятность')
plt.hist(x=df['count_friday_13'], bins=5, density=True)
plt.show()

plt.xlabel('points')
plt.ylabel('Вероятность')
plt.hist(x=df['count_friday_6'], bins=5, density=True)
plt.show()

plt.xlabel('points')
plt.ylabel('Вероятность')
plt.hist(x=df['count_13-count_6'], bins=5, density=True)
plt.show()

plt.boxplot(df['count_friday_13'])
plt.show()

plt.boxplot(df['count_friday_6'])git
`
plt.show()

plt.boxplot(df['count_13-count_6'])
plt.show()
