#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Distributed under terms of the MIT license.

import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import os, os.path


face_cascades = [cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt.xml'),
                             cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt2.xml'),cv2.CascadeClassifier('haarcascade/sideface.xml')]
    
eye_cascades = [cv2.CascadeClassifier('haarcascade/haarcascade_smile.xml'),cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml'),cv2.CascadeClassifier('haarcascade/haarcascade_lefteye_2splits.xml')]

cap = cv2.VideoCapture('comic2.mp4');
while 1:

    ret, img = cap.read()
    img = cv2.resize(img, (1000,600))  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    for face_cascade in face_cascades:  
        faces = face_cascade.detectMultiScale(gray, 1.3, 1)


        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
            for eye_cascade in eye_cascades:
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows();
