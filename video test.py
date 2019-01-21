import cv2
import time
import numpy as np


# Load in a video file, or access the camera use 'filename.mp4" for file, or a number for a camera
cap = cv2.VideoCapture('WIN_20190119_14_27_53_Pro.mp4')

#extract the first frame
ret, frame=cap.read()

# show the dimensions of the video
rows, cols, channels = frame.shape
print ("Video is:{0} Pixels Wide, {1} Pixels High, and {2} Channels".format(rows, cols, channels))

# Keep extracting frames in a loop until end of video or "q" is pressed.
while True:
    ret, frame=cap.read()
# convert the frame to greyscale as well
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # draw a 1 pixel thick red (but since it's grey it'll be black) circle of radius 220 in the center of the video
    cv2.circle(grey, (int(cols / 2), int(rows / 2)), 220, (0, 0, 255), 1)
    # draw a bullseye circle of 1 pixel thick, radius 4 in the center of the video feed
    cv2.circle(grey, (int(cols / 2), int(rows / 2)), 4, (0, 0, 255), 1)
    # draw a vision target left box
    lbpts = np.array([[451, 158], [488, 18], [541, 32], [502, 175]], np.int32)
    cv2.polylines(grey, [lbpts], True, (0, 0, 255), 1)
    # draw a vision target for the right box
    rbpts = np.array([[779, 175], [750, 32], [805, 18], [835, 160]], np.int32)
    cv2.polylines(grey, [rbpts], True, (0, 0, 255), 1)
# display both the color and grayscale
    cv2.imshow('frame', frame)
    cv2.imshow('gray', grey)
# quit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
# wait 30 sec, and then die
        time.sleep(30)
        break

cap.release()
cv2.destroyAllWindows()

