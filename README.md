Image Categorizer and CNN Generator
This project provides a way to categorize images, organize them into labeled folders, and generate a Convolutional Neural Network (CNN) model based on the organized dataset.

Features
Interactive Image Categorization: The script allows the user to classify images manually by viewing them and assigning categories.
Automatic Dataset Organization: Once images are categorized or presented in a CSV file, they are automatically sorted into folders by category.
CNN Model Generation: After organizing the dataset, the script generates a CNN model using the categorized images.

Requirements:


Python 3.8 or higher
Required packages: pandas, PIL, matplotlib, tensorflow, shutil

Install the required dependencies by running in the terminal:

pip install pandas pillow matplotlib tensorflow


Run the Main Script:

python3 interactive_image_categorizer_and_cnn.py


Provide Inputs:

Enter the directory path containing your images.
Specify the desired image size (width and height).
Manually categorize any uncategorized images.
The script will skip those steps if images are already categorized and organized.

Output:

The script will organize the images into folders based on the categories they have been defined as.
A CNN model will be generated based on the organized dataset.


File Structure
interactive_image_categorizer_and_cnn.py: Main script that handles categorization, organization, and CNN generation.
helper.py: Helper functions for image manipulation and other utilities.
CNN_Generator.py: Script for generating a CNN model based on the organized dataset.
categorized_images.csv: CSV file storing the image names and their categories.
