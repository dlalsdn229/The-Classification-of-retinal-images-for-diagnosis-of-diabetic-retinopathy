import cv2
import os
import csv

     

def process2(img):
    #중앙검출    
    imgr=cv2.resize(img,None,fx=0.3,fy=0.3)
    imgray = cv2.cvtColor(imgr,cv2.COLOR_BGR2GRAY)
     
    height = imgr.shape[0] 
    width = imgr.shape[1]
    
    mask = imgray[int(height *0.25) : int(height*0.75) , int(width*0.25) : int(width*0.75)]

   
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
        revision=avg_brightness * 0.5
        mask[mask<(avg_brightness + revision)]=0
    elif(avg_brightness < 120):
        revision=avg_brightness * 0.5
        mask[mask<(avg_brightness + revision)]=0
    else:
        revision=avg_brightness * 0.3
        mask[mask<(avg_brightness + revision)]=0

    mcount =0
    
    for x in range(0,mask_h):
      for y in range(0, mask_w):      
          if mask[x][y] != 0:          
              mcount=mcount+1
              no_zero_w=+1
              no_zero_h=+1
   
    
    print("평균밝기값 = ", avg_brightness)
    print("마스킹 필터 값 = ", avg_brightness + revision)
    
    mpercent = (mcount / (mask_h*mask_w)) *100
    print("mpercent = ",mpercent)
    #사용가능
    if mpercent > 0.02 and mpercent < 0.95:#0.03
        return 1
    #사용불가능
    else:
        return 0      

if __name__ == "__main__":

    
    count = 1    
    
    pathFolder = "/Users/user/Desktop/vesseloutput"
    originFolder = "/Users/user/Desktop/optosview"
    
    filesArray = [x for x in os.listdir(pathFolder) if os.path.isfile(os.path.join(pathFolder,x))]
    
    destinationFolder_P = "/Users/user/Desktop/test_output/positive/"
    destinationFolder_N = "/Users/user/Desktop/test_output/negative/"
    destinationFolder_bP = "/Users/user/Desktop/test_output/testP/"
    destinationFolder_bN = "/Users/user/Desktop/test_output/testN/"

    
    if not os.path.exists(destinationFolder_P):
        os.mkdir(destinationFolder_P)
        
    for file_name in filesArray:
        file_name_no_extension = os.path.splitext(file_name)[0]
        fundus = cv2.imread(pathFolder+'/'+file_name)		
        
        origin = cv2.imread(originFolder+'/'+file_name)
        flag = process2(origin)

       
        if flag==1:          
            print(str(count) + ". 사용가능")
            print(file_name_no_extension)
            print("==================================")
            cv2.imwrite(destinationFolder_P+file_name_no_extension+".jpg",origin)
            cv2.imwrite(destinationFolder_bP+file_name_no_extension+".jpg",fundus)
            count+=1

        else:
            print(str(count) + ". 사용할 수 없음")
            print(file_name_no_extension)
            print("==================================")
            cv2.imwrite(destinationFolder_N+file_name_no_extension+".jpg",origin)
            cv2.imwrite(destinationFolder_bN+file_name_no_extension+".jpg",fundus)
            count+=1
        

  
        
                    
    
