Image Categorization and Organization Project
This project allows users to categorize images manually, save the categories to a CSV file, and then automatically organize the images into folders based on the categories. The scripts are designed for use on macOS but should work on any system with Python installed.

Project Overview
Image Categorization Script: Displays images from a specified folder, allows the user to input categories for each image, and saves the filename and its category to a CSV file.
Organize Images Script: Reads the CSV file and moves the images into corresponding category folders.
Requirements
To run this project, you need the following installed:

Python 3.x
The following Python packages:
Pillow (for image handling)
matplotlib (for displaying images)
pandas (for handling CSV files)
shutil (for file operations, part of Python standard library)



You can install the necessary libraries by running:
bash
Copy code
pip install Pillow matplotlib pandas



Setup and Usage
Step 1: Image Categorization
Image Directory: Ensure you have a folder of images that you want to categorize.

Run the Categorization Script:

Edit the image_dir path in the script to point to the directory containing your images.
Run the script, and it will display each image, asking for a category.
The image name and category will be saved to a CSV file (categorized_images.csv).


Step 2: Organizing Images
CSV File: After running the categorization script, ensure that categorized_images.csv exists and contains the correct data.

Run the Organizing Script:

Edit the image_dir path to point to your images folder.
Edit the output_dir to the location where you want the organized folders to be created.
The script will read the CSV and organize the images into folders based on their category.


Folder Structure:
project_root/
    categorized_images.csv
    categorize_images.py
    organize_images.py
    organized_dataset/
        cats/
            image1.jpg
            image4.jpg
        dogs/
            image2.jpg
            image5.jpg
        birds/
            image3.jpg
