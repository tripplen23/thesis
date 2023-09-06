import cv2
import numpy as np
from imutils.video import VideoStream
from yolodetect import YoloDetect
import asyncio

# Constants and Parameters
VIDEO_SOURCE = 0
RESIZE_SCALE = 0.5  # Adjust as needed
POLY_COLOR = (255, 0, 0)  # Red
CIRCLE_COLOR = (0, 0, 255)  # Blue

# Initialize video stream and YoloDetect
video = VideoStream(src=VIDEO_SOURCE).start()
points = []  # Initialize polygon points
model = YoloDetect(detect_class="person")

"""Callback for left mouse click"""


def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])


"""Handle Drawing Polygon Area or Warning Area"""


def draw_polygon(frame, points):
    for point in points:
        frame = cv2.circle(frame, (point[0], point[1]), 5, CIRCLE_COLOR, -1)

    frame = cv2.polylines(frame, [np.int32(points)],
                          False, POLY_COLOR, thickness=2)
    return frame


"""Resize the frame"""


def rescaleFrame(frame, scale=2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)


"""Main Logic"""


async def main():
    detect = False

    while True:
        frame = video.read()
        # flip the frame as the webcam view is not the same direction as us.
        frame = cv2.flip(frame, 1)

        frame_resize = rescaleFrame(frame)

        # Drawing the polygon area
        frame_resize = draw_polygon(frame_resize, points)

        if detect:
            frame_resize = await model.detect(frame=frame_resize, points=points)

        key = cv2.waitKey(1) & 0xFF
        # Press 'q' key to exit the video loop
        if key == ord('q'):
            break
        # Press 'd' key to detect the final polygon point
        elif key == ord('d'):
            points.append(points[0])
            detect = True

        # Display to the screen
        cv2.imshow("Intrusion Warning", frame_resize)

        cv2.setMouseCallback('Intrusion Warning', handle_left_click, points)

    # Stop the video stream and close all windows
    video.stop()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    asyncio.run(main())
