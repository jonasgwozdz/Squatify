# video_processing.py
import logging
import os
import cv2
import mediapipe as mp
import pandas as pd


# Set up logging
logging.basicConfig(level=logging.INFO)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Define the body parts
body_parts = ['Nose', 'Left eye inner', 'Left eye', 'Left eye outer', 'Right eye inner', 'Right eye', 'Right eye outer', 'Left ear', 'Right ear', 'Mouth left', 'Mouth right', 'Left shoulder', 'Right shoulder', 'Left elbow', 'Right elbow', 'Left wrist', 'Right wrist', 'Left pinky', 'Right pinky', 'Left index', 'Right index', 'Left thumb', 'Right thumb', 'Left hip', 'Right hip', 'Left knee', 'Right knee', 'Left ankle', 'Right ankle', 'Left heel', 'Right heel', 'Left foot index', 'Right foot index']

def process_video(video_file, video_dir):
    logging.info(f'Processing video: {video_file}')
    video_path = os.path.join(video_dir, video_file)
    cap = cv2.VideoCapture(video_path)

    pose_data = []

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        frame_number = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            frame_data = {'Label': '', 'Timestamp': frame_number}
            try:
                landmarks = results.pose_landmarks.landmark
                for i, landmark in enumerate(landmarks):
                    frame_data[f'{body_parts[i]}_x'] = landmark.x
                    frame_data[f'{body_parts[i]}_y'] = landmark.y
                    frame_data[f'{body_parts[i]}_z'] = landmark.z
            except:
                pass

            pose_data.append(frame_data)
            frame_number += 1

    cap.release()

    pose_df = pd.DataFrame(pose_data)
    tracking_data_dir = 'tracking_data'
    if not os.path.exists(tracking_data_dir):
        os.makedirs(tracking_data_dir)
    csv_file = os.path.join(tracking_data_dir, f'Tracking_{video_file[:-4]}.csv')
    pose_df.to_csv(csv_file, index=False)
    logging.info(f'Tracking data for {video_file} stored in {csv_file}')