import cv2
import pytesseract
import os
from PIL import Image

# Directory where the vertical sections are stored
vertical_output_dir = 'output_sections/vertical_sections'

# Define the custom configuration for OCR
custom_config = '--psm 6 -c tessedit_char_whitelist=০১২৩৪৫৬৭৮৯'  # For both sections

# Perform OCR on each vertical section
extracted_results = {}

for filename in sorted(os.listdir(vertical_output_dir)):
    if filename.endswith('.png'):
        # Load the vertical section image
        section_path = os.path.join(vertical_output_dir, filename)
        section_image = cv2.imread(section_path)

        # Convert to grayscale
        gray_section = cv2.cvtColor(section_image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to improve text clarity
        thresh_section = cv2.threshold(gray_section, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Perform OCR
        section_text = pytesseract.image_to_string(Image.fromarray(thresh_section), config=custom_config, lang='ben')

        # Store the extracted text for validation
        extracted_results[filename] = section_text.strip()

# Validate the extracted results based on expected patterns
for filename, text in extracted_results.items():
    if 'first_section' in filename:
        if len(text) == 2 and all(char in '০১২৩৪৫৬৭৮৯' for char in text):
            print(f"Extracted valid text from {filename}: {text}")
        else:
            print(f"Invalid or unexpected text from {filename}: {text}")
    elif 'second_section' in filename:
        if len(text) == 4 and all(char in '০১২৩৪৫৬৭৮৯' for char in text):
            print(f"Extracted valid text from {filename}: {text}")
        else:
            print(f"Invalid or unexpected text from {filename}: {text}")
    else:
        print(f"Unknown section: {filename}")
