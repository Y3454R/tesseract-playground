import cv2
import os

# Create the output directory for vertical sections if it doesn't exist
vertical_output_dir = 'output_sections/vertical_sections'
os.makedirs(vertical_output_dir, exist_ok=True)

# Load the image using OpenCV
image = cv2.imread('images/sample_image_bangla.jpg')
# image = cv2.imread('images/126-jpg_jpg.rf.fc6cd630ae9672be2526c9bfb69e5318_0car_lp.png')

# Get image dimensions
height, width = image.shape[:2]

# Split the image horizontally
lower_section = image[int(height/2):height, 0:width]  # Bottom half for numbers

# Define the number of vertical splits and the width of each section
num_vertical_splits = 3  # Adjust based on the number of segments needed
split_width = width // num_vertical_splits

# Iterate to create vertical sections
for i in range(num_vertical_splits):
    # Calculate the x-coordinates for each vertical slice
    start_x = i * split_width
    end_x = (i + 1) * split_width if (i + 1) < num_vertical_splits else width

    # Extract the vertical slice from the lower section
    vertical_slice = lower_section[:, start_x:end_x]

    # Save the vertical slice in the specified directory
    vertical_slice_path = os.path.join(vertical_output_dir, f'vertical_section_{i + 1}.png')
    cv2.imwrite(vertical_slice_path, vertical_slice)

    print(f"Vertical section {i + 1} saved as: {vertical_slice_path}")
