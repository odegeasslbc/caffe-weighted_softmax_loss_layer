# caffe-weighted_softmax_loss_layer
Source files of a weighted_softmax_with_loss layer for latest version of caffe (http://caffe.berkeleyvision.org/). 
Allow wild cards to be accepted as a bottom input of the loss layer

#Usage

    put the .hpp file in:      
    /path-to-your-caffe-master/include/caffe/layers/   
    put the .cpp and .cu files in: 
    /path-to-your-caffe-master/src/caffe/layers/ 

then compile it in terminal at  /path-to-your-caffe-master/   by typing   "make all"

in caffe prototxt file:
```
layer {
  name: "image_data"
  type: "Data"
  top: "image_data"
  top: "label"
}
layer {
  name: "junk_image_data"
  type: "Data"
  top: "junk_image_data"    # <-- we don't need this junk image
  top: "sample_weight"      # <-- but we do need this label as a weight 
                                  which you want to assign when calculate the loss
}
layers {
    name: "loss"
    type: "WeightedSoftmaxWithLoss"
    bottom: "last_layer"
    bottom: "label"
    bottom: "sample_weight"  # <-- add this
    top: "loss"
}
```
