#!/usr/bin/env python
# coding: utf-8

# In[23]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv('student.csv')
df




# In[36]:


a=df['Marks']
b=df['Name']
plt.xlabel('marks')
plt.pie(df['Marks'],labels=df['Name'],shadow=True,autopct='%1.1f%%')
plt.show()
plt.xlabel('age')
plt.pie(df['Age'],labels=df['Name'],shadow=True,autopct='%1.1f%%')
plt.show()
plt.xlabel('Study_hours')
plt.pie(df['Study_hours'],labels=df['Name'],shadow=True,autopct='%1.1f%%')
plt.show()


# In[ ]:




