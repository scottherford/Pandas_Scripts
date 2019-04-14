# Index/Match function ## better than VLOOKUP
## Search entire spreadsheets (by column or row)

# Two dataframes
## Goal: match the last name column in df_2 
### with the correct rows in df_1 

# List of solutions:

import pandas as pd 
import random

data_1 = {'id':[1002,1004,1006],
	'first_name':['Cersei','Daenerys','Arya']}

df_1 = pd.DataFrame(data=data_1)
df_1

data_2 = {'id':[1003,1004,1005,1002,1006],
	'last_name':['Tyrell','Targaryen','Snow','Lannister','Stark']}

df_2 = pd.DataFrame(data=data_2)
df_2

# Solution 1: Using.map()
%timeit
df_1['last_name'] = df_1.id.map(df_2.set_index('id')['last_name'].to_dict())
print('data frame 1 after procv')
display(df_1)

# Solution 2: Using.join()
%timeit
joined_df = df_1.set_index('id').join(df_2.set_index('id'))
joined_df

# Solution 3: Using.merge()
%timeit
merged_df = df_1.merge(df_2, how='left', on='id')
merged_df

# Solution 4: Using.concat()
%timeit
concat_df = pd.concat([df_1.set_index('id'), df_2.set_index('id').last_name], axis=1, sort='id', join='inner')
