import os
import cv2
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import json

DATASET_PATH = "dataset"
IMG_SIZE = 64

data = []
labels = []

class_names = sorted(os.listdir(DATASET_PATH))
label_map = {label: idx for idx, label in enumerate(class_names)}

for label in class_names:
    path = os.path.join(DATASET_PATH, label)
    for img_name in os.listdir(path):
        try:
            img_path = os.path.join(path, img_name)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            data.append(img)
            labels.append(label_map[label])
        except Exception as e:
            print(f"Error loading {img_name}: {e}")

data = np.array(data) / 255.0
labels = tf.keras.utils.to_categorical(labels)

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(class_names), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=15, validation_data=(x_test, y_test))

model.save("sign_model.h5")

# Save class names for inference
with open("class_names.json", "w") as f:
    json.dump(class_names, f)