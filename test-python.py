#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import sqlite3

# create an SQLite3 connection
conn = sqlite3.connect("./db/db")


# In[16]:


pd.options.display.precision = 5
df = pd.read_excel(r'skill_test_data.xlsx', sheet_name='data')


# In[ ]:


# Test/check dataframe loaded from excel file
df.head()


# In[ ]:


pivot3 = pd.pivot_table(df, index='Platform (Northbeam)', values=['Spend','Attributed Rev (1d)','Imprs','Visits','New Visits','Transactions (1d)','Email Signups (1d)'], aggfunc='sum')
pivot3 = pivot3.astype(float)

# Sort values by Revenue (descending)
pivot3.sort_values(by='Attributed Rev (1d)', ascending=False, inplace=True)

# Rename columns
pivot3.rename(columns = {'Spend':'Sum of Spend', 'Attributed Rev (1d)':'Sum of Attributed Rev (1d)', 'Imprs':'Sum of Imprs', 'Visits':'Sum of Visits', 'New Visits':'Sum of New Visits', 'Transactions (1d)':'Sum of New Transactions (1d)', 'Email Signups (1d)': 'Sum of Email Signups (1d)'}, inplace = True)

# Add Grand Total at the bottom row
pivot3 = pivot3.append(pivot3[['Sum of Spend','Sum of Attributed Rev (1d)','Sum of Imprs','Sum of Visits','Sum of New Visits','Sum of New Transactions (1d)','Sum of Email Signups (1d)']].sum().rename('Grand Total'))

# Rearrange columns
reindexed = pivot3.reindex(columns=['Sum of Spend','Sum of Attributed Rev (1d)','Sum of Imprs','Sum of Visits','Sum of New Visits','Sum of New Transactions (1d)','Sum of Email Signups (1d)'])

reindexed


# In[20]:


# upload to SQLite
reindexed.to_sql('pivot_table', conn, if_exists='replace')

# close connection
conn.close()

