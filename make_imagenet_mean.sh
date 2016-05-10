#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=/media/bruce/Storage1/new_images
DATA=/home/bruce/Res/new_images
TOOLS=/home/bruce/Res/caffe/build/tools


$TOOLS/compute_image_mean $EXAMPLE/augmented_train_lmdb \
  $EXAMPLE/aug__train_mean.binaryproto

$TOOLS/compute_image_mean $EXAMPLE/augmented_val_lmdb \
  $EXAMPLE/aug_val_mean.binaryproto

echo "Done."
