import cv2
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from telegram_utils import send_telegram
import datetime
from pygame import mixer
mixer.init()
sound = mixer.Sound("alarm_audio/alarm2.wav")


# Check if Centroid of human detect is inside the Polygon area


def isInside(points, centroid):
    polygon = Polygon(points)
    centroid = Point(centroid)
    print(polygon.contains(centroid))
    return polygon.contains(centroid)


class YoloDetect():
    def __init__(self, detect_class="person", frame_width=900, frame_height=1280):
        # Parameters
        self.classnames_file = "model/yolov3.txt"
        self.weights_file = "model/yolov3.weights"
        self.config_file = "model/yolov3.cfg"
        self.conf_threshold = 0.5
        self.nms_threshold = 0.4
        self.detect_class = detect_class
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.scale = 1 / 255
        self.model = cv2.dnn.readNet(self.weights_file, self.config_file)
        self.classes = None
        self.output_layers = None
        self.read_class_file()
        self.get_output_layers()
        self.last_alert = None
        self.alert_telegram_each = 15  # Each alert is sent in 15 seconds

    def read_class_file(self):
        with open(self.classnames_file, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]

    def get_output_layers(self):
        layer_names = self.model.getLayerNames()
        self.output_layers = [layer_names[i - 1]
                              for i in self.model.getUnconnectedOutLayers()]

    def draw_prediction(self, img, class_id, x, y, x_plus_w, y_plus_h, points):
        label = str(self.classes[class_id])
        color = (0, 255, 0)  # Green

        # Calculate the new coordinates for the top-left and bottom-right corners
        new_x = max(x, 0)
        new_y = max(y, 0)
        new_x_plus_w = min(x_plus_w, img.shape[1])
        new_y_plus_h = min(y_plus_h, img.shape[0])

        # Calculate the new bounding box width and height
        new_w = new_x_plus_w - new_x
        new_h = new_y_plus_h - new_y

        # Draw the bounding box and label
        cv2.rectangle(img, (new_x, new_y),
                      (new_x_plus_w, new_y_plus_h), color, 2)
        cv2.putText(img, label, (new_x, new_y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Calculate the centroid of the new bounding box
        centroid_x = new_x + (new_w // 2)
        centroid_y = new_y + (new_h // 2)
        centroid = (centroid_x, centroid_y)
        cv2.circle(img, centroid, 5, (color), -1)

        if isInside(points, centroid):
            img = self.alert(img)
            try:
                sound.play()
            except:  # isplaying = False
                pass
        return isInside(points, centroid)

    async def alert(self, img):
        cv2.putText(img, "ALARM!!!", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2)
        # Send alert message to Telegram
        if (self.last_alert is None) or (
            (datetime.datetime.utcnow() -
             self.last_alert).total_seconds() > self.alert_telegram_each
        ):
            self.last_alert = datetime.datetime.utcnow()
            cv2.imwrite("alert.png", cv2.resize(
                img, dsize=None, fx=0.2, fy=0.2))
            await send_telegram("Intrusion detected! Please take action.")
        return img

    async def detect(self, frame, points):
        blob = cv2.dnn.blobFromImage(
            frame, self.scale, (416, 416), (0, 0, 0), True, crop=False)
        self.model.setInput(blob)
        outs = self.model.forward(self.output_layers)

        # Filter objects in the frame
        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if (confidence >= self.conf_threshold) and (self.classes[class_id] == self.detect_class):
                    center_x = int(detection[0] * self.frame_width)
                    center_y = int(detection[1] * self.frame_height)
                    w = int(detection[2] * self.frame_width)
                    h = int(detection[3] * self.frame_height)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        indices = cv2.dnn.NMSBoxes(
            boxes, confidences, self.conf_threshold, self.nms_threshold)

        for i in indices:
            box = boxes[i]
            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]
            await self.alert(frame)
            self.draw_prediction(frame, class_ids[i], round(
                x), round(y), round(x + w), round(y + h), points)

        return frame
