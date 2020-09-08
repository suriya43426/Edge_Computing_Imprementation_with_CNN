import face_recognition
import cv2
from datetime import datetime, timedelta
import numpy as np
import platform
import pickle

known_face_encodings = []
known_face_metadata = []

def save_known_faces():
    with open("known_faces.dat", "wb") as face_data_file:
        face_data = [known_face_encodings, known_face_metadata]
        pickle.dump(face_data, face_data_file)
        print("Known faces backed up to disk.")


def running_on_jetson_nano():
    return platform.machine() == "aarch64"

def register_new_face(face_encoding, face_image):
    known_face_encodings.append(face_encoding)
    known_face_metadata.append({
        "first_seen": datetime.now(),
        "first_seen_this_interaction": datetime.now(),
        "last_seen": datetime.now(),
        "seen_count": 1,
        "seen_frames": 1,
        "face_image": face_image,
    })

def lookup_known_face(face_encoding):
    metadata = None

    if len(known_face_encodings) == 0:
        return metadata

    face_distances = face_recognition.face_distance(
        known_face_encodings, 
        face_encoding
    )

    best_match_index = np.argmin(face_distances)

    if face_distances[best_match_index] < 0.65:
        metadata = known_face_metadata[best_match_index]
        metadata["last_seen"] = datetime.now()
        metadata["seen_frames"] += 1

        if datetime.now() - metadata["first_seen_this_interaction"]  
                > timedelta(minutes=5):
            metadata["first_seen_this_interaction"] = datetime.now()
            metadata["seen_count"] += 1

    return metadata

def main_loop():
    if running_on_jetson_nano():
        video_capture = 
            cv2.VideoCapture(
                get_jetson_gstreamer_source(), 
                cv2.CAP_GSTREAMER
            )
    else:
        video_capture = cv2.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color
    rgb_small_frame = small_frame[:, :, ::-1]

face_locations = face_recognition.face_locations(rgb_small_frame)
face_encodings = face_recognition.face_encodings(
                     rgb_small_frame, 
                     face_locations
                  )

for face_location, face_encoding in zip(
                       face_locations, 
                       face_encodings):
    metadata = lookup_known_face(face_encoding)

    if metadata is not None:
        time_at_door = datetime.now() - 
            metadata['first_seen_this_interaction']
        face_label = f"At door {int(time_at_door.total_seconds())}s"

    else:
        face_label = "New visitor!"

        # Grab the image of the the face
        top, right, bottom, left = face_location
        face_image = small_frame[top:bottom, left:right]
        face_image = cv2.resize(face_image, (150, 150))

        # Add the new face to our known face data
        register_new_face(face_encoding, face_image)

for (top, right, bottom, left), face_label in 
                  zip(face_locations, face_labels):
    # Scale back up face location
    # since the frame we detected in was 1/4 size
    top *= 4
    right *= 4
    bottom *= 4
    left *= 4

    # Draw a box around the face
    cv2.rectangle(
        frame, (left, top), (right, bottom), (0, 0, 255), 2
    )

    # Draw a label with a description below the face
    cv2.rectangle(
        frame, (left, bottom - 35), (right, bottom), 
        (0, 0, 255), cv2.FILLED
    )
    cv2.putText(
        frame, face_label, 
        (left + 6, bottom - 6), 
        cv2.FONT_HERSHEY_DUPLEX, 0.8, 
        (255, 255, 255), 1
    )

number_of_recent_visitors = 0
for metadata in known_face_metadata:
    # If we have seen this person in the last minute
    if datetime.now() - metadata["last_seen"] 
                         < timedelta(seconds=10):
        # Draw the known face image
        x_position = number_of_recent_visitors * 150
        frame[30:180, x_position:x_position + 150] =
              metadata["face_image"]
        number_of_recent_visitors += 1

        # Label the image with how many times they have visited
        visits = metadata['seen_count']
        visit_label = f"{visits} visits"
        if visits == 1:
            visit_label = "First visit"
        cv2.putText(
            frame, visit_label, 
            (x_position + 10, 170), 
            cv2.FONT_HERSHEY_DUPLEX, 0.6, 
            (255, 255, 255), 1
        )

cv2.imshow('Video', frame)

if len(face_locations) > 0 and number_of_frames_since_save > 100:
    save_known_faces()
    number_of_faces_since_save = 0
else:
    number_of_faces_since_save += 1

https://github.com/ageitgey/face_recognition
