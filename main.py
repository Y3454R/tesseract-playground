from PIL import Image
import pytesseract
import os

# # For Windows, specify the path to the Tesseract executable (skip this for Linux/macOS)
# # Make sure the path matches where Tesseract is installed
# if os.name == 'nt':  # Check if running on Windows
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load an image from file

image_path = 'images/sample_image.jpeg'  # Replace this with the path to your image
image = Image.open(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(text)

# Optionally, you can detect individual characters and their positions using image_to_boxes
boxes = pytesseract.image_to_boxes(image)
print("\nCharacter Bounding Boxes:")
print(boxes)

# You can also extract data (words, lines, confidence, etc.) using image_to_data
data = pytesseract.image_to_data(image)
print("\nExtracted Data (with bounding boxes and confidence):")
print(data)
