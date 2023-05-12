import cv2 as cv
from tqdm import tqdm
import pandas as pd
import numpy as np
import seaborn as sns
import tensorflow as tf
import os
from keras.models import Model, Sequential
from keras import layers
from keras import optimizers
import matplotlib.pyplot as plt


# Определение параметров для выполнения функций получения изображений.
data_dir = 'signatures/train'
batch_size = 32
img_height = 64
img_width = 64

# Получение изображений для тренировки.
train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# Получение изображений для проверки.
val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# Вывод названий классов.
class_names = train_ds.class_names
print(class_names)

# Настройка набора данных для производительности.
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# Создание модели
num_classes = len(class_names)

model = Sequential([
    tf.keras.layers.Rescaling(1./255),
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(num_classes)
    ])

model.compile(optimizer='adam',
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_ds, validation_data=val_ds, epochs=3)

model.summary()

# fig, ax = plt.subplots()
# ax.imshow(x_test[76])
# plt.title(y_test[76])
#
# plt.show()





# # Make numpy values easier to read.
# np.set_printoptions(precision=3, suppress=True)
#
# csv_path = "sign_data/train_data.csv"
# path = 'sign_data/train/'
# column = '068/09_068.png'
#
#
# def load_images(csv_path, path, column):
#     """Редактирование и загрузка изображений в массивы."""
#     sign_data = pd.read_csv(csv_path)
#
#     x, y = [], []
# #    for ind in tqdm(sign_data.index):
#     ind = 230
#     name = sign_data[column][ind]
#     img = cv.cvtColor(cv.imread(path+str(name)), cv.COLOR_BGR2GRAY)
#     img = np.array(img).astype('float32')/255
#     img = cv.resize(img, (128,128), cv.INTER_CUBIC)
#     x += [img]
#     y += [str(name).split('/')[0]]
#
#     x, y = np.array(x), np.array(y)
#     return x, y
#
#
# x_train, y_train = load_images(csv_path, path, column)
# fig, ax = plt.subplots()
# ax.imshow(x_train[0])
# plt.title(y_train[0])
# plt.show()
