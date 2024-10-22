import os
import pandas as pd
from PIL import Image, UnidentifiedImageError
import matplotlib.pyplot as plt
import csv
import shutil
import sys


sys.path.append('/mnt/data/')
import helper 
import CNN_Generator

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')


def display_image(image_path, img_size):
    try:
        img = Image.open(image_path)
        img = img.resize(img_size)  
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    except UnidentifiedImageError:
        print(f"Error: Unable to open '{image_path}' as an image.")

def categorize_images(image_dir, img_size, csv_filename):
    if not os.path.exists(csv_filename):
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Image Name', 'Category'])

    if os.path.exists(csv_filename):
        df = pd.read_csv(csv_filename)
    else:
        df = pd.DataFrame(columns=['Image Name', 'Category'])

    for image_name in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_name)

        if not image_name.lower().endswith(IMAGE_EXTENSIONS):
            print(f"Skipping non-image file: {image_name}")
            continue

        if image_name in df['Image Name'].values:
            continue
        display_image(image_path, img_size)

        category = input(f"Enter a category for '{image_name}': ")

        new_row = pd.DataFrame({'Image Name': [image_name], 'Category': [category]})
        df = pd.concat([df, new_row], ignore_index=True)

        df.to_csv(csv_filename, index=False)

        print(f"'{image_name}' categorized as '{category}'.")

    print("All images have been categorized.")

def is_organization_complete(image_dir, output_dir, csv_filename):
    if not os.path.exists(csv_filename):
        print(f"Error: CSV file '{csv_filename}' not found.")
        return False

    df = pd.read_csv(csv_filename)

    for _, row in df.iterrows():
        image_name = row['Image Name']
        category = row['Category']
        category_dir = os.path.join(output_dir, category)
        image_in_category_dir = os.path.join(category_dir, image_name)

        if not os.path.exists(image_in_category_dir):
            return False
    return True


def organize_images(image_dir, csv_filename, output_dir):

    if not os.path.exists(csv_filename):
        print(f"Error: CSV file '{csv_filename}' not found.")
        return

    df = pd.read_csv(csv_filename)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for _, row in df.iterrows():
        image_name = row['Image Name']
        category = row['Category']
        image_path = os.path.join(image_dir, image_name)

        category_dir = os.path.join(output_dir, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

        if os.path.exists(image_path):
            shutil.move(image_path, os.path.join(category_dir, image_name))
            print(f"Moved '{image_name}' to '{category_dir}'")
        else:
            print(f"Error: '{image_name}' not found in '{image_dir}'")


def generate_cnn_model(organized_dataset_dir):
    CNN_Generator.generate_cnn(organized_dataset_dir)
    print("CNN model has been generated based on the organized dataset.")


def main():
    image_dir = input("Enter the path to the directory containing your images: ")
    if not os.path.exists(image_dir):
        print("The specified directory does not exist.")
        return

    try:
        width = int(input("Enter the desired image width: "))
        height = int(input("Enter the desired image height: "))
        img_size = (width, height)
    except ValueError:
        print("Invalid input for image size. Please enter integer values.")
        return

    csv_filename = 'categorized_images.csv'
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(IMAGE_EXTENSIONS)]
    num_images = len(image_files)

    if os.path.exists(csv_filename):
        df = pd.read_csv(csv_filename)
        if len(df) == num_images:
            print("All images are already categorized. Skipping classification step.")
        else:
            print(f"Found {len(df)} categorized images, but there are {num_images} images in total.")
            categorize_images(image_dir, img_size, csv_filename)
    else:
        categorize_images(image_dir, img_size, csv_filename)
    output_dir = 'organized_dataset'

    if is_organization_complete(image_dir, output_dir, csv_filename):
        print("All images are already organized. Skipping organization step.")
    else:
        organize_images(image_dir, csv_filename, output_dir)

    generate_cnn_model(output_dir)

if __name__ == "__main__":
    main()
