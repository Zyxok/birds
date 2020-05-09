import demo.csv_parser
from demo.video import VideoFrames
from demo.constants import SPECIES, SPECIES_COUNT

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

import random


def get_images_and_labels():
    videos = demo.csv_parser.parse_get_videos()
    random.shuffle(videos)
    videos = videos[:40]

    images = []
    labels = []
    for video in videos:
        frames_list = list(VideoFrames(video))

        for i in range(5):  # Takes 5 random frames from each video
            frame = random.choice(frames_list)
            frame = frame / 255.0

            images.append(frame)
            labels.append(SPECIES.index(video.species))

    return images, labels


def test_display(images, labels):
    plt.figure(figsize=(10, 10))
    for i in range(15):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap=plt.cm.binary)
        plt.xlabel(SPECIES[labels[i]])
    plt.show()


def main():
    images, labels = get_images_and_labels()
    training_count = 25 * 5
    train_images = np.array(images[:training_count])
    test_images = np.array(images[training_count:])
    train_labels = np.array(labels[:training_count])
    test_labels = np.array(labels[training_count:])

    # test_display(images, labels)

    model = models.Sequential()

    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(360, 585, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(SPECIES_COUNT))
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
