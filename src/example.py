# coding utf-8

import numpy as np
import matplotlib.pyplot as plt
from Rosenblatt import *

# generate a set of data that can be separated by a hyper plane
def linear_data_generate(m,n):
	# generate a hyper plane
	hyper_plane = np.random.randn(m)
	bias = np.random.randn(1)[0]
	# training_data = np.ndarray(0)
	# print training_data
	training_data = np.zeros([n,m+1])
	training_data[:,0:m] = np.random.randn(n,m)
	# print "training data:",training_data
	for i in range(n):
		# 
		t = training_data[i,0:m]
		# t[0] = 1.0
		if np.dot(t,hyper_plane) + bias < 0:
			training_data[i,m] = -1 # = np.vstack((training_data,np.append(t[1:],-1)))
		elif np.dot(t,hyper_plane) + bias > 0:
			training_data[i,m] = 1 # = np.vstack((training_data,np.append(t[1:],1)))
		else:
			pass
	return {"plane":hyper_plane, "bias":bias, "data":training_data}

def line_function(x,y,w,b):
	# w is the weight vector
	# b is the bias
	return w[0]*x+w[1]*y+b
	# pass 
if __name__ == '__main__':
	t = linear_data_generate(2,1000)
	# paint
	#print t
	plane = t["plane"]
	data = t["data"]
	bias = t["bias"]
	#print data
	label_first = data[:,2]==1
	label_second = data[:,2]==-1
	data_first = data[label_first,0:2]
	#print data_first
	data_second = data[label_second,0:2]
	plt.plot(data_first[:,0],data_first[:,1],'ro')
	plt.plot(data_second[:,0],data_second[:,1],'bo')
	#print data[:,0].max(),data[:,0].min()
	xmin = data[:,0].min()
	xmax = data[:,0].max()
	ymin = data[:,1].min()
	ymax = data[:,1].max()

	#xmin,xmax = (-1.5,1.5)
	XT = np.linspace(xmin,xmax,100)
	YT = np.linspace(ymin,ymax,100)
	X,Y = np.meshgrid(XT,YT)
	Z = line_function(X,Y,plane,bias)

	t = Rosenblatt_sensor(2,0.5)
	# print data.shape
	t.learning_process(data)
	print t.weight(),t.bias()
	print plane,bias
	plt.contour(X,Y,Z,[0])
	ZZ = line_function(X,Y,t.weight(),t.bias())
	plt.contour(X,Y,ZZ,[0],color='r')
	plt.show()
