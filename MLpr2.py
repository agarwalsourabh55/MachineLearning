#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np 
x=np.arange(start=100,stop=125,step=1)
i=int(input("enter the value from where you want to start"))
if i in x:
    z=i+80
    b=np.arange(i,z,5).reshape(8,2)
    print(b)


# In[ ]:




