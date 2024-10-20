import cv2
import mediapipe as mp
import time

def capture_finger(cap, cx,cy, mpHands, hands, mpDraw):
    success, img = cap.read()
    
    if not success or img is None:
        print("Error: Could not read frame. "+str(img is None))
        return 0, 0
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        handLandmark = results.multi_hand_landmarks[0]
        for id, lm in enumerate(handLandmark.landmark):
            h, w,c = img.shape
            px, py = int(lm.x * w), int(lm.y * h)
            if id == 8:  # Index of the tip of the index finger
                cv2.circle(img, (px, py), 15, (255, 0, 0), cv2.FILLED)
                cx,cy = px, py
        mpDraw.draw_landmarks(img, handLandmark, mpHands.HAND_CONNECTIONS)
    
    cv2.imshow("Image", img)
    return cx,cy

def correct(x,y):
    max_x = 650
    max_y=500
    #if x <0:
    #    x=0
    #if y < 0:
    #    y =0
    
    return (max_x-x)*1.638,y*1.8
