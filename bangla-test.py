import cv2
import pytesseract
from PIL import Image

# Load the image using OpenCV
image = cv2.imread('images/sample_image_bangla.jpg')

# Get image dimensions
height, width = image.shape[:2]

# Split the image horizontally
upper_section = image[0:int(height/2), 0:width]  # Top half for text
lower_section = image[int(height/2):height, 0:width]  # Bottom half for numbers

# Convert the sections to grayscale
gray_upper = cv2.cvtColor(upper_section, cv2.COLOR_BGR2GRAY)
gray_lower = cv2.cvtColor(lower_section, cv2.COLOR_BGR2GRAY)

# Apply thresholding to improve text clarity
thresh_upper = cv2.threshold(gray_upper, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
thresh_lower = cv2.threshold(gray_lower, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Perform OCR on each section
upper_text = pytesseract.image_to_string(Image.fromarray(thresh_upper), lang='ben')
lower_text = pytesseract.image_to_string(Image.fromarray(thresh_lower), config='--psm 7', lang='ben')

# Combine the results
extracted_text = upper_text.strip() + "\n" + lower_text.strip()

print("Optimized Extracted Bangla Text:")
print(extracted_text)
