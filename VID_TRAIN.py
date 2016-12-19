#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Distributed under terms of the MIT license.

"""
This code is responsible for the creation of a dataset

"""

from VID_HEAD import *

#face_cascades
def create_train(path):

    path_folder = [os.path.join(path,i) for i in os.listdir(path)]
    
    train_images = []
    label_images = []
    
    for folder in path_folder:
    
        path_image = [os.path.join(folder,i) for i in os.listdir(folder)]
        for temp_path in path_image:
            
            image = cv2.imread(temp_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            temp_label = os.path.split(temp_path)[1].split(".")[0]
                    
        
            #rem = 0;
            #for i in range(len(temp_label)):
            #    if ord(temp_label[i]) >=48 and ord(temp_label[i]) <=57:
            #        rem = i
            #        break

            temp_label = temp_label[:3]

            train_images.append(image)
            label_images.append(temp_label)
            

    return train_images,label_images
