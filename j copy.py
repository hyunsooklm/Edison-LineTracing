import cv2
import os
import numpy as np
from tracing import *
video=cv2.VideoCapture(-1)
redline = (0, 0, 255)

while(video.isOpened()):
    ret,image=video.read()
  #  cv2.imshow("original",image)

    image_otsu = image.copy()

    # image_otsu=image_otsu[240:,:]
    image_otsu_gray=cv2.cvtColor(image_otsu,cv2.COLOR_BGR2GRAY)
    # kernel=np.ones((3,3),np.uint8)


    # image_otsu = cv2.erode(image_otsu, kernel, iterations=5)
    # image_otsu = cv2.dilate(image_otsu, kernel, iterations=5)


    #현재 진행차선 검출용 이미지 자르기
    

    _,otsu=cv2.threshold(image_otsu_gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # 이미지 자르기 & 가우시안블러 & threshhold





    contours_otsu,_ = cv2.findContours(otsu.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    max_otsu = max(contours_otsu,key=lambda c:cv2.contourArea(c))
    # #max_contour찾기
    mmt_thr_otsu=cv2.moments(max_otsu)
    # #mmt

    #
    cx_otsu = int(mmt_thr_otsu['m10'] / mmt_thr_otsu['m00'])  # 무게중심_otsu x좌표
    cy_otsu = int(mmt_thr_otsu['m01'] / mmt_thr_otsu['m00'])  # 무게중심_otsu y좌표

    #
    cv2.line(image_otsu, (cx_otsu, 0), (cx_otsu, image_otsu.shape[0]), redline, 1)  # (cx,0)~(cx,세로길이)
    cv2.line(image_otsu, (0, cy_otsu), (image_otsu.shape[1], cy_otsu), redline, 1)  # (0,cy)~(가로길이,cy)

    #contour 그리기
    cv2.drawContours(image_otsu, max_otsu, -1, (0, 255, 0), 3)
    
    location=(cx_otsu+20,cy_otsu+20)
    font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    fontscale=1
    thickness=2


    cv2.putText(image_otsu,str(cx_otsu),location,font,fontscale,(0,0,255),thickness)
    cv2.imshow('otsu',image_otsu)
    key=cv2.waitKey(10)&0xFF    
    if key==ord('q'):
        break
    if 280<cx_otsu<360:
 #       straight(100)
        print("straiht")
    elif cx_otsu<280:
  #      left(40,70)
        print("turn left")
    elif cx_otsu>360:
  #      right(70,40)
        print("turn right") 
#GPIO.cleanup()
video.release()
cv2.destroyAllWindows()
print("end!!")