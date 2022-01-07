#import libraries
import os
import json

#define paths
path_labels    = '/home/guest/work/akasaka/signate2/train_annotations'      
path_images    = '/home/guest/work/akasaka/signate2/train_imgs' #path where, the are the decoded train images
path_out_file  = 'data_for_yolo_training.txt'

#array that defines which classes have to be extracted. 
classes = ['Car', 'Pedestrian', 'Truck', 'Signal', 'Signs', 'Bicycle', 'Motorbike', 'Bus', 'Svehicle', 'Train']

out_file    = open(path_out_file, "w")
annotations = os.listdir(path_labels)

print(annotations)

for i in range (0, len(annotations)):#here we browse all videos
    video_name = annotations[i].split('/')[-1].split('\\')[-1].split('.')[0]
    data       = json.load(open(os.path.join(path_labels, annotations[i])))
    
    for v in range (0,600): #here we browse all frames. Single movie has 600 frames
        img_name     = path_images+'/'+video_name+'/'+str(v)+".png"
        labels       = data['sequence'][v]
        str_to_write = img_name
        for c in range (0, len(classes)):
            try:
                for inst in data['sequence'][v][classes[c]]:
                    box           = inst['box2d']
                    str_to_write += ' '+str(box[0])+','+str(box[1])+','+str(box[2])+','+str(box[3])+','+str(c)
                    #str_to_write += ' '+str(int(box[0]))+','+str(int(box[1]))+','+str(int(box[2]))+','+str(int(box[3]))+','+str(c)
            except:
                continue #nothing, the class is just not presented in the frame
         
        if str_to_write != img_name: #we do not want to write images without annotations2
            out_file.write(str_to_write+'\n')
        
out_file.close() 
