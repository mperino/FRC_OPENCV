import cv2
import numpy as np
import matplotlib.pyplot as plt

version=0.1

# list 2 images (or image frame from video)
img1 = cv2.imread('./hatch.jpeg',0)
img2 = cv2.imread('./findin.jpg',0)

# similarity detector
orb = cv2.ORB_create()

# key points for each img
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf= cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck= True)

# sort matches
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3= cv2.drawMatches(img1, kp2, img2,kp2, matches[:10], None, flags=2 )
plt.imshow(img3)
plt.show()
