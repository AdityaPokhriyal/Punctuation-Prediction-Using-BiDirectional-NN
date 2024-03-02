import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print(tf.__version__)