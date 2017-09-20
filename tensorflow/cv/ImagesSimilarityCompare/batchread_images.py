'''
name:batchreadimgs.py
create date:8/23/2017
author:jimchen
'''

import tensorflow as tf 
import numpy as np
import scipy.misc as misc
import os
		
		
IMGS_PLACE_DIR = "/images/"
		
def getImagesandLabels():
	paths=[]
	labels=[]
	cwd=os.getcwd()+IMGS_PLACE_DIR
	for file_name in os.listdir(cwd):
		if file_name.endswith('png'):
			filefullpath = os.path.join(cwd, file_name)
			paths.append(filefullpath)
			filepath,tempname = os.path.split(filefullpath)
			singlename,ext = os.path.splitext(tempname)
			labels.append(singlename)
	return paths,labels


images=[]
labels=[]
images,labels = getImagesandLabels()
print("loadimgfromfile images:\n%s \n\nlabels:\n%s"%(images,labels))
filename_queue = tf.train.slice_input_producer([images,labels], shuffle=True, num_epochs=5)
file_contents=tf.read_file(filename_queue[0])
image_buf = tf.image.decode_image(file_contents,channels=3)
label=filename_queue[1]
sess.run(tf.local_variables_initializer())
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess,coord=coord)
num=len(labels)
print("images total num:",num)
all_label=[]
all_photo=[]
with tf.Session() as sess:	
	for i in range(num):
		image,label_value = sess.run([image_buf,label])
		image_shape = image.shape
		print("image image_shape:",image_shape)
		all_label.append(label_value)
		all_photo.append(image)
		#misc.imsave('read/%d'%(i)+'.jpg',image)
	#print("image image[0]:",image[0])
coord.request_stop()
coord.join(threads)




















 
