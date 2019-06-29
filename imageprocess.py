#!/usr/bin/env python
# coding: utf-8


import numpy as np
np.zeros((400,300))# for black image 
np.full((400,300),255)#for white image 


#gan library for face recognition
get_ipython().system('pip3 install opencv-contrib-python')
import cv2
#only for collab
#import matplotlib.pyplot as plt 

print(cv2.__version__)


#image reading 
img=cv2.imread('index.jpeg',1)  
#1 means same colour channel  ----
#0 means no colour ----
#-1 maintain image transparency ---
#split into BGR
#x,y,z=cv2.split(img)
#print shape 
img.shape
# opencv suppert BGR 
# type of img
type(img)
#to display image
cv2.line(img,(0,0),(100,30),(0,0,255),3)    # to display line on the image 
cv2.imshow('index',img)

# wait fro window to close
cv2.waitKey(0)    #mili/micro sec
# to  stop image editor


#from google.colab.patches import cv2_imshow

