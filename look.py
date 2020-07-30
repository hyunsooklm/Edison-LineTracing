import cv2

try:
    video=cv2.VideoCapture('./output2.mp4')
except:
    print("failed")
while True:
    succeed,img=video.read()
    if succeed:
        cv2.imshow('img',img)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
    else:
         print("no camera opened")
         break
video.release()
cv2.destroyAllWindows()
