import cv2
import os
import numpy as np
video=cv2.VideoCapture('./sample.mp4')

redline = (0, 0, 255)

while(video.isOpened()):
    ret,image=video.read()
    image_adaptive = image.copy()
    image_otsu = image.copy()

    image=image[:,0:640]
    image_otsu=image_otsu[:,0:640]
    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    kernel=np.ones((3,3),np.uint8)

    image=cv2.erode(image,kernel,iterations=5)
    image=cv2.dilate(image,kernel,iterations=5)

    image_otsu = cv2.erode(image_otsu, kernel, iterations=5)
    image_otsu = cv2.dilate(image_otsu, kernel, iterations=5)

    _,thr=cv2.threshold(image_gray,65,255,cv2.THRESH_BINARY_INV)
    _,otsu=cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # 이미지 자르기 & 가우시안블러 & threshhold





    contours_thr,_=cv2.findContours(thr.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contours_otsu,_ = cv2.findContours(otsu.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    max_thr=max(contours_thr,key=lambda c:cv2.contourArea(c))
    max_otsu = max(contours_otsu,key=lambda c:cv2.contourArea(c))
    # #max_contour찾기
    mmt_thr_contour=cv2.moments(max_thr)
    mmt_thr_otsu=cv2.moments(max_otsu)
    # #mmt

    cx_thr = int(mmt_thr_contour['m10'] / mmt_thr_contour['m00'])  # 무게중심_thr x좌표
    cy_thr = int(mmt_thr_contour['m01'] / mmt_thr_contour['m00'])  # 무게중심_thr y좌표

    #
    cx_otsu = int(mmt_thr_otsu['m10'] / mmt_thr_otsu['m00'])  # 무게중심_otsu x좌표
    cy_otsu = int(mmt_thr_otsu['m01'] / mmt_thr_otsu['m00'])  # 무게중심_otsu y좌표

    cv2.line(image, (cx_thr, 0), (cx_thr, image.shape[0]), redline, 1)  # (cx,0)~(cx,세로길이)
    cv2.line(image, (0, cy_thr), (image.shape[1], cy_thr), redline, 1)  # (0,cy)~(가로길이,cy)

    #
    cv2.line(image_otsu, (cx_otsu, 0), (cx_otsu, image_otsu.shape[0]), redline, 1)  # (cx,0)~(cx,세로길이)
    cv2.line(image_otsu, (0, cy_otsu), (image_otsu.shape[1], cy_otsu), redline, 1)  # (0,cy)~(가로길이,cy)


    #contour 그리기
    cv2.drawContours(image, max_thr, -1, (0, 255, 0), 3)
    cv2.drawContours(image_otsu, max_otsu, -1, (0, 255, 0), 3)

    cv2.imshow('threshold',image)
    cv2.imshow('otsu',image_otsu)
    key=cv2.waitKey(10)&0xFF
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
print("end!!")