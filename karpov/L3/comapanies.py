import pandas as pd

path_to_file = '3_companies.csv'
companies = pd.read_csv(path_to_file, sep=';')
print(companies.head())
print(companies.groupby('company').income.mean())


