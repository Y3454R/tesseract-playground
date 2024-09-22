import cv2
from openocr import OpenOCR

# Load the image using OpenCV
image_path = 'images/sample_image_bangla.jpg'
image = cv2.imread(image_path)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to improve text clarity
thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Save the preprocessed image (optional)
preprocessed_path = 'preprocessed_image_openocr.png'
cv2.imwrite(preprocessed_path, thresh_image)

# Create an OpenOCR object
ocr = OpenOCR()

# Use the object to perform OCR on the preprocessed image
text = ocr.ocr_image(preprocessed_path)

print("Extracted Bangla Text:")
print(text)
