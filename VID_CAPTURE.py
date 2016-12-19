#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Distributed under terms of the MIT license.

"""
This file was used to accumulate the training set of images

"""
from VID_HEAD import *


dirname = 'VID_DATASET/RAND'
#dirname = os.path.join(dirname,folder);
cap = cv2.VideoCapture(0)
count = 1
while 1:

    ret, img = cap.read()
    img = cv2.resize(img, (1000,600))  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    for face_cascade in face_cascades:  
        faces = face_cascade.detectMultiScale(gray, 1.3, 1)


        for (x,y,w,h) in faces:
            temp = img[y:y+h , x:x+w]

            if(len(temp)>0):
                cv2.imwrite(os.path.join(dirname,"jaipal%d.jpg"%count),temp)
                
                count = count + 1
            
#            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
            lips = mouth_cascades.detectMultiScale(roi_gray)
            
            for (mx,my,mw,mh) in lips:
                func()#for every mouth; return the maximum variation

 #           for eye_cascade in eye_cascades:
 #               eyes = eye_cascade.detectMultiScale(roi_gray)
 #               for (ex,ey,ew,eh) in eyes:
 #                   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows();
