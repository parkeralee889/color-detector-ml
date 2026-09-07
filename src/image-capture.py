import cv2 as cv

# create the webcam object
# the variable passed in tells where to look for input
webcam = cv.VideoCapture(0)
if (webcam.isOpened()):
    print("webcam is open")
else:
    print("couldn't get an input")



webcam_read = webcam.read()
while(webcam_read[0]):
    # displays a window with the webcam output
    display = cv.imshow("webcam feed", webcam_read[1])