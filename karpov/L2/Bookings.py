import pandas as pd

path_to_file = '2_bookings.csv'
bookings = pd.read_csv(path_to_file, sep=';')
bookings.columns = bookings.columns.str.replace(" ", "_").str.lower()
bookings_head = bookings.head(7)
print(bookings.shape)
print(bookings.dtypes)
print(bookings_head)
print(bookings.query('is_canceled == 0')
      .value_counts('country'))
print(bookings
      .groupby('hotel')['stays_total_nights']
      .mean()
      .round(2))
print(bookings.query('assigned_room_type != reserved_room_type').shape)
print(bookings.query('arrival_date_year == 2016').value_counts('arrival_date_month'))
print(bookings.query('arrival_date_year == 2017').value_counts('arrival_date_month'))
print(bookings.query('hotel == "City Hotel"').groupby('arrival_date_year')['arrival_date_month'].value_counts())
txt = "Children mean: {}, Babies mean: {}, Adults mean: {}"
print(txt.format(bookings.children.mean(), bookings.babies.mean(), bookings.adults.mean()))
bookings['total_kids'] = bookings.babies + bookings.children  # Create new column total_kids in df
print(bookings.groupby('hotel')['total_kids'].mean().round(2))
print(bookings.query('total_kids > 0')['is_canceled'].mean().round(4)*100)
print(bookings.query('total_kids == 0')['is_canceled'].mean().round(4)*100)
bookings['has_kids'] = bookings['total_kids'].astype(bool)
print((bookings[['has_kids', 'is_canceled']].value_counts()/bookings[['has_kids']].value_counts()*100).round(2))
print(bookings['has_kids'].head(6))
print(bookings[['has_kids', 'is_canceled']].head(6))