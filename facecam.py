# Detects faces in a specific picture
import cv2

capture = cv2.VideoCapture(0) #0 means that the video is captures through webcam

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    _, img = capture.read()


    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #turns the image into a grey scale image

    faces = face.detectMultiScale(grey, 1.1, 1) #Last number is the number of people in the picture

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2) #(image object, starting point, ending point, color(BGR), size of line)

    cv2.imshow('img', img)
    f = cv2.waitKey(30) & 0xff

    if f==27:
        break

capture.release()

print("Done")