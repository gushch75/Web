
import cv2
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
#img = cv2.imread('face.jpg')
#img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#faces = face_cascades.detectMultiScale(img_grey)

#print(faces)

#for ( x,y,w,h) in faces:
 #   cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


#cv2.imshow('Result',img)
#cv2.waitKey(1000)


cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    cv2.imshow('camera',frame)
    img_grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(img_grey)
    for ( x,y,w,h) in faces:
     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)  

    cv2.imshow('Result',frame)
    if cv2.waitKey(1) & 0xff == ord ('q'):
       break 

    
