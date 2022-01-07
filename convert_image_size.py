#import libraries
import os
import json
import numpy as np
import cv2

#define paths
path_labels    = '/home/guest/work/akasaka/signate2/train_annotations'      
path_images    = '/home/guest/work/train_data/signate2/20200613/images/train_imgs_416_416' #path where, the are the decoded train images
input_file  = 'data_for_yolo_training_416_416.txt'
output_file  = '/home/guest/work/train_data/signate2/20200613/data_for_yolo_signate2.txt'

os.makedirs(path_images, exist_ok=True)

image_list    = open(input_file, "r")
out_file    = open(output_file, "w")
image = image_list.readline()

count = 0

while image:

    str_to_write = image.split(' ')
    print(str_to_write[0])
    img = cv2.imread(str_to_write[0])

    cv2.imwrite(os.path.join(path_images, str('{:05d}'.format(count))+".jpg"), img)

    str_to_write[0] = os.path.join(path_images, str('{:05d}'.format(count))+".jpg")
    #print(' '.join(str_to_write))
    out_file.write(' '.join(str_to_write))
    count += 1

    image = image_list.readline()

image_list.close()
out_file.close()

