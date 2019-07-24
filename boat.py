import cv2
with open("boat7_0927.txt","r") as f:
    str = f.read()
    list = str.split(" ")
name = list[0]
xmin = int(list[4])
ymin = int(list[5])
xmax = int(list[6])
ymax = int(list[7])
img = cv2.imread("boat7_0927.jpg")
cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)
cv2.putText(img, name, (xmin, ymin), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),1)
cv2.imshow("img",img)
cv2.waitKey(0)
