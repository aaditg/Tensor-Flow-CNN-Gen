import os
import shutil
import pandas as pd

def organize_images(csv_file, image_dir, output_dir):
    df = pd.read_csv(csv_file)

    for index, row in df.iterrows():
        image_name = row['Image Name']
        category = row['Category']

        category_folder = os.path.join(output_dir, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        source = os.path.join(image_dir, image_name)
        destination = os.path.join(category_folder, image_name)
        
        if os.path.exists(source):
            shutil.move(source, destination)
            print(f"Moved '{image_name}' to '{category_folder}'")
        else:
            print(f"Image '{image_name}' not found in '{image_dir}'")

    print("All images have been organized.")

def main():
    csv_file = 'categorized_images.csv'
    image_dir = 'IMAGE DIRECTORY'  
    output_dir = 'DATASET DIRECTORY' 

    organize_images(csv_file, image_dir, output_dir)

if __name__ == "__main__":
    main()
