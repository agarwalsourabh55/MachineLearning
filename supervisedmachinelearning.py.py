#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the library
import pandas as pd 


# In[2]:


# now read the librsrary
df=pd.read_csv("train_data.csv")


# In[3]:


# see the data 
df


# In[8]:


# take attribute of this data 
df.Survived[0:]


# In[34]:


# to count no. of deaths in titanic
count=0
for i in df.Survived[0:] :
    if i is 0:
        count+=1
        
print(count)        


# In[ ]:




