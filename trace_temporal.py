import cv2
from tracing import *
import direction as Direction
import stop_detection as STOP 
import numpy as np

video = cv2.VideoCapture(-1)
location=(30,30)
font=cv2.FONT_HERSHEY_SIMPLEX
fontscale=1
thickness=3
STOP_DETECT_COUNT=0
while True:
    _, frame = video.read()
    D=Direction.direct_detection(frame,STOP_DETECT_COUNT)
    stop_frame=frame[55:,:]
    if STOP.stop_detection(stop_frame,STOP_DETECT_COUNT)==True:
        STOP_DETECT_COUNT+=1
        stop()
        sleep(5)
    elif D:
        if D=='R':
            right(100)
        else:
            left(100)
    else:        
        frame1 = frame.copy() #흰색용 복사
        frame2 = frame.copy() #검은색용 복사
        frame3 = frame.copy() #신호등, 표지판 
        #관심영역 아래로 설정

        gray1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        blur1 = cv2.GaussianBlur(gray1,(5,5),0)
        _,white_dst = cv2.threshold(blur1,240,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        white = white_dst[280:480,0:640]
        black=cv2.bitwise_not(white)
        #threshold
        #contour
        cv2.imshow('white',white)
        contours1,hierarchy = cv2.findContours(white.copy(), 1, cv2.CHAIN_APPROX_NONE)
        contours2,_=cv2.findContours(black.copy(), 1, cv2.CHAIN_APPROX_NONE)
        if len(contours1)>0 and len(contours2)>0: #흰 검 둘다잡힐떄
            c=max(contours1, key=cv2.contourArea)
            M=cv2.moments(c)
            try:
                cx=int(M['m10']/M['m00'])
                cy=int(M['m01']/M['m00'])
                #무게중심코드
            except ZeroDivisionError as e:
                print("what?")
                straight(100)
                continue
            if cx<=355:
                right(100)
            else:
                left(100)
        elif len(contours1)<=0 and len(contours2)>0: #검은색만 잡힐때
            straight(100)
        else:
            print("what is it?")
            pass
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):break
Motor_end()
frame.release()
cv2.destroyAllWindows()