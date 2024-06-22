# from PIL import Image
# import os

# def resize_images(input_dir, new_size):
#     # Loop through all files in the input directory
#     for filename in os.listdir(input_dir):
#         if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
#             # Open the image
#             img_path = os.path.join(input_dir, filename)
#             img = Image.open(img_path)

#             # Resize the image
#             resized_img = img.resize(new_size, Image.ANTIALIAS)

#             # Overwrite the original image with the resized image
#             resized_img.save(img_path)

#             print(f"Resized {filename} successfully")

# # Set the input directory
# input_dir = "/home/sam/Desktop/original"

# # Set the new size (width, height) in pixels
# new_size = (300, 300)

# # Resize images
# resize_images(input_dir, new_size)



# import os
# import glob

# def rename_images(directory):
#     # Change directory to where images are located
#     os.chdir(directory)
    
#     # Get a list of all image files in the directory
#     image_files = glob.glob('*.png') + glob.glob('*.jpg') + glob.glob('*.jpeg') + glob.glob('*.gif')
    
#     # Rename each image file
#     start_index = 100
#     for i, old_name in enumerate(image_files, start=start_index):
#         extension = os.path.splitext(old_name)[1]
#         new_name = f'pic{i}{extension}'
#         os.rename(old_name, new_name)
#         print(f'Renamed "{old_name}" to "{new_name}"')

# # Specify the directory containing the images
# directory = '/home/sam/Desktop/whatsapp'

# # Call the function to rename images
# rename_images(directory)

# import os
# import glob
# from PIL import Image

# def rename_images(directory):
#     # Change directory to where images are located
#     os.chdir(directory)
    
#     # Get a list of all image files in the directory
#     image_files = glob.glob('*.png') + glob.glob('*.jpg') + glob.glob('*.jpeg') + glob.glob('*.gif')
    
#     # Rename each image file
#     for i, old_name in enumerate(image_files, 1):
#         extension = os.path.splitext(old_name)[1]
#         if extension.lower() in ['.jpg', '.jpeg']:
#             # Convert JPEG/JPG to PNG
#             img = Image.open(old_name)
#             new_name = f'pic{i}.png'
#             img.save(new_name)
#             os.remove(old_name)
#         else:
#             new_name = f'pic{i}{extension}'
#             os.rename(old_name, new_name)
#         print(f'Renamed "{old_name}" to "{new_name}"')

# # Specify the directory containing the images
# directory = '/home/sam/Desktop/whatsapp'

# # Call the function to rename images
# rename_images(directory)
# from PIL import Image
# import os

# def resize_images(input_dir, output_dir, new_size):
#     # Create the output directory if it doesn't exist
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     # Loop through all files in the input directory
#     for filename in os.listdir(input_dir):
#         if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
#             # Open the image
#             img_path = os.path.join(input_dir, filename)
#             img = Image.open(img_path)

#             # Resize the image
#             resized_img = img.resize(new_size, Image.ANTIALIAS)

#             # Save the resized image to the output directory
#             output_path = os.path.join(output_dir, filename)
#             resized_img.save(output_path)

#             print(f"Resized {filename} successfully")

# # Set the input and output directories
# input_dir = "input_directory"
# output_dir = "output_directory"

# # Set the new size (width, height) in pixels
# new_size = (300, 300)

# # Resize images
# resize_images(input_dir, output_dir, new_size)
# from PIL import Image
# import os

# def resize_images(input_dir, new_size):
#     # Loop through all files in the input directory
#     for filename in os.listdir(input_dir):
#         if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
#             # Open the image
#             img_path = os.path.join(input_dir, filename)
#             img = Image.open(img_path)

#             # Resize the image
#             resized_img = img.resize(new_size, Image.BILINEAR)

#             # Overwrite the original image with the resized image
#             resized_img.save(img_path)

#             print(f"Resized {filename} successfully")

# # Set the input directory
# input_dir = "/home/sam/Desktop/whatsapp"

# # Set the new size (width, height) in pixels
# new_size = (400, 400)

# # Resize images
# resize_images(input_dir, new_size)

# RENAME Custom

import os

def rename_images(directory, start_num=400):
    # List all files in the directory
    files = os.listdir(directory)

    # Filter out only image files (you can add more extensions if needed)
    image_files = [file for file in files if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'))]

    # Sort files to ensure they are renamed in a consistent order
    image_files.sort()

    # Iterate through the image files and rename them
    for i, filename in enumerate(image_files):
        # Construct the new file name
        new_name = f"pic{start_num + i}.png"
        
        # Get the full path to the old and new files
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed '{old_file}' to '{new_file}'")

# Specify the directory containing the images
directory = '/home/sam/Desktop/whatsapp'

# Call the function to rename images
rename_images(directory)
