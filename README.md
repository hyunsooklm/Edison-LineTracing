# Edison-LineTracing
line-tracing 대회의 기록

this is code for 2020Edison software -얀센매커니즘을 이용한 자율주행 로봇 만들기

this compose of 4 area
1. tracing.py ->manipulate motor of robots. straight, turn left, turn right, back.
2. stop_detection.py -> if there is stop_sign in robots_camera's insight, stop 5 seconds and start moving
3. direct.py -> 표지판에서 좌우인식. 정사각 네모를 잡고, 그 안에서 작은 정사각형의 무게중삼의 위치파악.
4. trace.py -> 기본적인 주행알고리즘은 검은색->직진, 흰검-> 흰색무게중심의 반대편, 흰색만-> 좌우회전
5. checkHSV.py-> stop_detection에서 hsv변환시 stop_sign이 잡히는 hsv값을 알아내기위한 코드. 