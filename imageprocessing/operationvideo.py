#!/usr/bin/env python
# coding: utf-8

# In[11]:


import cv2


# In[12]:


#starting camera
cap=cv2.VideoCapture(0)


# In[13]:


#while cap.isOpened() :
 #  #grayscaling
#    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#    cv2.imshow('live',frame)
#    cv2.imshow('livegray',grayimg)
#    if cv2.waitKey(10) & 0xff == ord('q') :
#        break
#cv2.destroyAllWindows()
#cap.release()


# In[ ]:


while cap.isOpened():
    status,frame=cap.read()
    #line
    cv2.line(frame,(0,0),(200,300),(0,255,0),3)
    #rectangle
    cv2.rectangle(frame,(50,50),(150,200),(0,0,255),2)
    #circle
    cv2.circle(frame,(200,300),100,(13,44,123),2)
    cv2.imshow('livegray',frame)
    if cv2.waitKey(10) & 0xff == ord('q') :
        break


# In[ ]:




