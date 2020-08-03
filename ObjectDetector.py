import cv2

################################################################
path = 'haarcascades/haarcascade_stop_default.xml'  # PATH OF THE CASCADE
cameraNo = 0                       # CAMERA NUMBER
objectName = 'Stop_Sign'       # OBJECT NAME TO DISPLAY
frameWidth= 640                     # DISPLAY WIDTH
frameHeight = 480                  # DISPLAY HEIGHT
color= (255,0,255)
#################################################################

# url = "http://192.168.0.3:8080" # Your url might be different, check the app
# cap = cv2.VideoCapture(url+"/video")
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

def empty(a):
    pass

# CREATE TRACKBAR
# cv2.namedWindow("Result")
# cv2.resizeWindow("Result",frameWidth,frameHeight+100)
# cv2.createTrackbar("Min Area","Result",0,100000,empty)
# cv2.createTrackbar("Brightness","Result",180,255,empty)
scaleVal = 1.1
neig = 3
# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier(path)

img=cv2.imread('images/v48.3087.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sign=cascade.detectMultiScale(gray,1.7,3)
for (x,y,w,h) in sign:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# if len(sign)!=0 && 빨간색 -> 정지 & 5초후 출발