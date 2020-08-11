import cv2
import os
import numpy as np
def direct_detection(frame,STOP_DETECT_COUNT):
    if STOP_DETECT_COUNT==0:
        return False
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)  
    _,thresh1 = cv2.threshold(blur,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
    thresh2=cv2.bitwise_not(thresh1)       ##흰색 검출


    blk,_ = cv2.findContours(thresh2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    ########검은색 비율 거르기
    blkroi = []
    whcont = []
    whco=[]

    for i in range(len(blk)):
        con = blk[i]
        area = cv2.contourArea(con)
        x,y,w,h = cv2.boundingRect(con)
        rarea = w*h
        if h/w>=0.8 and h/w<=1.2 and w<=400 and w>=100  and area/rarea>=0.5:
            blkroi.append([con,x,y,w,h])
            th = thresh1[y:y+h,x:x+w]
            wh,_ = cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            for i in range(len(wh)):
                con1 = wh[i]
                area1 = cv2.contourArea(con1)
                x1,y1,w1,h1 = cv2.boundingRect(con1)
                rarea1 = w1*h1
                if h1/w1>=0.8 and h1/w1<=1.2 and w1<=150 and w1>=20  and area1/rarea1>=0.7:
                    whco.append([con1,x,y,w,h])

            if len(whco)>0:
                total_x=0
                for i in range(len(whco)):
                    #cv2.drawContours(frame[y:y+h,x:x+w],whco[i][0],-1,(255,255,255),2)
                    c=whco[i][0]
                    M=cv2.moments(c)
                    try:
                        cx=int(M['m10']/M['m00'])
                        total_x+=cx
                    except:
                        pass
                if (w/2)<total_x:
                    print('left')
                    return 'L'
                else:
                    print('right')
                    return 'R'
            else:
                return False
        else:
            return False
    return False