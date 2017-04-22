import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('facehaar.xml')

vid = cv2.VideoCapture(0);

while True:
    ret, img = vid.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("detection",img)
    d = cv2.waitKey(30) & 0xff
    if d ==27:
        break;
        cv2.imshow("detection",img)

img.release()
cv2.destroyAllWindows()
    
