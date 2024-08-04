# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#PYTHON CODE FOR CATAGORIES 
#pip install tensorflow opencv-python-headless pillow

from typing import List



import os
import shutil
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions, MobileNetV2

# Load pre-trained MobileNetV2 model + higher level layers
model = MobileNetV2(weights='imagenet')

# Define your categories and corresponding folders
categories = {
    'ring': 'rings',
    'necklace': 'necklaces',
    'bracelet': 'bracelets',
    'earring': 'earrings',
    'mangalsutra': 'mangalsutras'
}

# Create folders for each category if they don't exist
base_folder = 'D:\Whats app'  # Change this to your folder containing photos
for folder in categories.values():
    os.makedirs(os.path.join(base_folder, folder), exist_ok=True)

# Function to classify and move images
def classify_and_sort(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    # Preprocess the image
    img_array = preprocess_input(img_array)

    # Predict
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)[0][0]

    # Extract the predicted label
    label = decoded_predictions[1]
    print(f"Image: {image_path} | Predicted: {label}")

    # Move image to the corresponding folder based on the prediction
    for keyword, folder in categories.items():
        if keyword in label:
            shutil.move(image_path, os.path.join(base_folder, folder))
            return

# Path to your images
image_directory = 'D:\Whats app'  # Change this to your folder containing photos

# Process each image
for filename in os.listdir(image_directory):
    file_path = os.path.join(image_directory, filename)
    if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        classify_and_sort(file_path)


