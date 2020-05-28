import os

if not os.path.isdir(".\\demo"):
    raise IOError("This should be run from the \\birds directory.")

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.python.data import Dataset
import demo



# demo.convert.make_images.run(demo.csv_parser.parse_get_videos())
demo.frame_nn.main()


# TODO section


# TODO: Use padding + bucketing for variable length
# TODO: Data augmentation
# TODO Note- the framerate for 722701 and 723925 is not 29.97.

