from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensor2tensor.bin import t2t_eval
import tensorflow as tf
import register


def main(argv):
  t2t_eval.main(argv)


if __name__ == "__main__":
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run()
