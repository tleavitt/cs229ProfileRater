import numpy as np
import matplotlib
#matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import random
from copy import deepcopy
import pickle

# def get_image(imgname):
#     return mpimg.imread(imgname) #represents each pixel as a 3-tuple of RGB values
#     #return np.apply_along_axis(lambda x: 1. if x[0] == 0 else 0., 2, raw_img) #flattens to a 2d matrix

# def plot_image(mtx, filename = None):
#     plt.imshow(mtx)

# plt.clf()
# # plt.axis([-1., 1., -1., 1.])
# face = get_image("SCUT-FBP-100.jpg")
# plot_image(face)
# x = plt.ginput(n=3, timeout=-1)
# #plt.show()
# print "clicked:", x

def label_face(filename):
	plt.clf()
	face = mpimg.imread(filename)
	plt.imshow(face)
	labels = plt.ginput(n=19, timeout=-1, show_clicks=True)
	print "points labeled:", labels
	return labels

pic_names = ["SCUT-FBP-{}.jpg".format(i) for i in xrange(100, 110)]
labeled_pics = {}

for pic_name in pic_names:
	labeled_pics[pic_name] = label_face("faces/" + pic_name)

with open("labeled_faces.txt", "w") as f:
	pickle.dump(labeled_pics, f)
# 	for i in xrange(len(pic_names)):
# 		pic_name = pic_names[i]
# 		pic_labels = pts[i]
# 		print "Writing:", pic_name
# 		f.write(pic_name + pickle.dumps(pic_labels))


print "Done!"
