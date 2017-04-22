import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('myhaarc.xml')

img = cv2.imread('corals.jpg');
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)  
cv2.imwrite('563.jpg',img)
cv2.waitKey(0)
