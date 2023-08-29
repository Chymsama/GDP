#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import re


# In[3]:


data_path = 'D:\\codegym3\\'
data_name = 'GDPlist.csv'

df = pd.read_csv(data_path+data_name, encoding= 'unicode_escape')

df.head(3)


# In[4]:


df.shape


# In[5]:


df.dtypes


# In[7]:


t = df.groupby(['Continent'])['Country'].count()

print(t)


# In[13]:


import matplotlib.pyplot as plt

plt.hist(df['GDP (millions of US$)'], bins=10, edgecolor='k', alpha=0.7)

plt.title('Phân phối GDP của các quốc gia')
plt.xlabel('GDP (millions of US$)')
plt.ylabel('Số lượng quốc gia')

plt.show()


# In[14]:


t = df.groupby(['Continent'])['GDP (millions of US$)'].sum()

print(t)


# In[15]:


x = df.sort_values(by ='GDP (millions of US$)',ascending=False).head(10)

print(x)

