#INITIAL SETUP
#----------------------------------------------------------------
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
import os
import time

folderPath = 'frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]

intro =  graphic[0] # read frames\img 1 in the intro variable
kill = graphic[1] # read frames\img 2 in the kill variable
winner = graphic[2]# read frames\img 3 in the winner variable
cam = cv2.VideoCapture(0) #read the camera
detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)

maxMove = 6500000
ret, frame = cam.read()
ref = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#sets the minimum confidence threshold for the detection
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frameDelta = cv2.absdiff(ref, gray)
thresh = cv2.threshold(frameDelta, 20, 255, cv2.THRESH_BINARY)[1]
change = np.sum(thresh)

#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------

folPath = 'img'
onii = os.listdir(folPath)

gra = [cv2.imread(f'{folPath}/{imPath}') for imPath in onii]
sqr_img = gra[1] # read img\sqr (1) in the sqr_img variable
mlsa = gra[0] # read img\mlsa in the mlsa variable


#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED

cv2.imshow('Cookie Cutter', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
cv2.waitKey(1)

while True:
    cv2.imshow('Cookie Cutter', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
gameOver = False
NotWon = True
#GAME LOGIC UPTO THE TEAMS
#-----------------------------------------------------------------------------------------
while not gameOver:
        continue
#LOSS SCREEN

if NotWon:
    for i in range(10):
        cv2.imshow('Cookie Cutter', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))
   
    while True:
        cv2.imshow('Cookie Cutter', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break

else:
    
    cv2.imshow('Cookie Cutter', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
    cv2.waitKey(125)

#show the win screen from the winner image read before

    while True:
        #show the win screen from the winner image read before and end it after we press q
        cv2.imshow('Cookie Cutter', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break

cv2.destroyAllWindows()