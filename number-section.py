import cv2
import os

# Create the output directory for vertical sections if it doesn't exist
vertical_output_dir = 'output_sections/vertical_sections'
os.makedirs(vertical_output_dir, exist_ok=True)

if os.path.exists(vertical_output_dir):
    # Iterate over all items in the directory
    for item in os.listdir(vertical_output_dir ):
        item_path = os.path.join(vertical_output_dir , item)  # Get full path

        # Check if the item is a file
        if os.path.isfile(item_path):
            os.remove(item_path)  # Delete the file

    # print(f"All files deleted from: {vertical_output_dir }")
else:
    print(f"The directory does not exist: {vertical_output_dir }")

# Directory containing the images to process
images_dir = 'images'

# Iterate over each image file in the images directory
for filename in sorted(os.listdir(images_dir)):
    if filename.endswith(('.jpg', '.png')):  # Check for image file extensions
        image_path = os.path.join(images_dir, filename)
        # Load the image using OpenCV
        image = cv2.imread(image_path)

        # Get image dimensions
        height, width = image.shape[:2]

        # Split the image horizontally
        lower_section = image[int(height / 2):height, 0:width]  # Bottom half for numbers

        # Calculate the widths for the sections
        first_section_width = width // 3
        second_section_width = width - first_section_width

        # Extract the first section (1/3)
        first_section = lower_section[:, 0:first_section_width]
        first_section_path = os.path.join(vertical_output_dir, f'{filename}_first_section.png')
        cv2.imwrite(first_section_path, first_section)
        # print(f"First section (1/3) saved as: {first_section_path}")

        # Extract the second section (2/3)
        second_section = lower_section[:, first_section_width:width]
        second_section_path = os.path.join(vertical_output_dir, f'{filename}_second_section.png')
        cv2.imwrite(second_section_path, second_section)
        # print(f"Second section (2/3) saved as: {second_section_path}")
