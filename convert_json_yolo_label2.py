#import libraries
import os
import sys
import cv2

if len(os.sys.argv) != 2:
    print("Need to set keras-yolo anotattion file\n")
    quit()

data_filename = os.sys.argv[1]

train_text = os.path.dirname(data_filename)+'/'+'train.txt'
valid_text = os.path.dirname(data_filename)+'/'+'valid.txt'

train_list_file    = open(train_text, "w")
valid_list_file    = open(valid_text, "w")

with open(data_filename, "r") as f:

    count = 0

    for read_data in f:
        print(read_data.split(' ')[0])
        
        img_name = read_data.split(' ')[0]
        if count % 10 :
            train_list_file.write(img_name+'\n')
        else :
            valid_list_file.write(img_name+'\n')

        annotations = read_data.split(' ')[1:]

        img = cv2.imread(img_name)
        #print(img.shape)
        height, width, channel = img.shape

        str_to_write = ""
        for i in range (0, len(annotations)):#here we browse all videos
            
            #print(annotations[i])
            box = annotations[i].split(',')[0:4]
            x1 = int(box[0]) / width
            y1 = int(box[1]) / height
            x2 = int(box[2]) / width
            y2 = int(box[3]) / height
            #print(box)
            classes = annotations[i].split(',')[4].replace("\n", "")

            str_to_write += str(classes)+' '+str('{:1.6f}'.format((x1 + x2)/2))+' '+str('{:1.6f}'.format((y1 + y2)/2))+' '+str('{:1.6f}'.format(x2 - x1))+' '+str('{:1.6f}'.format(y2 - y1))+'\n'

        path_out_file=img_name.replace("/images/", "/labels/").replace(".jpg", ".txt")

        os.makedirs(os.path.dirname(path_out_file), exist_ok=True)

        with open(path_out_file, "w") as out_file:
            #print(path_out_file)
            #print(str_to_write)
            out_file.write(str_to_write)
    
        count += 1
        
train_list_file.close()
valid_list_file.close()

