# Image-Resizing

This Python script is used to resize images in a specified folder to a target size while maintaining their aspect ratio. Additionally, it moves the original images to a "trash" folder for safekeeping after resizing.

## Requirements
- Python 3.x
- Pillow library (PIL fork)

## Installation
1. Install Python 3.x from the official website: https://www.python.org/downloads/
2. Install the Pillow library using pip:
`pip install Pillow`

## Usage
1. Prepare the image files you want to resize and place them in the imagesToBeResized folder.
2. Create the following directories in the same folder as the script:
  - *imagesResized* (to store the resized images)
  - *trash* (to store the original images after resizing)
3. Run the script using the following command:
`python resize.py`
After running the script, the images in the imagesToBeResized folder will be resized to the target dimensions (369x369) and saved in the imagesResized folder. The original images will be moved to the trash folder.
