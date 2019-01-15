# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:01:45 2019

@author: Velocity_carbon
"""

import datetime
import cv2
import time

cap = cv2.VideoCapture(0)

second=datetime.datetime.now().strftime('%S')

x=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    time.sleep(1)
    w =70
    h =120
    thresh=150
    minus =40
    x1 =100-minus
    y1 =150
    
    x2 =100+thresh-minus
    y2 =150
    
    x3 =100+(thresh*2)-minus
    y3 =150
    
    x4 =100+(thresh*3)-minus
    y4 =150
    
    cv2.rectangle(frame, (x1, y1), (x1+w, y1+h), (255, 255, 00), 2)
    cv2.rectangle(frame, (x2, y2), (x2+w, y2+h), (255, 255, 00), 2)
    cv2.rectangle(frame, (x3, y3), (x3+w, y3+h), (255, 255, 00), 2)
    cv2.rectangle(frame, (x4, y4), (x4+w, y4+h), (255, 255, 00), 2)
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    crop_img1 = frame[y1:y1+h, x1:x1+w]
    crop_img2 = frame[y2:y2+h, x2:x2+w]
    crop_img3 = frame[y3:y3+h, x3:x3+w]
    crop_img4 = frame[y4:y4+h, x4:x4+w]
    
    cv2.imshow('1croped',crop_img1)
    cv2.imshow('2croped',crop_img2)
    cv2.imshow('3croped',crop_img3)
    cv2.imshow('4croped',crop_img4)

    x=x+1
    
    
    #Saving 
    label1 = '.jpg'
    label1 = str(x) + label1
    dir_label1= 'D:/Python LCC data/L1/'
    label1= dir_label1 + label1    
    cv2.imwrite(label1 ,crop_img1)
    
    label2 = '.jpg'
    label2 = str(x) + label2
    dir_label2= 'D:/Python LCC data/L2/'
    label2= dir_label2 + label2    
    cv2.imwrite(label2 ,crop_img2)
    
    label3 = '.jpg'
    label3 = str(x) + label3
    dir_label3= 'D:/Python LCC data/L3/'
    label3= dir_label3 + label3    
    cv2.imwrite(label3 ,crop_img3)
    
    label4 = '.jpg'
    label4 = str(x) + label4
    dir_label4= 'D:/Python LCC data/L4/'
    label4= dir_label4 + label4    
    cv2.imwrite(label4 ,crop_img4)
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




    
    

currenttime=datetime.datetime.now().strftime('\n%H:%M')
print(currenttime)
timefile = open('time.txt','a')
timefile.write(currenttime)
timefile.close()