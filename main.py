# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:01:45 2019
@author: Velocity_carbon
"""

import datetime
import cv2

#import time

print('Main Start hoise :)')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)


x=0

new_s=int(datetime.datetime.now().strftime('%S'))

wait_time=10

check=(new_s + wait_time) % 60

mainstart =True
    
print('Press S to start')
while(True):
    # Capture frame-by-frame
    
    try:
        ret, frame = cap.read()
    except:
        print('Camra te prb\n') 
        break
        
        
    w =70
    h =120
    thresh=170
    minus =60
    x1 =100-minus
    y1 =150
    
    x2 =100+thresh-minus
    y2 =150
    
    x3 =100+(thresh*2)-minus
    y3 =150
    
    x4 =100+(thresh*3)-minus
    y4 =150
    
    pauseframe = frame
    cv2.rectangle(frame, (x1, y1), (x1+w, y1+h), (255, 255, 00), 2)
    cv2.rectangle(frame, (x2, y2), (x2+w, y2+h), (255, 255, 00), 2)
    cv2.rectangle(frame, (x3, y3), (x3+w, y3+h), (255, 255, 00), 2)
    cv2.rectangle(frame, (x4, y4), (x4+w, y4+h), (255, 255, 00), 2)
    
    # Display the resulting frame
    
    try:
        cv2.imshow('frame',frame)
    except:
        print('Show te prb\n')
        break
    
    
    if cv2.waitKey(1) & 0xFF == ord('p'):
        print('pause hoisi :3 abar S to startq')
        mainstart =True
    
    while(mainstart):
        try:
            ret, frame = cap.read()
        except:
            print('Camra te prb\n')
            break
            
        cv2.rectangle(frame, (x1, y1), (x1+w, y1+h), (255, 255, 00), 2)
        cv2.rectangle(frame, (x2, y2), (x2+w, y2+h), (255, 255, 00), 2)
        cv2.rectangle(frame, (x3, y3), (x3+w, y3+h), (255, 255, 00), 2)
        cv2.rectangle(frame, (x4, y4), (x4+w, y4+h), (255, 255, 00), 2)
        try:
            cv2.imshow('frame',frame)
        except:
            print('Show te prb\n')
            
        if cv2.waitKey(1) & 0xFF == ord('s'):
            print('Start Hoilam :3')
            mainstart =False

    
    
    #Crop
    crop_img1 = pauseframe[y1:y1+h, x1:x1+w]
    crop_img2 = pauseframe[y2:y2+h, x2:x2+w]
    crop_img3 = pauseframe[y3:y3+h, x3:x3+w]
    crop_img4 = pauseframe[y4:y4+h, x4:x4+w]
    
    #cv2.imshow('1croped',crop_img1)
    #cv2.imshow('2croped',crop_img2)
    #cv2.imshow('3croped',crop_img3)
    #cv2.imshow('4croped',crop_img4)

    
    
    new_s=int(datetime.datetime.now().strftime('%S'))
    if new_s == check:
        x=x+1
        check=(check+wait_time) % 60

        
        #Saving time
        currenttime=datetime.datetime.now().strftime('\n%H:%M:%S')
        write_time= datetime.datetime.now().strftime('h%Hm%Ms%S')
        print(x)
        print(write_time)
        #print(currenttime)
        timefile = open('time.txt','a')
        timefile.write(currenttime)
        timefile.close()

        #Saving 
        label1 = 'L1.jpg'
        label1 = str(x) +str(write_time)+ label1
        print(label1)
        dir_label1= 'D:/Python LCC data/L1/'
        label1= dir_label1 + label1    
        cv2.imwrite(label1 ,crop_img1)
        
        label2 = 'L2.jpg'
        label2 = str(x) +str(write_time)+ label2
        dir_label2= 'D:/Python LCC data/L2/'
        label2= dir_label2 + label2    
        cv2.imwrite(label2 ,crop_img2)
        
        label3 = 'L3.jpg'
        label3 = str(x) +str(write_time)+ label3
        dir_label3= 'D:/Python LCC data/L3/'
        label3= dir_label3 + label3    
        cv2.imwrite(label3 ,crop_img3)
        
        label4 = 'L4.jpg'
        label4 = str(x) +str(write_time)+ label4
        dir_label4= 'D:/Python LCC data/L4/'
        label4= dir_label4 + label4    
        cv2.imwrite(label4 ,crop_img4)
        
        print('New Ch',check)
        print('Old sec =',new_s)

    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

    
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

