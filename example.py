import tensorflow as tf
import tensorflow_datasets as tfds

# LOAD THE MNIST DATASET #

(ds_train, ds_test), ds_info = tfds.load(
    'mnist',
    split=['train', 'test'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
)

# DISPLAY EXAMPLE ENTRIES #

tfds.show_examples(ds_train, ds_info)