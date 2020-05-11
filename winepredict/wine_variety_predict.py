#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
sw = stopwords.words('english')


# In[29]:


df=pd.read_csv('datasets/train.csv')
df


# In[30]:


df.info()
df.dropna(axis=0)


# In[31]:


X_train = df['review_description']
y_train = df['variety']

X_train.shape


# In[32]:


print ('There are %d varieties of wines in this dataset' % len(set(y_train)))


# In[33]:


labelEncoder = LabelEncoder()
y_train = labelEncoder.fit_transform(y_train)


# In[34]:


X_train = X_train.str.lower()


# In[35]:


list_aux = []
for phase_word in X_train:
    list_aux.append(' '.join([re.sub('[0-9\W_]', '', word) for word in phase_word.split() if not word in sw]))
X_train = list_aux


# In[36]:


countVectorizer = CountVectorizer()
X_train = countVectorizer.fit_transform(X_train)


# In[37]:


X_train.shape


# In[38]:


model = Sequential()
model.add(Dense(100, activation='relu', input_dim=len(countVectorizer.get_feature_names())))
model.add(Dense(units=y_train.max()+1, activation='sigmoid'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=2, verbose=1)


# In[39]:


scores = model.evaluate(X_train, y_train, verbose=1)
scores
print ('The accuracy of the model is %s' % scores[1])


# In[43]:





# In[ ]:





# In[ ]:




