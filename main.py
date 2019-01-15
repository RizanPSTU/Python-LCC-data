# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:01:45 2019

@author: Velocity_carbon
"""

import datetime
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
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