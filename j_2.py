import cv2
#import os
import numpy as np
video = cv2.VideoCapture(-1)
video.set(cv2.CAP_PROP_FRAME_WIDTH,640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,480)


while(True):
    _, frame = video.read()

    frame1 = frame.copy() #흰색용 복사
    frame2 = frame.copy() #검은색용 복사
    frame3 = frame.copy() #신호등, 표지판 
    #관심영역 아래로 설정
    white_im = frame1[340:480,0:640]
    black_im = frame2[200:480,0:640]

    gray1 = cv2.cvtColor(white_im,cv2.COLOR_BGR2GRAY)
    blur1 = cv2.GaussianBlur(gray1,(5,5),0)
    _,thresh1 = cv2.threshold(blur1,60,255,cv2.THRESH_BINARY_INV)
    #이미지 반전
    dst=cv2.bitwise_not(thresh1)
    
    gray2 = cv2.cvtColor(black_im,cv2.COLOR_BGR2GRAY)
    blur2 = cv2.GaussianBlur(gray2,(5,5),0)
    _,thresh2 = cv2.threshold(blur2,60,255,cv2.THRESH_BINARY_INV)
    

    #윤곽선 검출(흰색)
    contours1,hierarchy = cv2.findContours(dst.copy(), 1, cv2.CHAIN_APPROX_NONE)
    #검은색
    contours2,hierarchy = cv2.findContours(thresh2.copy(), 1, cv2.CHAIN_APPROX_NONE)
    
    
    if len(contours1)>0:
        c=max(contours1, key=cv2.contourArea)
        M=cv2.moments(c)

        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])

        cv2.line(frame,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(frame,(0,cy),(1280,cy),(255,0,0),1)

        cv2.drawContours(frame, contours1,-1,(0,255,0),1)

        if cx<=220:
            print('turn right')

        if cx>=220 and cx<=420:
            print('o')

        if cx>=420:
            print('turn right')

    elif len(contours2)>0:
        c=max(contours2, key=cv2.contourArea)
        M=cv2.moments(c)

        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])

        cv2.line(frame,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(frame,(0,cy),(1280,cy),(255,0,0),1)

        cv2.drawContours(frame, contours1,-1,(0,255,0),1)

        if cx<=220:
            print('turn right')

        if cx>=220 and cx<=420:
            print('o')

        if cx>=420:
            print('turn left')





    cv2.imshow('threshhold',thresh1)
    cv2.imshow('BAN',dst)
    cv2.imshow('origin',frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):break