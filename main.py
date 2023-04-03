from cvzone.HandTrackingModule 
import HandDetector
import cv2

cap = cv2.VideoCapture(0)
 
detector = HandDetector(detectionCon=0.8, maxHands=2)
#mySerial= cvzone.SerialObject("COM3",9600,1)
while True:
   
    success, img1 = cap.read()
    img = cv2.resize(img1,(600,400))
    
    
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
        

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  
            bbox2 = hand2["bbox"] 
            centerPoint2 = hand2['center'] 
            handType2 = hand2["type"]  

            fingers2 = detector.fingersUp(hand2)
            print(fingers2)

            
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  
            # length, info = detector.findDistance(lmList1[8], lmList2[8])  
   
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()



# import tensorflow as tf
# # Convert the model.
# converter = tf. lite. TFLiteConverter. from_saved_model(fruits_dir)
# tflite_model = converter. convert()

# with open('cv_model.tflite', 'wb') as f:
#     f.write(tflite_model)
