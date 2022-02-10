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
        percent = process(fundus)
        origin = cv2.imread(originFolder+'/'+file_name)        
        

        if percent > 0.02527:       
            print(str(count) + ". 사용가능")
            print(file_name_no_extension)
            print("==================================")
            cv2.imwrite(destinationFolder_P+file_name_no_extension+".jpg",origin)
            #cv2.imwrite(destinationFolder_bP+file_name_no_extension+".jpg",fundus)
            count+=1

        else:
            print(str(count) + ". 사용할 수 없음")
            print(file_name_no_extension)
            print("==================================")
            cv2.imwrite(destinationFolder_N+file_name_no_extension+".jpg",origin)
            #cv2.imwrite(destinationFolder_bN+file_name_no_extension+".jpg",fundus)
            count+=1

        

    
        
                    
    
