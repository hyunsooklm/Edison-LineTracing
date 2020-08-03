import cv2
import os
video=cv2.VideoCapture('./sample.mp4')

DIR='./N/'
count=0
while(video.isOpened()):
    ret,image=video.read()
    image=image[:,0:640]
    image=cv2.resize(image,dsize=(320,240),interpolation=cv2.INTER_AREA)
    cv2.imwrite('./N/pictureq_%d.png'%count,image)
    try:
        if not os.path.exists(DIR):
            os.mkdir(DIR)
    except OSError as e:
        print("failed to make directory")
        break
    print('Saved frame%d.png'%count)
    count+=1
    cv2.imshow('saved_picture',image)

    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
print("end!!")