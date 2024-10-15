import cv2
import easyocr
import matplotlib.pyplot as plt

# Load the image using OpenCV
image = cv2.imread('sample/test.png')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to improve text clarity
thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Save the preprocessed image (optional)
cv2.imwrite('preprocessed_image.png', thresh_image)

# Initialize EasyOCR reader for Bangla and English languages
reader = easyocr.Reader(['bn', 'en'], gpu=False)  # 'bn' for Bangla, 'en' for English

# Perform OCR on the thresholded image
result = reader.readtext(thresh_image)

# Display the result
print("Detected Text:")
for (bbox, text, prob) in result:
    print(f"Text: {text}, Probability: {prob}")

# Optionally, display the image with bounding boxes around the detected text
for (bbox, text, prob) in result:
    # Draw bounding box
    top_left = tuple(map(int, bbox[0]))
    bottom_right = tuple(map(int, bbox[2]))
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

# Show the image with detected text and bounding boxes
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
