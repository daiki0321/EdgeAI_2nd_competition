#import libraries
import os
import json
import numpy as np
import cv2

#define paths
path_labels    = '/home/guest/work/akasaka/signate2/train_annotations'      
path_images    = '/home/guest/work/train_data/signate2/20200613/images/train_imgs_equalizeHist' #path where, the are the decoded train images
input_file  = 'data_for_yolo_training_416_416.txt'
output_file  = '/home/guest/work/train_data/signate2/20200613/data_for_yolo_signate2.txt'

os.makedirs(path_images, exist_ok=True)

image_list    = open(input_file, "r")
out_file    = open(output_file, "a")
image = image_list.readline()

count = 0

a = 10
c_table = np.array([255.0 / (1 + np.exp(-a * (i - 128) / 255)) for i in np.arange(0, 256)]).astype("uint8")

while image:

    str_to_write = image.split(' ')
    print(str_to_write[0])
    old_img = cv2.imread(str_to_write[0])

    #gamma = 0.5
    #gamma_cvt = np.zeros((256,1),dtype = 'uint8')
    #for i in range(256):
    #    gamma_cvt[i][0] = 255 * (float(i)/255) ** (1.0/gamma)

    #gamma = 1 / np.sqrt(old_img.mean()) * 13
    #g_table = np.array([((i / 255.0) ** (1 / gamma)) * 255 for i in np.arange(0, 256)]).astype("uint8")

    #img_yuv = cv2.cvtColor(old_img, cv2.COLOR_RGB2YUV)
    #img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    #img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
    
    #ksize=3
    #img = cv2.medianBlur(old_img,ksize)
    
    #img_gamma = cv2.LUT(old_img, gamma_cvt)
    #img = cv2.LUT(img_gamma, c_table)

    R, G, B = cv2.split(old_img)

    output1_R = cv2.equalizeHist(R)
    output1_G = cv2.equalizeHist(G)
    output1_B = cv2.equalizeHist(B)

    img = cv2.merge((output1_R, output1_G, output1_B))

    cv2.imwrite(os.path.join(path_images, str('{:05d}'.format(count))+".jpg"), img)

    str_to_write[0] = os.path.join(path_images, str('{:05d}'.format(count))+".jpg")
    #print(' '.join(str_to_write))
    out_file.write(' '.join(str_to_write))
    count += 1

    image = image_list.readline()

image_list.close()
out_file.close()

