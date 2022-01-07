import os
import sys

classes = ['Car', 'Pedestrian', 'Truck', 'Signal', 'Signs', 'Bicycle', 'Motorbike', 'Bus', 'Svehicle', 'Train']

if len(sys.argv) != 3:
    print("Error argument is not enough")

input_filename = sys.argv[1]
output_filename = sys.argv[2]

output_string_target = ""
output_string_validate = ""

with open(input_filename, "r") as f:

    count = 0

    for read_data in f:
        read_data = read_data.split(" ")
        file_name = read_data[0]

        if len(read_data[1:]) == 0:
            output_string += file_name+",,,,,"

        for i in range (1, len(read_data[1:])):
            x1,y1,x2,y2,class_num = read_data[i].split(",")
            #print(f'{file_name} {x1} {y1} {x2} {y2} {class_num}')
            #print(classes[int(class_num)])
            if ((int(x2) - int(x1)) * (int(y2) - int(y1))) > (1024/416):
                if count % 10 != 0:
                    output_string_target += file_name+","+x1+","+y1+","+x2+","+y2+","+classes[int(class_num)]+"\n"
                else:
                    output_string_validate += file_name+","+x1+","+y1+","+x2+","+y2+","+classes[int(class_num)]+"\n"
        
        count += 1

with open(output_filename, "w") as output_file:
    output_file.write(output_string_target)

with open(output_filename.split(".")[0]+"_val"+"."+output_filename.split(".")[1], "w") as output_file:
    output_file.write(output_string_validate)
