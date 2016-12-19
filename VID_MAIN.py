#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright © 2016 gabbar1947 <gabbar1947@Rathores-MacBook-Pro.local>
# Distributed under terms of the MIT license.

"""
The actual control lies in this code
"""

from VID_TRAIN import *
from VID_TEST import *

def main():
    

    #preparing the dataset/ labels / images
    path = 'VID_DATASET'
    IMAGES, LABELS = create_train(path)

    for i in range(len(IMAGES)):
        IMAGES[i] = cv2.cvtColor(IMAGES[i], cv2.COLOR_BGR2GRAY)

    LABELS = map(int,LABELS)
    cv2.destroyAllWindows()
    recognizer.train(IMAGES, np.array(LABELS))
    
    create_test()

main()
