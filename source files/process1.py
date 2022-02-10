import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("000000256-20180919@092238-L3-S.jpg")

height = img.shape[0] 
width = img.shape[1]
h = int(height * 0.4)
w = int(width * 0.4)
count = 0

for x in range(0,width - w):
    for y in range(0,height - h):
        if img.item(y+int(h/2),x+int(w/2),0) == 0 and img.item(y+int(h/2),x+int(w/2),1) == 0 and img.item(y+int(h/2),x+int(w/2),2) == 0 :
            count = count + 1

print(count)
print(width * height)    
    

percent = count / ((width-w)*(height-h))
print(percent)


