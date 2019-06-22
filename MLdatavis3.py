#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("bank.csv")


# In[43]:


df


# In[ ]:





# In[25]:


# to count the total noofproducts 
data_pie=df.groupby('Geography').NumOfProducts.count()


# In[38]:


df.head(5).plot.bar('Surname','Age') #creating a bar pyplot


# In[51]:



#making graph fro column geography and age 
import  matplotlib.pyplot
df.head(5).plot('Geography','Age')


# 

# In[68]:


#legend in graph
df.head(5).plot('Geography','Age',label='x')
df.head(5).plot('Geography','NumOfProducts',label='y')
plt.legend()


# In[69]:


#bar plots
from matplotlib import style 
import numpy as np


# In[78]:


#scatter graph

import  matplotlib.pyplot  as plt
from matplotlib import style
import numpy as np

plt.title("bank")
plt.xlabel("x-axis")
plt.ylabel("y-label")
plt.scatter('Geography','Age',label="hello",color='b',marker='x')
# marker can be - *,o,x,
#  only x , y in scattre is important
#  when both parameter have same number of element then we use scatter
plt.legend()
plt.grid(True,color='y')
plt.show()


# In[ ]:




