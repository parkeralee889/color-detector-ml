import cv2 as cv

webcam = cv.VideoCapture(0)
if (webcam.isOpened()):
    print("webcam is open")
else:
    print("couldn't get an input")