#import libraries
import os
import json

#define paths
path_labels    = '/home/guest/work/akasaka/signate2/train_annotations'      
path_images    = '/home/guest/work/akasaka/signate2/train_imgs_416_416' #path where, the are the decoded train images
path_out_file  = 'data_for_yolo_training_416_416_coco.txt'

#array that defines which classes have to be extracted. 
classes = ['Car', 'Pedestrian', 'Truck', 'Signal', 'Signs', 'Bicycle', 'Motorbike', 'Bus', 'Svehicle', 'Train']

def convert_to_coco_label(sigante_data):

    coco_dict = {'Car' : 2, 'Pedestrian' : 0, 'Truck' : 7, 'Signal' : 9, 'Signs' : 11, 'Bicycle' : 1, 'Motorbike' : 3, 'Bus' : 5, 'Svehicle' : 2, 'Train' : 6}

    #print(f'{sigante_data} => {coco_dict[sigante_data]}')

    return coco_dict[sigante_data]

out_file    = open(path_out_file, "w")
annotations = os.listdir(path_labels)

for i in range (0, len(annotations)):#here we browse all videos
    video_name = annotations[i].split('/')[-1].split('\\')[-1].split('.')[0]
    data       = json.load(open(os.path.join(path_labels, annotations[i])))
    
    for v in range (0,600): #here we browse all frames. Single movie has 600 frames
        img_name     = path_images+'/'+video_name+'/'+str(v)+".jpg"
        labels       = data['sequence'][v]
        str_to_write = img_name
        for c in range (0, len(classes)):
            try:
                for inst in data['sequence'][v][classes[c]]:
                    box           = inst['box2d']
                    if (int(box[0]*416/1936) != int(box[2]*416/1936)) and (int(box[1]*416/1216) != int(box[3]*416/1216)):
                        str_to_write += ' '+str(int(box[0]*416/1936))+','+str(int(box[1]*416/1216))+','+str(int(box[2]*416/1936))+','+str(int(box[3]*416/1216))+','+str(convert_to_coco_label(classes[c]))
                    #str_to_write += ' '+str(int(box[0]))+','+str(int(box[1]))+','+str(int(box[2]))+','+str(int(box[3]))+','+str(c)
            except:
                continue #nothing, the class is just not presented in the frame

            print(str_to_write)
         
        if str_to_write != img_name: #we do not want to write images without annotations2
            out_file.write(str_to_write+'\n')
        
out_file.close() 
