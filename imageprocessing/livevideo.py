#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
#starting camera
cap=cv2.VideoCapture(0)
# adding plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')

#adding plugin now saving video         #speed
output=cv2.VideoWriter('class.avi',plugin,100,(640,480))   
                                            #wdth  #hght

while cap.isOpened() :
    status,frame=cap.read()
    cv2.imshow('live',frame)
    # draw pattern 
    output.write(frame)   #sending video  to videoWrite
    if cv2.waitKey(10)  & 0xff == ord('q') :
        break
        
        
cv2.destroyAllWindows() #this will destroy all windows
cap.release()
    


# In[ ]:




