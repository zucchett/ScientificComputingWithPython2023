#!/usr/bin/env python
# coding: utf-8

# In[8]:


#1

import pandas as pd
df=pd.read_csv('data/data_000637.txt', header=0, nrows=15000)
print(df)


# In[9]:


#2
maxvalue=df['BX_COUNTER'].max() + 1 
print(maxvalue)


# In[3]:


#e3
first_abs=(df['ORBIT_CNT'].iloc[0] * maxvalue + df['BX_COUNTER'].iloc[0] + df['TDC_MEAS'].iloc[0]) * 25
df['ABS_TIME']=((df['ORBIT_CNT'] * maxvalue + df['BX_COUNTER'] + df['TDC_MEAS']) * 25) - first_abs
df.head(10)


# In[19]:


#Zadanie4
s = pd.to_timedelta(df['ABS_TIME']).max()
print(s)


# In[12]:


#5
df1 = df.groupby('TDC_CHANNEL')['TDC_MEAS'].sum()
df1.sort_values(ascending=False, inplace=True)
df1.head(3)


# In[15]:


#6

df=pd.read_csv('data/data_000637.txt', header=0)
non_empty_orbits= df[df['TDC_MEAS'] > 0]['ORBIT_CNT'].nunique()

print(non_empty_orbits)


# In[17]:


#7
df=pd.read_csv('data/data_000637.txt', header=0)
unique_orbits = df[df['TDC_CHANNEL'] == 139]['ORBIT_CNT'].nunique()
print(unique_orbits)


# In[22]:


#8
df=pd.read_csv('data/data_000637.txt', header=0)
fpga_0 = df[df['FPGA'] == 0]['TDC_CHANNEL'].value_counts()
fpga_1 = df[df['FPGA'] == 1]['TDC_CHANNEL'].value_counts()
print(fpga_0)
print(fpga_1)


# In[23]:





# In[ ]:




