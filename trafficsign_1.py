import cv2
import os
import numpy as np
video=cv2.VideoCapture(0)

video.set(cv2.CAP_PROP_FRAME_WIDTH,640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,480)


while True:
    _, frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,100,200)
    
    cv2.imshow('blur',blur)
    _,thresh1 = cv2.threshold(blur,60,255,cv2.THRESH_BINARY)        ##흰색 검출
    _,thresh2 = cv2.threshold(blur,90,255,cv2.THRESH_BINARY_INV)    ##검은색 검출


    cv2.imshow('canny',thresh1)
    # cv2.imshow('thresh2',thresh2)

    blk,_ = cv2.findContours(thresh2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    wh,_ = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    


    ########검은색 비율 거르기
    blkroi = []

    for i in range(len(blk)):
        con = blk[i]
        area = cv2.contourArea(con)
        x,y,w,h = cv2.boundingRect(con)
        rarea = w*h

        if h/w>=0.8 and h/w<=1.2 and w<=200 and w>=30  and area/rarea>=0.5:
            blkroi.append([con,x,y,w,h])
    ########
    
    ########흰색 비율 거르기
    whroi = []

    for i in range(len(wh)):
        con1 = wh[i]
        area = cv2.contourArea(con1)
        x,y,w,h = cv2.boundingRect(con1)
        rarea = w*h

        if len(blkroi)>0:
            for i in range(len(blkroi)):
                if y>blkroi[i][2] and y+h<(blkroi[i][2]+blkroi[i][4]) and x>blkroi[i][1] and x+w<(blkroi[i][1]+blkroi[i][3]):
                    whroi.append(con1)
                    print("here")
                    for i in range(len(blk1)):
                        c=blk1[i]
                        M=cv2.moments(c)
        
                        cx=int(M['m10']/M['m00'])
        
                        b=min(whroi,key=cv2.contourArea)
                        m=cv2.moments(b)

                        bx=int(m['m10']/m['m00'])

                        if cx>=bx:
                            print('right')

                        if cx<=bx:
                            print('left')

        
 
    for i in range(len(blkroi)):
        blk1=blkroi[i][0]
    
    try:
        cv2.drawContours(frame,blk1,-1,(0,0,255),3)
    except:
        pass
    cv2.drawContours(frame,whroi,-1,(0,255,0),3)

    frame1 = frame.copy()
    cv2.line(frame,(320,100),(320,150),(255,0,0),3)
    print(len(blkroi))
    
    # try:
    #     for i in range(len(blk1)):
    #         c=blk1[i]
    #         M=cv2.moments(c)
        
    #         cx=int(M['m10']/M['m00'])
        
    #         b=min(whroi,key=cv2.contourArea)
    #         m=cv2.moments(b)

    #         bx=int(m['m10']/m['m00'])

    #         if cx>=bx:
    #             print('right')

    #         if cx<=bx:
    #             print('left')
    # except:
    #     pass      
    cv2.imshow('frame',frame)
    # contourditec
    if cv2.waitKey(1)&0xFF==ord('q'):break
    
video.release()
cv2.destroyAllWindows()

