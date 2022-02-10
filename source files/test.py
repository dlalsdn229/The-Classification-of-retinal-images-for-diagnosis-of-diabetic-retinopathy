import cv2
import os
import csv

#img = cv.imread(filesArray)
def process(img):
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
   
    return percent        

def process2(img):
    #중앙검출    
    imgr=cv2.resize(img,None,fx=0.3,fy=0.3)
    imgray = cv2.cvtColor(imgr,cv2.COLOR_BGR2GRAY)

    height = imgr.shape[0] 
    width = imgr.shape[1]
    
    mask = imgray[int(height *0.25) : int(height*0.75) , int(width*0.25) : int(width*0.75)]
    mask[mask<140] = 0

    mask_h=mask.shape[0]
    mask_w=mask.shape[1]

    mcount =0

    for x in range(0,mask_h):
       for y in range(0, mask_w):
          if mask[x][y] != 0:
              mcount=mcount+1
    
    mpercent = (mcount / (mask_h*mask_w)) *100
    print("mpercent = ",mpercent)
    #사용가능
    if mpercent > 0.03 and mpercent < 0.6:
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
    destinationFolder_A = "/Users/user/Desktop/test_output/ambi/"
    destinationFolder_bP = "/Users/user/Desktop/test_output/testP/"
    destinationFolder_bN = "/Users/user/Desktop/test_output/testN/"
    destinationFolder_bA = "/Users/user/Desktop/test_output/testambi/"

    
    if not os.path.exists(destinationFolder_P):
        os.mkdir(destinationFolder_P)
        
    for file_name in filesArray:
        file_name_no_extension = os.path.splitext(file_name)[0]
        fundus = cv2.imread(pathFolder+'/'+file_name)		
        percent = process(fundus)
        origin = cv2.imread(originFolder+'/'+file_name)
        flag = process2(origin)

        #csv
        '''
        with open('/Users/user/Desktop/density.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile,delimiter=',')
            writer.writerow([str(percent),str(flag)])     
            #csvfile.close()
        '''

        if percent > 0.02527 and flag==1:          
            print(str(count) + ". 사용가능")
            print(file_name_no_extension)
            print("==================================")
            cv2.imwrite(destinationFolder_P+file_name_no_extension+".jpg",origin)
            cv2.imwrite(destinationFolder_bP+file_name_no_extension+".jpg",fundus)
            count+=1

        elif percent <= 0.02527 and flag==0:
            print(str(count) + ". 사용할 수 없음")
            print(file_name_no_extension)
            print("==================================")
            cv2.imwrite(destinationFolder_N+file_name_no_extension+".jpg",origin)
            cv2.imwrite(destinationFolder_bN+file_name_no_extension+".jpg",fundus)
            count+=1

        else:
            print(str(count) + ". 모호함")
            print(file_name_no_extension)
            print("==================================")
            cv2.imwrite(destinationFolder_A+file_name_no_extension+".jpg",origin)
            cv2.imwrite(destinationFolder_bA+file_name_no_extension+".jpg",fundus)
            count+=1

    #csvfile.close()
        
                    
    
