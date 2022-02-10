import matplotlib.pyplot as plt
from matplotlib.image import imread
import cv2
import numpy as np


#시신경원판을 검출하는 코드 (optic disk)optic cup
img = cv2.imread("tt.jpg")
imgr=cv2.resize(img,None,fx=0.3,fy=0.3)
plt.show(imgr)
imgray = cv2.cvtColor(imgr,cv2.COLOR_BGR2GRAY)

cv2.imshow("original",imgray)

height = imgr.shape[0] 
width = imgr.shape[1]


mask = imgray[int(height *0.25) : int(height*0.75) , int(width*0.25) : int(width*0.75)]

np.savetxt("data.txt",mask,fmt="%d")

mask_h=mask.shape[0]
mask_w=mask.shape[1]

no_zero_pixel=0
total_brightness =0

for x in range(0,mask_h):
  for y in range(0, mask_w):
    total_brightness =+ mask[x][y]
    if mask[x][y] != 0:
      no_zero_pixel =+1

avg_brightness = (total_brightness / no_zero_pixel)
revision=0

if(avg_brightness < 15):
  #너무 어두운 사진
  mask[mask<256]=0
elif(avg_brightness <= 30):
  revision=avg_brightness * 4
  mask[mask<(avg_brightness + revision)]=0
elif(avg_brightness < 40):
  revision=avg_brightness * 3
  mask[mask<(avg_brightness + revision)]=0
elif(avg_brightness < 50):
  revision=avg_brightness * 1.8
  mask[mask<(avg_brightness + revision)]=0
elif(avg_brightness < 60):
  revision=avg_brightness * 1.4
  mask[mask<(avg_brightness + revision)]=0
elif(avg_brightness < 70):
  revision=avg_brightness * 1.2
  mask[mask<(avg_brightness + revision)]=0
elif(avg_brightness < 80):
  revision=avg_brightness * 1.0
  mask[mask<(avg_brightness + revision)]=0
elif(avg_brightness < 90):
  revision=avg_brightness * 0.6
  mask[mask<(avg_brightness + revision)]=0
elif(avg_brightness < 100):
  revision=avg_brightness * 0.6
  mask[mask<(avg_brightness + revision)]=0
elif(avg_brightness < 110):
  revision=avg_brightness * 0.4
  mask[mask<(avg_brightness + revision)]=0
elif(avg_brightness < 120):
  revision=avg_brightness * 0.3
  mask[mask<(avg_brightness + revision)]=0
else:
  revision=avg_brightness * 0.2
  mask[mask<(avg_brightness + revision)]=0

count =0

for x in range(0,mask_h):
  for y in range(0, mask_w):      
      if mask[x][y] != 0:          
          count=count+1
          no_zero_w=+1
          no_zero_h=+1


percent = (count / (mask_h * mask_w)) * 100
print(percent,"%")
print("평균밝기값 = ", avg_brightness)
print("마스킹 필터 값 = ", avg_brightness + revision)

          

#cv2.circle(mask,(x,y),10,(255,255,255),-1) 

cv2.imshow("mask",mask)
cv2.imshow("imgray", imgray)
cv2.waitKey()
cv2.destroyAllWindows()
