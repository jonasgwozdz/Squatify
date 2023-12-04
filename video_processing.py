# video_processing.py

import os
import cv2
import mediapipe as mp
import numpy as np
import pandas as pd

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def process_video(video_file, video_dir):
    video_path = os.path.join(video_dir, video_file)
    cap = cv2.VideoCapture(video_path)

    pose_data = []

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark
                pose_data.append([landmark.x for landmark in landmarks])
                pose_data.append([landmark.y for landmark in landmarks])
                pose_data.append([landmark.z for landmark in landmarks])
            except:
                pass

    cap.release()

    pose_df = pd.DataFrame(pose_data)
    tracking_data_dir = 'tracking_data'
    if not os.path.exists(tracking_data_dir):
        os.makedirs(tracking_data_dir)
    pose_df.to_csv(os.path.join(tracking_data_dir, f'Tracking{video_file[5:-4]}.csv'), index=False)