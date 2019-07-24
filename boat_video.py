import cv2
import os
import numpy as np


def label(img,txt):
    with open(txt,"r") as f:
        str = f.read()
        list = str.split(" ")
    name = list[0]
    xmin = int(list[4])
    ymin = int(list[5])
    xmax = int(list[6])
    ymax = int(list[7])
    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)
    cv2.putText(img, name, (xmin, ymin), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),1)
    return img


fps = 10
size = (1920, 1080)
name = "boat"
videowriter = cv2.VideoWriter(str(name) + ".avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
path1 = r'dataset/image_2/'
path2 = r'dataset/label_2/'
list1 = np.sort(os.listdir(path1))
list2 = np.sort(os.listdir(path2))
for i in range(len(list1)):
    img = cv2.imread(path1+list1[i])
    new_img = label(img,(path2+list2[i]))
    result = cv2.resize(new_img,(1920,1080))
    videowriter.write(result)
videowriter.release()
