# Import libraries
import numpy as np
import tensorflow as tf
from extra_keras_datasets import emnist

# Load the dataset of uppercase letters
(X_train, y_train), (X_test, y_test) = emnist.load_data(type='letters')

# Preprocess the images
X_train = X_train.reshape(-1, 28, 28, 1) / 255.0 # Reshape and normalize
X_test = X_test.reshape(-1, 28, 28, 1) / 255.0 # Reshape and normalize

# Define the CNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)), # Convolutional layer with 32 filters
    tf.keras.layers.MaxPooling2D(2, 2), # Max pooling layer with pool size of 2x2
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'), # Convolutional layer with 64 filters
    tf.keras.layers.MaxPooling2D(2, 2), # Max pooling layer with pool size of 2x2
    tf.keras.layers.Flatten(), # Flatten layer to convert the output to a vector
    tf.keras.layers.Dense(128, activation='relu'), # Fully connected layer with 128 units and relu activation function
    tf.keras.layers.Dense(26, activation='softmax') # Output layer with 26 units and softmax activation function for multiclass classification
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model on the training data
model.fit(X_train[:10000], y_train[:10000], epochs=10)

# Evaluate the model on the test data
model.evaluate(X_test[:1000], y_test[:1000])

