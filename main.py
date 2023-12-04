# main.py

import os
from multiprocessing import Pool
from video_processing import process_video

if __name__ == '__main__':
    video_dir = 'Videos'
    video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]

    with Pool() as p:
        p.starmap(process_video, [(video_file, video_dir) for video_file in video_files])