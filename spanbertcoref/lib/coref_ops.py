import tensorflow as tf
from tensorflow.python import pywrap_tensorflow

coref_op_library = tf.load_op_library("./lib/coref_kernels.so")

extract_spans = coref_op_library.extract_spans
tf.NotDifferentiable("ExtractSpans")
