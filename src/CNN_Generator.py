import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import numpy as np
import os

#BUILD THE MODEL
def create_cnn_model(input_shape, num_classes):
    model = models.Sequential()


    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))


    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))


    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))


    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))


    model.add(layers.Dense(num_classes, activation='softmax'))


    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model

#LOAD DATA
def load_data(data_dir, img_size, batch_size):

    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    
    #SPLIT THE DATA 80-20 INTO TRAINING/VERIFICATION
    train_data = datagen.flow_from_directory(data_dir, target_size=img_size, batch_size=batch_size, class_mode='categorical', subset='training')
    val_data = datagen.flow_from_directory(data_dir, target_size=img_size, batch_size=batch_size, class_mode='categorical', subset='validation')

    return train_data, val_data

#TRAIN MODEL
def train_model(model, train_data, val_data, epochs):
    history = model.fit(train_data, epochs=epochs, validation_data=val_data)
    return history

#MAIN GEN FUNCTION
def generate_cnn(organized_dataset_dir):
    data_dir = organized_dataset_dir
    img_size = (128, 128) #IMAGE SIZE
    batch_size = 32 #BATCH SIZE
    num_classes = len(os.listdir(data_dir))  #ASSUMING FOLDERS PER CLASS
    epochs = 10


    train_data, val_data = load_data(data_dir, img_size, batch_size)
    model = create_cnn_model(input_shape=img_size + (3,), num_classes=num_classes)
    history = train_model(model, train_data, val_data, epochs)
    model.save('cnn_image_classifier.h5')

    print("MODEL COMPLETE!")

if __name__ == "__main__":
    main()
