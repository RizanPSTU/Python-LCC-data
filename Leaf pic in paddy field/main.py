import numpy as np
import cv2


for x in range(145):
    #Hand segmentation
    
    numstr = '.jpg'
    numstr = str(x) + numstr
    img = cv2.imread(numstr)
        
    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    lower = np.array([0, 10, 60], dtype = "uint8") 
    upper = np.array([21, 150, 255], dtype = "uint8")
    
    mask = cv2.inRange(imghsv,lower,upper)
    mask = cv2.medianBlur(mask,257)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (305, 30))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, rect_kernel)
    
    
    image, contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    
    
    for cnt in contours:
        hull = cv2.convexHull(cnt)
        
    cv2.drawContours(mask, [hull],-1, 255, -1)
    #dst=cv2.drawContours(img , hull , -1, (0,0,255), 10)
    dst2 = cv2.bitwise_and(img, img, mask=mask)
    
        ## Save it
    string = 'm2.png'
    string = str(x) + string
    string2= 'E:/GoogleSyncedFolder/All projects/Lccpic/Seg/'
    mainstr= string2 + string    
    cv2.imwrite(mainstr ,dst2)
    
    ## Save it
    string = 'm2.png'
    string = str(x) + string
    string2= 'E:/GoogleSyncedFolder/All projects/Lccpic/'
    mainstr= string2 + string    
    cv2.imwrite(mainstr ,dst2)
    
    #Now segmenting leaf from hand
    numstr = 'm2.png'
    numstr = str(x) + numstr
    img = cv2.imread(numstr)
    
    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    lower = np.array([28, 55, 20], dtype = "uint8") 
    upper = np.array([75, 255, 255], dtype = "uint8")
    
    
    mask = cv2.inRange(imghsv,lower,upper)
        ## Save it
    string = 'mask.png'
    string = str(x) + string
    string2= 'E:/GoogleSyncedFolder/All projects/Lccpic/Seg/'
    mainstr= string2 + string    
    cv2.imwrite(mainstr ,mask)
    
    image, contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
     
    
    cnt = max(contours, key = cv2.contourArea)
    
    
    mask = np.zeros(img.shape[:2],np.uint8)
    
    cv2.drawContours(mask, [cnt], -1 , 255 , -1)
    
    dst = cv2.bitwise_and(img, img, mask=mask)
    
    
    ## Save it
    string = 'm.png'
    string = str(x) + string
    string2= 'E:/GoogleSyncedFolder/All projects/Lccpic/Seg/'
    mainstr= string2 + string    
    cv2.imwrite(mainstr ,dst)
    
