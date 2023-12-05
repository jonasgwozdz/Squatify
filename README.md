# Squatify

## Overview
Squatify is a tiny little tool designed for motion tracking and data logging during squats. It takes videos of people performing squats, tracks their motion, and exports this data into CSV files. This data is particularly useful for training neural networks in applications such as fitness coaching, physical therapy, and biomechanical analysis.

## Features
- **Video Processing**: Process videos to track squatting motion.
- **Motion Tracking**: Accurate tracking of key points during the squat.
- **Automatic Labeling**: Somewhat accurate labeling of the Squat motion.
- **Data Export**: Export motion data into well-structured CSV files.
- **Neural Network Training**: Data formatted for ease of use in training machine learning models.

## Getting Started
### Prerequisites
- Python 3.9.6
- Dependencies listed in `requirements.txt`

### Installation
Clone the repository, install the required packages, find some videos of someone squatting and run the main.py. it's that simple. You have to see it to believe it.

## Usage

Record or upload a squatting video, name it "VideoXX"( with a corresponding number) and put it into the Videos directory.
Run the motion tracking script: python main.py.
Collect the output CSV files from the designated output folder.

The 'labels_and_plots.ipynb' notebook is responsible for the automatic labeling of squat motion data. It utilizes state-of-the-art AI technology to accurately classify different phases of the squat motion. Additionally, this notebook provides functionality to visualize the motion data through colorful diagrams and allows for the trimming of unnecessary data from the CSV files.


## Contributing
please dont

## License
coming soon

## Acknowledgments
some code stolen from someone else, will link eventually.
