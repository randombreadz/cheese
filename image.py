import cv2
import time
import random

timeStart = time.time()

def take_snapshot():
   number = random.randint
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = "img" + str(number) + ".png"
        cv2.imwrite(imageName,frame)
        timeStart = time.time
        result = False
    return imageName
    print("Cheese!!!")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()