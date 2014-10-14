# coding utf-8

import numpy as np


# generate a set of data that can be separated by a hyper plane
def linear_data_generate(m,n):
	# generate a hyper plane
	hyper_plane = np.random.randn(m+1)
	training_data = []
	for i in range(n):
		# 
		t = np.random.randn(m+1)
		t[0] = 1.0
		if np.dot(t,hyper_plane) < 0:
			training_data.append(np.append(t[1:],-1))
		elif np.dot(t,hyper_plane)> 0:
			training_data.append(np.append(t[1:],1))
		else:
			pass
	return training_data

if __name__ == '__main__':
	t = data_generate(2,10)
	print t
