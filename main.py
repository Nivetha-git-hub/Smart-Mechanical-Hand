import serial
import time
from cvzone.SerialModule import SerialObject
from cvzone.HandTrackingModule import HandDetector
import cv2

#arduino = serial.Serial(port="COM3", baudrate=115200, timeout=.1)
#arduino.readline().decode('utf-8').rstrip()
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
mySerial= SerialObject("COM3",9600,1)
while True:
   
    success, img = cap.read()
    
    hands, img = detector.findHands(img)  
    # hands = detector.findHands(img, draw=False)  

    if hands:
        
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  
        bbox1 = hand1["bbox"]  
        centerPoint1 = hand1['center'] 
        handType1 = hand1["type"]  
        fingers1 = detector.fingersUp(hand1)
        print(fingers1)
        #value1=write_read(fingers1)
        mySerial.sendData(fingers1)

        if len(hands) == 2:
            
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  
            bbox2 = hand2["bbox"]  
            centerPoint2 = hand2['center'] 
            handType2 = hand2["type"]  

            fingers2 = detector.fingersUp(hand2)
            print(fingers2)
            #value2 = write_read(fingers2)
            mySerial.sendData(fingers2)

            
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  
            
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
