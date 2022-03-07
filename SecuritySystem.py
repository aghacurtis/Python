import mediapipe as mp
import cv2
import time
from datetime import datetime

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
mpFaceDetection = mp.solutions.face_detection
mpPose = mp.solutions.pose
pose = mpPose.Pose()
faceDetection = mpFaceDetection.FaceDetection()


pTime = 0
cTime = 0
img_counter = 0 


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    FaceResults = faceDetection.process(imgRGB)
    PoseResults = pose.process(imgRGB)
    
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
    if FaceResults.detections:
        for id, detection in enumerate(FaceResults.detections):
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih),  \
                  int(bboxC.width * iw), int(bboxC.height * ih)
            
            cv2.rectangle(img,bbox,(255,0,255), 2)
            cv2.putText(img, 'face detected', (10,400), cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)
            print("face detected")
            #img_name = "opencv_frame_{}.png".format(img_counter)
            #cv2.imwrite(img_name, img)
            print("Screenshot Taken")
            #img_counter+=1
            
  
            
    if PoseResults.pose_landmarks:
        mpDraw.draw_landmarks(img, PoseResults.pose_landmarks, mpPose.POSE_CONNECTIONS)
            
            
            
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime =cTime
    
    cv2.putText(img, f'FPS: {str(int(fps))}', (10,40), cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)
    cv2.putText(img, f'Time: {current_time}', (10,70), cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
