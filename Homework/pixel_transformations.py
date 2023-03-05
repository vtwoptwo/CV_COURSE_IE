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


#set working directory
PATH = os.environ['PWD']

# Load the images
img1 = cv2.imread(PATH + '/Homework/images/scene_nocup.jpg', 0)
img2 = cv2.imread(PATH + '/Homework/images/scene_cup.jpg', 0)

# Convert to 8-bit grayscale images
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Take the absolute value of their difference
img3 = cv2.absdiff(img1, img2)

# Do a binary threshold of the resulting image
ret, img4 = cv2.threshold(img3, 50, 255, cv2.THRESH_BINARY)

# Display the results
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)

cv2.waitKey(0)
cv2.destroyAllWindows()


