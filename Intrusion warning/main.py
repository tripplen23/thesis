import cv2
import numpy as np
from imutils.video import VideoStream
from yolodetect import YoloDetect

video = VideoStream(src=0).start()

# points is an array of points where user use them to create a polygon area.
points = []

# new model Yolo
model = YoloDetect(detect_class="person")


def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])


def draw_polygon(frame, points):
    for point in points:
        frame = cv2.circle(frame, (point[0], point[1]), 5, (0, 0, 255), -1)

    frame = cv2.polylines(frame, [np.int32(points)],
                          False, (255, 0, 0), thickness=2)
    return frame


detect = False

while True:
    frame = video.read()
    # flip the frame as the webcam view is not the same direction as us.
    frame = cv2.flip(frame, 1)

    # Drawing the polygon area
    frame = draw_polygon(frame, points)

    if detect:
        frame = model.detect(frame=frame, points=points)

    key = cv2.waitKey(1) & 0xFF
    # Press 'q' key to exit the video loop
    if key == ord('q'):
        break
    # Press 'd' key to detect the final polygon point
    elif key == ord('d'):
        points.append(points[0])
        detect = True

    # Display to the screen
    cv2.imshow("Intrusion Warning", frame)

    cv2.setMouseCallback('Intrusion Warning', handle_left_click, points)

# Stop the video stream and close all windows
video.stop()
cv2.destroyAllWindows()
