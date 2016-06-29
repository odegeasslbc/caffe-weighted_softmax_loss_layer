# set up Python environment: numpy for numerical routines, and matplotlib for plotting
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import re
#%matplotlib qt4

# display plots in this notebook

# set display defaults
plt.rcParams['figure.figsize'] = (10, 10)        # large images
plt.rcParams['image.interpolation'] = 'nearest'  # don't interpolate: show square pixels
plt.rcParams['image.cmap'] = 'gray'  # use grayscale output rather than a (potentially misleading) color heatmap

import sys
caffe_root = '/media/bruce/research/caffe-master/'  # this file should be run from {caffe_root}/examples (otherwise change this line)
sys.path.insert(0, caffe_root + 'python')

import caffe

import os
trial_root = '/media/bruce/research/trial_17/'
if os.path.isfile(trial_root + 'models/caffe_alexnet_train_iter_200000.caffemodel'):
    print 'CaffeNet found.'
else:
    print 'Model not found'

caffe.set_device(0)  # if we have multiple GPUs, pick the first one
caffe.set_mode_gpu()
#caffe.set_mode_cpu()

model_def = trial_root + 'config/deploy.prototxt'
model_weights = trial_root + 'models/caffe_alexnet_train_iter_200000.caffemodel'

net = caffe.Net(model_def,      # defines the structure of the model
                model_weights,  # contains the trained weights
                caffe.TEST)     # use test mode (e.g., don't perform dropout)



# load the mean ImageNet image (as distributed with Caffe) for subtraction
mu = np.load('/media/bruce/research/image_database/mean.npy')
mu = mu.mean(1).mean(1)  # average over pixels to obtain the mean (BGR) pixel values
print 'mean-subtracted values:', zip('BGR', mu)

# create transformer for the input called 'data'
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})

transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
transformer.set_channel_swap('data', (2,1,0))  # swap channels from RGB to BGR


net.blobs['data'].reshape(50,        # batch size
                          3,         # 3-channel (BGR) images
                          227, 227)  # image size is 227x227

 

def get_prediction(image):
	transformed_image = transformer.preprocess('data', image)
	#plt.imshow(image)
	#plt.show()


	# copy the image data into the memory allocated for the net
	net.blobs['data'].data[...] = transformed_image

	### perform classification
	output = net.forward()

	output_prob = output['prob'][0]  # the output probability vector for the first image in the batch

	print 'predicted class is:', output_prob.argmax()
	return output_prob.argmax()

#labels_file = '/media/bruce/research/images/label'
#labels = np.loadtxt(labels_file, str, delimiter='\t')
# sort top five predictions from softmax output
#top_inds = output_prob.argsort()[::-1][:5]  # reverse sort and take five largest items
#print zip(output_prob[top_inds],labels[top_inds])

predictFile = open('/media/bruce/research/trial_17/predict_result.txt',"w")
gtFile = open('/media/bruce/research/trial_17/gt.txt',"w")

flag = 1
with open('/media/bruce/research/trial_17/test') as test_file:
	for line in test_file:
		name = re.search(r'.+jpg',line).group()
		image = caffe.io.load_image('/media/bruce/research/images/' + name)
		value = get_prediction(image)
		predictFile.write(str(value)+'\n')

		gtValue = re.search(r'\d+',line).group(0)
		gtFile.write(str(gtValue)+'\n')
		
		print "tested images: " + str(flag)
		flag = flag + 1
		
