import demo

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

import random


def main():
    dataset = demo.dataset.get_dataset_frames()
    train_images = dataset
    test_images = dataset
    print(dataset)
    # print(test_images)
    # training_count = None  # ????
    # print("TRAINING COUNT:", training_count)
    train_labels = None
    test_labels = None

    # test_display(videos, labels)

    model = models.Sequential()
    model.add(layers.TimeDistributed(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(360, 585, 3))))
    model.add(layers.TimeDistributed(layers.MaxPooling2D((2, 2))))
    model.add(layers.TimeDistributed(layers.Flatten()))
    # model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    # model.add(layers.MaxPooling2D((2, 2)))
    # model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.add(layers.LSTM(32))  # NOT THE AMOUNT OF FRAMES!

    # 8 for testing
    # 128 = Around 5 seconds of frames
    # model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(len(demo.constants.SPECIES), activation='sigmoid'))
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    history = model.fit(train_images, train_labels, epochs=10,
                        validation_data=(test_images, test_labels))

    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0.0, 1])
    plt.legend(loc='lower right')
    plt.show()

    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

    print(test_acc)
