Image Categorizer and CNN Generator
This project provides a pipeline for categorizing images, organizing them into labeled folders, and generating a Convolutional Neural Network (CNN) model based on the organized dataset.

Features
Interactive Image Categorization: The script allows the user to classify images manually by viewing them and assigning categories.
Automatic Dataset Organization: Once images are categorized, they are automatically sorted into folders by category.
CNN Model Generation: After organizing the dataset, the script generates a CNN model using the categorized images.
Requirements
Python 3.8 or higher
Required packages: pandas, PIL (Pillow), matplotlib, tensorflow, shutil
You can install the required dependencies by running:

bash
Copy code
pip install pandas pillow matplotlib tensorflow
Usage
Run the Main Script:

bash
Copy code
python interactive_image_categorizer_and_cnn.py
Provide Inputs:

Enter the directory path containing your images.
Specify the desired image size (width and height).
Manually categorize any uncategorized images.
If images are already categorized and organized, the script will skip those steps.

Output:

The script will organize the images into category-based folders.
A CNN model will be generated based on the organized dataset.
File Structure
interactive_image_categorizer_and_cnn.py: Main script that handles categorization, organization, and CNN generation.
helper.py: Helper functions for image manipulation and other utilities.
CNN_Generator.py: Script for generating a CNN model based on the organized dataset.
categorized_images.csv: CSV file storing the image names and their categories.
Notes
Ensure that the dataset contains only valid image files before running the script.
The output dataset will be organized in the organized_dataset/ folder.
