import cv2 as cv
import tensorflow as tf

capture = cv.VideoCapture(0)

#check if camera can open
if not capture.isOpened(): 
    print("Cannot open camera :(")
    exit()

while True: 
    #caputre each frame 
    ret, frame = capture.read()

    #check if frame is captured
    if not ret: 
        print("Aur naur, frame not captured")
        break

    cv.imshow('frame', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

    