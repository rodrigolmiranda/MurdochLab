#%% 0.0 Imports
import pandas as pd
import inflection
# import numpy as np

#%% 0.1 Helper Functions


#%% 0.1 Loading data

df_sales_raw = pd.read_csv('data/train.csv', low_memory = False)
df_store_raw = pd.read_csv('data/store.csv', low_memory = False)
df_raw = pd.merge(df_sales_raw, df_store_raw, how='left', on='Store')
# print(df_raw.columns)

#%% 1.0 Data Description

cols_old = ['Store', 'DayOfWeek', 'Date', 'Sales', 'Customers', 'Open', 'Promo',
            'StateHoliday', 'SchoolHoliday', 'StoreType', 'Assortment',
            'CompetitionDistance', 'CompetitionOpenSinceMonth',
            'CompetitionOpenSinceYear', 'Promo2', 'Promo2SinceWeek',
            'Promo2SinceYear', 'PromoInterval']
snakecase = lambda x: inflection.underscore(x)
cols_new = list(map(snakecase, cols_old))
df_raw.columns = cols_new

# #%% 1.2 Data Dimension

# print('Number of Rows:{}'.format(df_raw.shape[0]))
# print('Number of Cols:{}'.format(df_raw.shape[1]))

# #%% 1.2 Data Types

# df_raw['date'] = pd.to_datetime(df_raw['date'])
# print(df_raw.dtypes)


# #%% 1.2 Check NA
# print(df_raw.isna().sum())

# #%%