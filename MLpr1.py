#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import random
#Taking input from user
x=np.arange(6).reshape(3,2)
y=np.arange(10).reshape(2,5)
for i in range(3):
    for j in range(2):
        x[i][j]=input()
for i in range(2):
    for j in range(5):
        y[i][j]=input()
print("Saving following data into  the file :")
print(x)
print(y)
#filling the array with random number
w=np.arange(6).reshape(3,2)
z=np.arange(10).reshape(2,5)
for i in range(3):
    for j in range(2):
        w[i][j]=random.randint(1,10)
for i in range(2):
    for j in range(5):
        z[i][j]=random.randint(1,20)

print("Saving following data into  the file :")
print(w)
print(z)
#saving all data in file 
np.savetxt("ab.csv",x,delimiter=",")
np.savetxt("abc.csv",y,delimiter=",")
np.savetxt("c.csv",w,delimiter=",")
np.savetxt("b.csv",z,delimiter=",")


# 
