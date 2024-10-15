import cv2
import pytesseract
import os
from PIL import Image

# Directory where the vertical sections are stored
vertical_output_dir = 'output_sections/vertical_sections'

# Perform OCR on each vertical section
for filename in sorted(os.listdir(vertical_output_dir)):
    if filename.endswith('.png'):
        # Load the vertical section image
        section_path = os.path.join(vertical_output_dir, filename)
        section_image = cv2.imread(section_path)

        # Convert to grayscale
        gray_section = cv2.cvtColor(section_image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to improve text clarity
        thresh_section = cv2.threshold(gray_section, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Perform OCR with a configuration that prioritizes number recognition
        custom_config = '--psm 7 -c tessedit_char_whitelist=০১২৩৪৫৬৭৮৯'
        section_text = pytesseract.image_to_string(Image.fromarray(thresh_section), config=custom_config, lang='ben')

        # Print the extracted text for each section
        print(f"Extracted text from {filename}:")
        print(section_text.strip() if section_text.strip() else "No numerals found")
        print("-" * 50)
