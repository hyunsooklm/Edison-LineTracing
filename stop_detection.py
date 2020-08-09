import cv2
import os
import numpy as np

def empty():
    pass

lower_red = np.array([145,100,100])
upper_red = np.array([255,255,255])

def stop_detection(frame,count):
    if count>0:
        return False
    else:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        red_range = cv2.inRange(hsv, lower_red, upper_red)
        red_range = cv2.erode(red_range,None, iterations=2)
        red_range = cv2.dilate(red_range,None,iterations=2)
        cv2.imshow('red',red_range)
        cnts,_ = cv2.findContours(red_range.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        try:
            if len(cnts)>0: #컨투어잡고
                cnt2=max(cnts,key=cv2.contourArea)
                cv2.drawContours(frame,cnt2,-1,(0,255,0),3)
                #### contour 몇 개인지
                epsilon = 0.03*cv2.arcLength(cnt2,True)
                approx = cv2.approxPolyDP(cnt2,epsilon,True)
                size = len(approx)
                if size<6:  #삼ㄱ각형잡았을경우
                    print(size)
                    for q in range(size-1):
                        cv2.line(frame,tuple(approx[q][0]),tuple(approx[q+1][0]),(255,0,0),3)
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False
