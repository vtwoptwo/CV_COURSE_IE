"""
Take a picture of a scene. Then, without moving the camera, puta coffee cup in the scene and take a second picture. 

Load theseimages and convert both to 8-bit grayscale images.

a. Take the absolute value of their difference. Display the result,which should look like a noisy mask of a coffee mug.


b. Do a binary threshold of the resulting image using a levelthat preserves most of the coffee mug but removes some ofthe noise. 
Display the result. The “on” values should be set to 255.

"""


import cv2
import numpy as np
import os 
import sys
import matplotlib.pyplot as plt

#set working directory
PATH = os.environ['PWD']

# Load the images
img1 = cv2.imread(PATH + '/Homework/images/scene_nocup.jpg')
img2 = cv2.imread(PATH + '/Homework/images/scene_cup.jpg')

img1 = img1[2000:4032, 0:3024]
img2 = img2[2000:4032, 0:3024]

# import pdb; pdb.set_trace()
# Convert to 8-bit grayscale images
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#make image1 more monotone 
img1 = cv2.addWeighted(img1, 0.2, img1, 0, 0)

img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# add a small blur
img1 = cv2.GaussianBlur(img1,(9,9),0)
#
img2 = cv2.GaussianBlur(img2,(9,9),0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)


# Take the absolute value of their difference
img3 = cv2.absdiff(img1, img2 ) 

cv2.imshow('img3', img3)

plt.hist(img3.ravel(),256,[0,256]); plt.show()


# threshold 
ret, img4 = cv2.threshold(img3, 70, 255, cv2.THRESH_BINARY_INV)
ret, img5 = cv2.threshold(img3, 70, 255, cv2.THRESH_BINARY)


cv2.imshow('img4', img4)
cv2.imshow('img5', img5)


plt.hist(img4.ravel(),256,[0,256]); plt.show()
# Display the histogram of the pixels





