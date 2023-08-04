from PIL import Image
import shutil
import os

def resize_images(source_folder, destination_folder, trash_folder, target_dimensions):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    if not os.path.exists(trash_folder):
        os.makedirs(trash_folder)
        
    for filename in os.listdir(source_folder):
        input_path = os.path.join(source_folder, filename)
        output_path = os.path.join(destination_folder, filename)
        
        try:
            with Image.open(input_path) as img:
                img.thumbnail(target_dimensions, Image.ANTIALIAS)
                img.save(output_path, optimize=True, quality=95)
            
            trash_path = os.path.join(trash_folder, filename)
            shutil.move(input_path, trash_path)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            
            
source_folder = "./imagesToBeResized/"
destination_folder = "./imagesResized/"
trash_folder = "./trash/"
target_dimensions = (369, 369)

resize_images(source_folder, destination_folder, trash_folder, target_dimensions)