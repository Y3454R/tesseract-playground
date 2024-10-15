import cv2
import pytesseract
import os
from PIL import Image

# Check if Tesseract is installed and accessible
try:
    # Attempt to get the Tesseract version to verify it's accessible
    pytesseract.get_tesseract_version()
except Exception as e:
    print("Tesseract is not installed or not found in PATH.")
    print("Please make sure Tesseract is installed and added to your PATH.")
    raise SystemExit(e)  # Exit the program if Tesseract is not available

# Define directories and file paths
image_directory = 'images'  # Directory containing input images
output_directory = 'output_sections/lower_halves'  # Directory for cropped images
log_file_path = 'extraction_log.txt'  # Log file for OCR results
patterns_file = 'number_patterns.txt'  # Path to your user-defined patterns file

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Delete all existing files in the output directory
for filename in os.listdir(output_directory):
    file_path = os.path.join(output_directory, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
print(f"All existing files in {output_directory} have been deleted.")

# Open the log file for writing
with open(log_file_path, 'w', encoding='utf-8') as log_file:
    # Loop through each image in the input directory
    for filename in os.listdir(image_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check for image formats
            image_path = os.path.join(image_directory, filename)

            try:
                # Load the image using OpenCV
                image = cv2.imread(image_path)
                if image is None:
                    raise ValueError(f"Image file {filename} could not be read. It might be corrupted.")

                # Get image dimensions
                height, width = image.shape[:2]

                # Cut the image horizontally in half
                lower_half = image[height // 2:height, 0:width]

                # Save the cropped lower half
                cropped_image_path = os.path.join(output_directory, f'lower_half_{filename}')
                cv2.imwrite(cropped_image_path, lower_half)
                print(f"Cropped lower half saved as: {cropped_image_path}")

                # Convert the lower half to a PIL image for pytesseract
                lower_half_pil = Image.fromarray(lower_half)

                # Set the DPI to improve OCR quality
                lower_half_pil.save('temp_image.png', dpi=(300, 300))
                lower_half_pil = Image.open('temp_image.png')

                # Define custom configuration for Bangla OCR with user-defined patterns
                custom_config = f'-l ben --psm 6 --user-patterns {patterns_file} -c tessedit_char_whitelist=০১২৩৪৫৬৭৮৯'

                # Perform OCR on the lower half
                extracted_text = pytesseract.image_to_string(lower_half_pil, config=custom_config)

                # Print and log the extracted text
                log_file.write(f"Extracted text from {filename}:\n")
                if extracted_text.strip():
                    print(f"Extracted text from {filename}: {extracted_text.strip()}")
                    log_file.write(extracted_text.strip() + '\n')
                else:
                    print(f"No text found in {filename}.")
                    log_file.write("No text found.\n")

                log_file.write("-" * 50 + '\n')

            except Exception as e:
                print(f"Error processing {filename}: {e}")
                log_file.write(f"Error processing {filename}: {e}\n")

print("Processing complete. Check 'extraction_log.txt' for details.")
