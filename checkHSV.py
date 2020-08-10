import cv2
import numpy as np

#################################################################

def empty(a):
    pass

# CREATE TRACKBAR
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)

cv2.createTrackbar("min_H","Result",0,255,empty)
cv2.createTrackbar("max_H","Result",0,255,empty)

cv2.createTrackbar("min_S","Result",0,255,empty)
cv2.createTrackbar("max_S","Result",0,255,empty)

cv2.createTrackbar("min_V","Result",0,255,empty)
cv2.createTrackbar("max_V","Result",0,255,empty)

video=cv2.VideoCapture(0)


while True:
    succeed,img=video.read()
    if succeed:
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        low_h=cv2.getTrackbarPos('min_H','Result')
        max_h=cv2.getTrackbarPos('max_H','Result')
        low_s=cv2.getTrackbarPos('min_S','Result')
        max_s=cv2.getTrackbarPos('max_S','Result')
        low_v=cv2.getTrackbarPos('min_V','Result')
        max_v=cv2.getTrackbarPos('max_V','Result')
        lower_red=np.array([low_h,low_s,low_v])
        upper_red=np.array([max_h,max_s,max_v])
        print((low_h,low_s,low_v))
        print((max_h,max_s,max_v))
        
        red_range=cv2.inRange(hsv,lower_red,upper_red)
        
        red_result=cv2.bitwise_and(img,img,mask=red_range)
        blur=cv2.GaussianBlur(red_result.copy(),(5,5),0)
        
        cv2.imshow("Result",blur)
        if cv2.waitKey(1)&0xFF==ord('q'):break
video.release()
cv2.destroyAllWindows()