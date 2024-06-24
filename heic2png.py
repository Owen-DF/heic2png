#created by Owen Fleischer 6/21/24
#change top directory to the directory with all the folders with images inside of it

#future work, delete old folders of onconverted files. 

from PIL import Image
import numpy as np
import cv2
import pillow_heif
import os
import shutil



#change here for other directories
topDirectory = r"C:\Users\ofleischer\OneDrive - MetroTek Electrical\Luminace Sites\9362.33 MD - 19-S142 Boonsboro\Photos"
count = 0
for folder in os.listdir(topDirectory):
    imageFolderPath = os.path.join(topDirectory, folder)
    if not os.path.isdir(imageFolderPath):
        continue
    outputDirectory = imageFolderPath + " Converted"

    # Ensure the output directory exists
    os.makedirs(outputDirectory, exist_ok=True)
   
    for filename in os.listdir(imageFolderPath):
        if filename.lower().endswith(".heic"):
            heic_file_path = os.path.join(imageFolderPath, filename)
            heif_file = pillow_heif.read_heif(heic_file_path)
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data, 
                "raw", 
                heif_file.mode, 
                heif_file.stride,
            )
            # Ensure the image is in RGB mode
            image = image.convert("RGB")
            # Convert the PIL image to a NumPy array
            np_array = np.array(image)
            output_file_path = os.path.join(outputDirectory, filename.replace(".heic", ".png"))
            # Save the image using OpenCV
            cv2.imwrite(output_file_path, cv2.cvtColor(np_array, cv2.COLOR_RGB2BGR))
            print(f"Converted {filename} to {output_file_path}")
            count = count + 1

        elif filename.lower().endswith(".jpg"):
            image_filepath = os.path.join(imageFolderPath, filename)
            output_file_path = os.path.join(outputDirectory, filename)
            
            # Copy the file
            shutil.copy2(image_filepath, output_file_path)
            print(f"Copied {filename} to {output_file_path}")
            count = count + 1


print("Conversion complete: " + str(count))
