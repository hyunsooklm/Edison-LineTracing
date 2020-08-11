import cv2
import os
import numpy as np
from tracing import *

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
        red_range = cv2.erode(red_range,None, iterations=1)
        red_range = cv2.dilate(red_range,None,iterations=1)

        #thresh 후 흰색에서 contour찾기 vs 붉은색에서 contour찾기
        # gray1 = cv2.cvtColor(red_range,cv2.COLOR_BGR2GRAY)
        # blur1 = cv2.GaussianBlur(gray1,(5,5),0)
        # _,white_dst = cv2.threshold(blur1,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # cv2.imshow('white',white_dst)
        cnts,_ = cv2.findContours(red_range.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        try:
            if len(cnts)>0: #컨투어잡고
                cnt2=max(cnts,key=cv2.contourArea)
                # cv2.drawContours(frame,cnt2,-1,(0,255,0),3)
                # #### contour 몇 개인지
                epsilon = 0.03*cv2.arcLength(cnt2,True)
                approx = cv2.approxPolyDP(cnt2,epsilon,True)
                size = len(approx)
                if size<6:  #삼ㄱ각형잡았을경우
                #    print(size)
                    # for q in range(size-1):
                    #     cv2.line(frame,tuple(approx[q][0]),tuple(approx[q+1][0]),(255,0,0),3)
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False
if __name__ == "__main__":
    video=cv2.VideoCapture(0)
    count=0
    while True:
        ret,frame=video.read()
        frame=frame[70:,:]
        ret=stop_detection(frame,count)
        if ret==True:
            count+=1
            stop()
            sleep(5)
            continue
        straight(100)
        if cv2.waitKey(1)&0xFF==ord('q'):break
    video.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()