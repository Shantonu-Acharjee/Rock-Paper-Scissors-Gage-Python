import cv2
import mediapipe as mp
import time
import os
from random import randint


a = ['Rock', 'Paper', 'Seissors'] 


cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
fingerCoordinates = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumCoordinates = (4, 2)



folderPath = 'Photos'
myList = os.listdir(folderPath)
print(myList)


overlayList = []
for imPath in myList:
    
    image = cv2.imread(f'{folderPath}/{imPath}')

    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

#print(len(overlayList))








def you(UserInput):
    print('You Enter ', a[UserInput - 1])



    RandomNumber = randint(1,3)
    RandomNumber = RandomNumber - 1


    if UserInput == UserInput:
        #print('Random Number is : ', RandomNumber)

        if RandomNumber == 0:
            computer =  a[RandomNumber]
            print('Computer : ', computer)
            

        elif RandomNumber == 1:
            computer =  a[RandomNumber]
            print('Computer : ', computer)
            

        elif RandomNumber == 2:
            computer =  a[RandomNumber]
            print('Computer : ', computer)
            


    if RandomNumber == 0: # rock
        
        if UserInput-1 == 0:
            print('Drow') 
        

        elif UserInput-1 == 1:
            print('You Win')

        elif UserInput-1 == 2:
            print('Computer Win')



    elif RandomNumber == 1: # paper
        
        if UserInput-1 == 0:
            print('Computer win') 
        

        elif UserInput-1 == 1:
            print('Drow')

        elif UserInput-1 == 2:
            print('You Win')




    elif RandomNumber == 2: # Seissors
        
        if UserInput-1 == 0:
            print('You Win') 
        

        elif UserInput-1 == 1:
            print('Computer Win')

        elif UserInput-1 == 2:
            print('Drow')









pTime = 0
while True:
    Success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    multiLandMarks = results.multi_hand_landmarks
    #print(multiLandMarks)


    if multiLandMarks:
        handPoints = []
        for handLms in multiLandMarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            for idx, lm in enumerate(handLms.landmark):
                # print(idx, lm)
                h,w,c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(idx, cx, cy)
                handPoints.append((cx, cy))


        for point in handPoints:
            # print(point)
            cv2.circle(img, point, 7, (0, 0, 255), cv2.FILLED)


        upCount = 0
        for coordinate in fingerCoordinates:
            (8, 6)
            if handPoints[coordinate[0]][1] < handPoints[coordinate[1]][1]:
                upCount += 1

        if handPoints[thumCoordinates[0]][0] > handPoints[thumCoordinates[1]][0]:
            upCount += 1

        cv2.putText(img, str(upCount), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        h,w,c = overlayList[0].shape
        #img[260:h+260, 240:w+240] = overlayList[upCount]-----------------------------
        print(upCount)



        
        
        if upCount == 0:
            you(1)
            

        elif upCount == 5 :
            you(2)
            


        elif upCount == 2 :
            you(3)
           






    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (420, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    # print(Success)
    cv2.imshow('Finger Counter', img)
    k = cv2.waitKey(1)

    if k == ord('q') or k == ord('Q'):
        break


