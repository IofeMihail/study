import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so


path_to_file = '3_user_data.csv'
user_data = pd.read_csv(path_to_file, sep=',')

path_to_file = '3_logs.csv'
logs = pd.read_csv(path_to_file, sep=',')

print(user_data.dtypes)
print(user_data.shape)

print(logs.dtypes)
print(logs.shape)

print(logs.value_counts('platform'))
print(logs.query('success').value_counts('client').head(9).sort_index())
print(logs.query('success').value_counts('platform'))
full_user_data = logs.join(user_data.set_index('client'), on='client')
print(full_user_data.query('premium == True')
      .value_counts('platform'))




# sns.displot(full_user_data.age)
# sns.displot(full_user_data, x='age', hue='premium', kde='True', stat='density', common_norm=False, bins=14)
# plt.show()
data = logs.query('success').value_counts('client')\
      .reset_index()\
      .rename(columns={0: 'values'})\
      .value_counts('values')\
      .reset_index()\
      .rename(columns={'values': 'counts_of_operations', 0: 'counts_of_users'})

# sns.barplot(data, x='counts_of_operations',  y='counts_of_users')
# plt.show()

print(full_user_data.shape)

age_data = full_user_data.query('success == True and platform == "computer"').\
      value_counts('age').\
      reset_index().\
      rename(columns={0: 'values'})

plt.figure(figsize=(20, 8))
g = sns.barplot(age_data, x='age',  y='values')
plt.show()
