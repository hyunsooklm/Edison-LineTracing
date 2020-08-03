import cv2
import sys
try:
    cap=cv2.VideoCapture(0)
except:
    sys.exit()

while True:
    succeed,frame=cap.read()
    if succeed:
        # 검은라인만 잡을때
        blackline=cv2.inRange(frame,(0,0,0),(50,50,50))
        _,contours,__=cv2.findContours(blackline.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if(len(contours)>0):
            max_line=max(contours,)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()