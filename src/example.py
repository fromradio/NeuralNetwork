# coding utf-8

import numpy as np
import matplotlib.pyplot as plt


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

if __name__ == '__main__':
	t = linear_data_generate(2,100)
	# paint
	#print t
	plane = t["plane"]
	data = t["data"]
	#print data
	label_first = data[:,2]==1
	label_second = data[:,2]==-1
	data_first = data[label_first,0:2]
	print data_first
	data_second = data[label_second,0:2]
	plt.plot(data_first[:,0],data_first[:,1],'ro')
	plt.plot(data_second[:,0],data_second[:,1],'bo')
	plt.show()
