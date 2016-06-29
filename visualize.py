# get the features of each layer in the give caffe model from given images
# and visalize the output activations (features/ data)

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

# Make sure that caffe is on the python path:
caffe_root = '/media/bruce/research/caffe-master/'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

caffe.set_mode_cpu()
net = caffe.Classifier('/media/bruce/research/trial_17/config/fc6.prototxt',
                       '/media/bruce/research/trial_17/models/caffe_alexnet_train_iter_200000.caffemodel')
# input preprocessing: 'data' is the name of the input blob == net.inputs[0]
net.transformer.set_mean('data', np.load('/media/bruce/research/image_database/mean.npy').mean(1).mean(1))  # ImageNet mean
net.transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
net.transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB

scores = net.predict([caffe.io.load_image('/media/bruce/research/images/15_fauvism/859_ladies-with-parrots_org.jpg')])
print scores

im = caffe.io.load_image('/media/bruce/research/images/15_fauvism/859_ladies-with-parrots_org.jpg')

net.blobs['data'].data[...] = net.transformer.preprocess('data', im)
out = net.forward()
#print out['prob'].argmax()

#print [(k, v[0].data.shape) for k, v in net.params.items()]
#print [(k, v.data.shape) for k, v in net.blobs.items()]

def vis_square(data, padsize=1, padval=0):
    data -= data.min()
    data /= data.max()
    
    # force the number of filters to be square
    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = ((0, n ** 2 - data.shape[0]), (0, padsize), (0, padsize)) + ((0, 0),) * (data.ndim - 3)
    data = np.pad(data, padding, mode='constant', constant_values=(padval, padval))
    
    # tile the filters into an image
    data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3) + tuple(range(4, data.ndim + 1)))
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])
    
    plt.imshow(data)
    plt.show()
	

#plt.imshow(net.transformer.deprocess('data', net.blobs['data'].data[4]))
#plt.show()

#filters = net.params['conv1'][0].data
#print filters
#vis_square(filters.transpose(0, 2, 3, 1))

feat = net.blobs['fc11'].data[0]
plt.subplot(2, 1, 1)
plt.plot(feat.flat)
plt.subplot(2, 1, 2)
_ = plt.hist(feat.flat[feat.flat > 0], bins=100)
plt.show()
