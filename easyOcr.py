import cv2
import easyocr
import os
import matplotlib.pyplot as plt

# Define directories
image_directory = 'sample'  # Directory containing input images
output_directory = 'output_images'  # Directory to save images with detected text

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Initialize EasyOCR reader for Bangla and English languages
reader = easyocr.Reader(['bn', 'en'], gpu=False)  # 'bn' for Bangla, 'en' for English

# Process each image in the directory
for filename in os.listdir(image_directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check for image formats
        image_path = os.path.join(image_directory, filename)
        print(f"Processing {filename}...")

        # Load the image using OpenCV
        image = cv2.imread(image_path)

        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to improve text clarity
        thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Save the preprocessed image (optional)
        preprocessed_image_path = os.path.join(output_directory, f'preprocessed_{filename}')
        cv2.imwrite(preprocessed_image_path, thresh_image)

        # Perform OCR on the thresholded image
        result = reader.readtext(thresh_image)

        # Display the result
        print("Detected Text:")
        for (bbox, text, prob) in result:
            print(f"Text: {text}, Probability: {prob}")

            # Draw bounding box around detected text
            top_left = tuple(map(int, bbox[0]))
            bottom_right = tuple(map(int, bbox[2]))
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        # Save the image with detected text
        output_image_path = os.path.join(output_directory, f'output_{filename}')
        cv2.imwrite(output_image_path, image)

        # Optionally, display the image with detected text and bounding boxes
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title(f"Detected text in {filename}")
        plt.axis('off')
        plt.show()

print("Processing complete. Check the output_images directory for results.")
