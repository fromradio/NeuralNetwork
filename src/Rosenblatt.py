# coding utf-8

# Rosenblatt sensor

import numpy as np


class Rosenblatt_sensor:
	"""
	A simple rosenblatt sensor of neural network

	"""
	def __init__(self,n=1,yita = 1.):
		# input:
		#	n is the dimension of input
		#
		self.__n = n # the dimesion
		self.__w = np.zeros(n) # the weight vector of the whole machine
		self.__b = 0. # the bias
		self.__yita = yita # the ratio
		#print 'hello', self.__w

	def learning(self,x,d):
		# update of the machine
		y = np.sign(np.dot(x,self.__w)+self.__b)
		if y != d:
			# update
			self.__w = self.__w + self.__yita*(d-y)*x
			self.__b = self.__b + self.__yita*(d-y)
		else:
			pass
		#print self.__w,self.__b

	def learning_process(self,data):
		# specified data 
		#print "shape",data.shape
		m,n = data.shape # the shape
		for i in range(0,m):
			# iteration
			#print data[i,0:n-1]
			self.learning(data[i,0:n-1],data[i,n-1])
	def weight(self):
		# getter
		return self.__w
	def bias(self):
		return self.__b
	def test(self): 
		print 'test'


def main():
	t = Rosenblatt_sensor(1)
	t.learning([1.],1)
	# t = Rosenblatt_sensor()
	# t.test()

if __name__ == '__main__':
	main()