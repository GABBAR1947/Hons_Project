#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright © 2016 gabbar1947 <gabbar1947@Rathores-MacBook-Pro.local>
# Distributed under terms of the MIT license.

"""
This code is for Testing Purposes

"""

from VID_HEAD import *

def create_test():

    cap = cv2.VideoCapture(0)
    
    while 1:
        ret, img = cap.read()
        img = cv2.resize(img, (1000,600))  
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        for face_cascade in face_cascades:  
            faces = face_cascade.detectMultiScale(gray, 1.3, 1)
            
            if len(faces) == 0:
                continue

            for (x,y,w,h) in faces:
                label_predicted, conf = recognizer.predict(gray[y: y + h, x: x + w]) 
                print NAMES[int(label_predicted)]

        
        cv2.imshow('img',img)
        k = cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows();
       

