import base64
import requests
from copy import deepcopy
import cvut.time as cvuttime
from face_list import face_list1, face_list2
import pytest

URL_FR = "http://10.0.8.121:8004/face_registration"

# Function to encode an image to base64
def encodeToBase64Img(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def test_registration_multiple_faces():
    # Initialize an empty list to store the registered face IDs
    face_ids = []

    # Iterate over the image paths and register each face with OpCode=0 and FaceID=-1
    for i, image_path in enumerate(face_list1):
        person = encodeToBase64Img(image_path)
        data = {
            "TimeSend": cvuttime.get_time_now("%Y-%m-%dT%H:%M:%S.%f"),
            "Item": {
                "ImageData": person,
                "FaceID": -1,
                "OpCode": 0
            }
        }
        response = requests.post(URL_FR, json=data)
        response_data = response.json()

        assert "success" in response_data["Message"].lower()
        assert response_data["StatusCode"] == 1
        assert response_data["FaceID"] == i

        # Store the registered face ID in the list
        face_ids.append(response_data["FaceID"])

def test_update_multiple_faces():
    # Initialize an empty list to store the registered face IDs
    face_ids = []

    # Iterate over the image paths and register each face with OpCode=0 and FaceID=-1
    for i, image_path in enumerate(face_list2):
        person = encodeToBase64Img(image_path)
        data = {
            "TimeSend": cvuttime.get_time_now("%Y-%m-%dT%H:%M:%S.%f"),
            "Item": {
                "ImageData": person,
                "FaceID": i,
                "OpCode": 1
            }
        }
        response = requests.post(URL_FR, json=data)
        response_data = response.json()

        assert "success" in response_data["Message"].lower()
        assert response_data["StatusCode"] == 1
        assert response_data["FaceID"] == i

        # Store the registered face ID in the list
        face_ids.append(response_data["FaceID"])

def test_delete_multiple_faces():
    # Initialize an empty list to store the deleted face IDs
    deleted_face_ids = []

    # Iterate over the face IDs and delete each face with OpCode=2 and FaceID=-1
    for i in range(len(face_list1)):
        data = {
            "TimeSend": cvuttime.get_time_now("%Y-%m-%dT%H:%M:%S.%f"),
            "Item": {
                "ImageData": None,
                "FaceID": i,
                "OpCode": 2
            }
        }
        response = requests.post(URL_FR, json=data)
        response_data = response.json()

        assert "success" in response_data["Message"].lower()
        assert response_data["StatusCode"] == 1
        assert response_data["FaceID"] == i

        # Store the deleted face ID in the list
        deleted_face_ids.append(i)

    # Verify that all the face IDs have been deleted
    assert set(deleted_face_ids) == set(range(len(face_list1)))


