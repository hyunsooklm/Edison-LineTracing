import cv2

try:
    cap=cv2.VideoCapture(-1)
except:
    print("no video!")



fourcc=cv2.VideoWriter_fourcc(*'DIVX')
out=cv2.VideoWriter('output.mp4',fourcc,30.0,(640,480))

while(cap.isOpened()):
    succeed,frame=cap.read()
    if succeed:
        cv2.imshow('image',frame)
        out.write(frame)

        if cv2.waitKey(1)&0xFF==ord('q'):
            break
    else:
         print("cap is not opened!")
         break

cap.release()
out.release()
cv2.destroyAllWindows()
