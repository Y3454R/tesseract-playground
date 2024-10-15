import cv2
import os
from PIL import Image

# Create the output directory if it doesn't exist
output_dir = 'output_sections'
os.makedirs(output_dir, exist_ok=True)

# Load the image using OpenCV
# 126-jpg_jpg.rf.fc6cd630ae9672be2526c9bfb69e5318_0car_lp.png
# image = cv2.imread('images/sample_image_bangla.jpg')

image = cv2.imread('images/126-jpg_jpg.rf.fc6cd630ae9672be2526c9bfb69e5318_0car_lp.png')

# Get image dimensions
height, width = image.shape[:2]

# Split the image horizontally
upper_section = image[0:int(height/2), 0:width]  # Top half for text
lower_section = image[int(height/2):height, 0:width]  # Bottom half for numbers

# Save the two sections in the specified directory
upper_section_path = os.path.join(output_dir, 'upper_section.png')
lower_section_path = os.path.join(output_dir, 'lower_section.png')

cv2.imwrite(upper_section_path, upper_section)
cv2.imwrite(lower_section_path, lower_section)

print(f"Upper section saved as: {upper_section_path}")
print(f"Lower section saved as: {lower_section_path}")
