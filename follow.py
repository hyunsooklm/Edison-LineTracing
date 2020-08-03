import cv2
import numpy as np

def folow():
    video=cv2.VideoCapture('./sample.mp4')
    while(video.isOpened()):
        succeed,frame=video.read()
        if succeed:
            frame=frame[:,:640]
            origin=frame.copy()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, line = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            kernel=np.ones((9,9),np.uint8)
            cv2.imshow("before closing",line)
            line = cv2.dilate(line, kernel, iterations=5) #검정색을 돋보이게, -> 1 or 0 == 1
            line = cv2.erode(line, kernel, iterations=5)  #흰색을 돋보이게, ->1 and 1 == 1
            contours_otsu, _ = cv2.findContours(line.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            contour = max(contours_otsu, key=lambda c: cv2.contourArea(c))
            cv2.imshow('closing',line)
            #boundingbox
            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

            #minarearect
            blackbox=cv2.minAreaRect(contour)
            (x_min,y_min),(w_min,h_min),ang=blackbox
            ang=int(ang)
            box=cv2.boxPoints(blackbox)
            box=np.int0(box)
            cv2.line(frame,tuple(map(int,(x_min,y_min))),tuple(map(int,(x_min,y_min+10))),(0,255,0),2)
            cv2.drawContours(frame,[box],0,(0,0,255),3)
            if ang<-45:
                ang=ang+90
            #putText
            cv2.putText(frame,str(ang),(310,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)
            #show
            cv2.imshow("contour",frame)
            cv2.imshow("origin",origin)
            if cv2.waitKey(10)&0xFF==ord('q'):
                break

        else:
            print("out")
            break
    video.release()
    cv2.destroyAllWindows()

folow()