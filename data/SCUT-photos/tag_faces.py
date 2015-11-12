import numpy as np
import matplotlib
#matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import random
from copy import deepcopy

def get_image(imgname):
    return mpimg.imread(imgname) #represents each pixel as a 3-tuple of RGB values
    #return np.apply_along_axis(lambda x: 1. if x[0] == 0 else 0., 2, raw_img) #flattens to a 2d matrix

def plot_image(mtx, filename = None):
    plt.imshow(mtx)

plt.clf()
# plt.axis([-1., 1., -1., 1.])
face = get_image("SCUT-FBP-100.jpg")
plot_image(face)
x = plt.ginput(n=3, timeout=-1)
#plt.show()
print "clicked:", x