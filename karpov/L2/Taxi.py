import pandas as pd

taxi = pd.read_csv('2_taxi_nyc.csv')
print(taxi.shape)
print(taxi.dtypes)
taxi = taxi.rename(columns={'pcp 01': 'pcp_01',
                            'pcp 06': 'pcp_06',
                            'pcp 24': 'pcp_24'})

print(taxi.value_counts('borough'))
print(taxi.pickups
      .sum())
print(taxi.groupby('borough')
      .pickups
      .sum()
      )
print(taxi.groupby('borough')
      .pickups
      .sum()
      .idxmin()
      )
print(taxi.groupby(['borough', 'hday'], as_index=False)
      .agg({'pickups': 'mean'}))

print(taxi.groupby(['borough', 'pickup_month'], as_index=False)
      .agg({'pickups': 'sum'})
      .sort_values('pickups', ascending=False))


def temp_to_celcius(temp_f):
    temp_c = (temp_f - 32) * 5.0 / 9.0
    return temp_c


print(temp_to_celcius(taxi['temp']))
