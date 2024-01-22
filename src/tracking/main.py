# main.py
import os
import csv
from multiprocessing import Pool
from video_processing import process_video
from tqdm import tqdm

def rename_video(video_file, video_dir, new_name):
    # Rename the video file
    new_name_with_ext = new_name + '.mp4'
    os.rename(os.path.join(video_dir, video_file), os.path.join(video_dir, new_name_with_ext))

    # Return the old and new names
    return video_file, new_name_with_ext

if __name__ == '__main__':
    video_dir = '../../data/training/videos'
    video_files = [f for f in os.listdir(video_dir) if f.endswith('.mov') or f.endswith('.MOV') or f.endswith('.mp4')]

    with Pool() as p:
        # Rename the video files
        results = list(tqdm(p.starmap(rename_video, [(video_file, video_dir, f'video{index:02}') for index, video_file in enumerate(video_files, start=1)]), total=len(video_files)))

        # Save the old and new names of the video files in a CSV file in the video directory
        with open(os.path.join(video_dir, 'videofilenames.csv'), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Old Name', 'New Name'])
            writer.writerows(results)

        # Process the video files
        tqdm(p.starmap(process_video, [(result[1], video_dir) for result in results]), total=len(results))