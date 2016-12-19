#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright © 2016 gabbar1947 <gabbar1947@Rathores-MacBook-Pro.local>
# Distributed under terms of the MIT license.

"""
This file contains all the headers to be included in all the files 

"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import os, os.path

recognizer = cv2.createLBPHFaceRecognizer()

face_cascades = [cv2.CascadeClassifier('haarcascade/sideface.xml'),
                 cv2.CascadeClassifier('haarcascade/haarcascade_profileface.xml'),
                 cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt.xml'),
                 cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt2.xml'),
                 cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt_tree.xml'),
                 cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')]
    
eye_cascades = [cv2.CascadeClassifier('haarcascade/haarcascade_smile.xml'),
                cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml'), 
                cv2.CascadeClassifier('haarcascade/haarcascade_lefteye_2splits.xml')]

mouth_cascades = [cv2.CascadeClassifier('haarcascade/Mouth.xml')]

NAMES = { 999:'Aayush' , 998:'Dhruv' , 997:'Jerin' , 996:'Shubham' , 995:'Allen' , 994:'Jaipal', 993:'Mahtab', 992:'Siddhartha'}
