#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Distributed under terms of the MIT license.

import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import os, os.path


face_cascades = [cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml'),
                             cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt2.xml'),cv2.CascadeClassifier('haarcascade/sideface.xml')]
    
eye_cascades = [cv2.CascadeClassifier('haarcascade/haarcascade_smile.xml'),cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml'),cv2.CascadeClassifier('haarcascade/haarcascade_lefteye_2splits.xml')]

path = "./input"
valid_images = [".jpg",".gif",".png",".tga",".jpeg"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue

    img = cv2.imread(os.path.join(path,f))
    img = cv2.resize(img, (1000,600))  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    for face_cascade in face_cascades:  
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)


        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

            
#            roi_gray = gray[y:y+h, x:x+w]
#            roi_color = img[y:y+h, x:x+w]
            
#            for eye_cascade in eye_cascades:
#                eyes = eye_cascade.detectMultiScale(roi_gray)
#                for (ex,ey,ew,eh) in eyes:
#                   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

     
    
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.imshow('img',img)
    cv2.waitKey(0)

cv2.destroyAllWindows();
