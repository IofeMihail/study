import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


path_to_file = '3_taxi_peru.csv'
taxi = pd.read_csv(path_to_file, sep=';',  parse_dates=['start_at', 'end_at', 'arrived_at'])

print(taxi.columns)
print(taxi.shape)
print((taxi.groupby('source')['journey_id'].count()/taxi.journey_id.count()*100).round(0))
# print((taxi.source.value_counts()/taxi.journey_id.count()*100).round(0)) normal way to count percent of sources
sources = taxi.groupby('source')['journey_id'].count()
print(sources.plot())