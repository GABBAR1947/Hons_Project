#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from PIL import Image
import os, os.path
import cv2

imgs = []
path = "./input"
valid_images = [".jpg",".gif",".png",".tga",".jpeg"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(Image.open(os.path.join(path,f)));

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow('img',imgs[1])
cv2.waitKey(0)

