import os

from tensorflow.python.data import Dataset
from tensorflow.python.data.ops import dataset_ops
from tensorflow.python.ops import io_ops, image_ops

import demo
from tensorflow.keras import preprocessing
import tensorflow as tf


def map_to_image(path):
    num_channels = 3  # RGB
    img = io_ops.read_file(path)
    img = image_ops.decode_image(
        img, channels=num_channels, expand_animations=False)
    return img

    # image_ops.resize_images_v2(img, image_size, method=interpolation) not resized so


def get_dataset_frames():
    all_paths = []
    for dir_path, frame_count in zip(demo.data_constants.VIDEO_DIR_SORTED_PATHS, demo.data_constants.SORTED_FRAMES):
        temp_frames = []
        for i in range(frame_count):
            temp_frames.append(os.path.join(dir_path, str(i)+'.jpg'))
        all_paths.append(temp_frames)

    # TODO: Add padding, verify if it works
    path_ds = Dataset.from_tensor_slices(all_paths)

    img_ds = path_ds.apply(lambda x: tf.map_fn(map_to_image, x))
    # fix- ValueError: Unbatching a dataset is only supported for rank >= 1

    label_ds = preprocessing.dataset_utils.labels_to_dataset(demo.data_constants.csv_parser_assertions(), 'int', None)
    img_ds = dataset_ops.Dataset.zip((img_ds, label_ds))
    return img_ds

    # dataset = preprocessing.image_dataset_from_directory(
    #    demo.constants.Path.FRAMES,
    #    labels='inferred',  # demo.csv_parser.csv_parser_assertions(),
    #    label_mode=None,  # 'int',
    #    color_mode='rgb',
    #    batch_size=1,
    #    image_size=(360, 585),  # Should all be the same size, already resized
    #    shuffle=True,
    #    seed=demo.constants.SHUFFLE_SEED,
    #    validation_split=0.2,
    #    subset=subset,
    # )
