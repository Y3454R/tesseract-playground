import cv2
import pytesseract
from PIL import Image

# Load the image using OpenCV
image = cv2.imread('images/sample_image_bangla.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to improve text clarity
thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Save the preprocessed image (optional)
cv2.imwrite('preprocessed_image.png', thresh_image)

# Perform OCR
text = pytesseract.image_to_string(Image.fromarray(thresh_image), lang='ben')

print("Extracted Bangla Text:")
print(text)
