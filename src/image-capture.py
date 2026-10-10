import cv2 as cv

# creates the webcam object
# the variable passed in tells where to look for input
webcam = cv.VideoCapture(1)
if (webcam.isOpened()):
    print("webcam is open")
else:
    print("couldn't get an input")

#zooms the webcam to resize to desired dimensions
def zoom(frame, zoom_factor):
    if(zoom_factor <= 1.0):
        return frame

    #get the width and height from the numpy array
    h, w = frame.shape[:2]

    zoom_w = int(w / zoom_factor)
    zoom_h = int(h / zoom_factor)

    #locate the dimensions for the cut out image
    center_x = int(w / 2)
    center_y = int(h / 2)
    left_x = int(center_x - (zoom_w / 2))
    top_y = int(center_y - (zoom_h / 2))
    right_x = int(center_x + (zoom_w / 2))
    bottom_y = int(center_y + (zoom_h / 2))

    #new cropped frame object with the cut out image from the original frame
    cropped_frame = frame[top_y:bottom_y, left_x:right_x]
    return cv.resize(cropped_frame, (w, h))

#webcam.read returns a tuple [boolean: if the frame was read, numpy array: data of the image]
webcam_read = webcam.read()
#how zoomed in the webcam is
zoom_factor = 2.0
#loop to output a video of the webcam
while(webcam_read[0]):
    #resizes the webcam
    zoomed_webcam = zoom(webcam_read[1], zoom_factor)
    # displays a window with the webcam output
    display = cv.imshow("webcam feed", zoomed_webcam)
    # allows the frame to refresh and terminate program
    key = cv.waitKey(1)
    if (key == -1):
        webcam_read = webcam.read()
    else:
        webcam.release()
        cv.destroyAllWindows()