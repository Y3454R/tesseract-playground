import os

# Directory containing the images to rename
directory = 'images'  # Change this to your images directory path

# List all files in the directory
files = sorted(os.listdir(directory))

# Iterate through the files and rename them
for index, filename in enumerate(files):
    # Construct the new filename
    new_name = f'test_{index + 1}.png'  # Change the extension if necessary

    # Get the full paths for the old and new filenames
    old_file_path = os.path.join(directory, filename)
    new_file_path = os.path.join(directory, new_name)

    # Rename the file
    os.rename(old_file_path, new_file_path)

    print(f'Renamed: {filename} to {new_name}')
