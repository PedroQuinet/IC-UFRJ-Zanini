from PIL import Image
import os
import numpy as np
import tensorflow as tf
import pandas as pd

IMAGE_SIZES = [100, 100]

# reads all images in filepath, resizes it according with 2D list img_sizes and 
# store them in a np_array. The string filepath can only contain images (no other
# file types such as txt for example are allowed). 
# It works only for RGB images.
def images_to_np_array(filepath, img_sizes):
    #-----------------------------------------------------------------------------
    # Args:
    #     filepath:  String with the path to the directory containing the images.
    #                It CANNOT end with the / character.
    #     img_sizes: 2D array [num_rows, num_columns].
    #-----------------------------------------------------------------------------

    # list all files in filepath
    list_of_files = [file for file in os.listdir(filepath)]

    # number of image files
    n_images = len(list_of_files)

    # create np_array to store all images
    array_images = np.zeros([n_images, IMAGE_SIZES[0], IMAGE_SIZES[1], 3])

    for index in range( n_images ):

        # get file name   
        file_name = list_of_files[index]

        # Open the image form working directory
        image = Image.open(filepath + '/' + file_name)

        # resize image
        image_resized = image.resize(IMAGE_SIZES)

        # convert it to numpy
        np_image = np.asarray(image_resized)
        array_images[index,:,:,:] = np_image

    return array_images


# read all capivaras
capivara_array = images_to_np_array(filepath = "./capivara", img_sizes = IMAGE_SIZES)
y_capivara = np.zeros(capivara_array.shape[0])

# read all dunkies
burro_array = images_to_np_array(filepath = "./burro", img_sizes = IMAGE_SIZES)
y_burro = np.ones(burro_array.shape[0])

# create y vector with labels
y = np.concatenate( (y_capivara, y_burro) )

# concatenate and shuffle images
array_images = np.concatenate( (capivara_array, burro_array), axis = 0 )
number_of_images = array_images.shape[0]
permuted_index = np.random.permutation(number_of_images)
array_images = array_images[permuted_index, :, :, :]
y = y[permuted_index]

# splitting training and test sets

x_train = array_images[0:700,:,:,:]
y_train = y[0:700]

x_test = array_images[700:,:,:,:]
y_test = y[700:]


# preprocessing 
array_images = tf.keras.applications.densenet.preprocess_input(array_images, data_format = "channels_last")


# initialize model with weights treined in imagenet 
base_model = tf.keras.applications.DenseNet169(
    include_top=False,
    weights="imagenet",
    input_shape=(IMAGE_SIZES[0], IMAGE_SIZES[1], 3),
    pooling="avg",
    classes=2,
    classifier_activation="None"
)

# Freeze model weights
base_model.trainable = False

# data augmentation layer
data_augmentation = tf.keras.Sequential(
    [tf.keras.layers.RandomFlip("horizontal"), tf.keras.layers.RandomRotation(0.5),]
)

inputs = tf.keras.Input(shape=(IMAGE_SIZES[0], IMAGE_SIZES[1], 3))
# apply data augmentation
x = data_augmentation(inputs)
# We make sure that the base_model is running in inference mode here,
# by passing `training=False`. This is important for fine-tuning, as you will
# learn in a few paragraphs.
x = base_model(x, training=False)
# Convert features of shape `base_model.output_shape[1:]` to vectors
x = tf.keras.layers.Flatten(data_format = "channels_last")(x)
x = tf.keras.layers.Dense(100, activation = "relu")(x)
x = tf.keras.layers.Dense(100, activation = "relu")(x)
x = tf.keras.layers.Dense(100, activation = "relu")(x)
outputs = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(inputs, outputs)

model.summary()

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate = 0.0001),
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    metrics=[tf.keras.metrics.BinaryAccuracy()],
)

history = model.fit(x = x_train, 
                    y = y_train, 
                    epochs = 100, 
                    validation_data = (x_test, y_test), 
                    batch_size = 100)
