import os
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import csv

def display_image(image_path):
    img = Image.open(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def categorize_images(image_dir, csv_filename):

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
        

        if image_name in df['Image Name'].values:
            continue
        display_image(image_path)
        category = input(f"Enter a category for '{image_name}': ")
        df = df.append({'Image Name': image_name, 'Category': category}, ignore_index=True)
        df.to_csv(csv_filename, index=False)
        
        print(f"'{image_name}' categorized as '{category}'.")

    print("Classification Complete")


def main():
    image_dir = 'IMAGE DIRECTORY'  
    csv_filename = 'categorized_images.csv'
    categorize_images(image_dir, csv_filename)

if __name__ == "__main__":
    main()
