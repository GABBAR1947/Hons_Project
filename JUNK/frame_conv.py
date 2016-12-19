#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Distributed under terms of the MIT license.

import cv2
import numpy as np
cap = cv2.VideoCapture('./comic2.mp4')
success,image = cap.read();

count = 0
s =  True
while s:
    s,image = cap.read()
    print' read a new frame',s
      
    cv2.imwrite("frame%d.jpg"%count,image)
    count+=1;
