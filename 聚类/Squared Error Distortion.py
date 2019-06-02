'''
Squared Error Distortion Problem:
 Compute the squared error distortion of a set of data points with respect to a set of centers. 
  Input: A set of points Data and a set of centers Centers.

  Output: The squared error distortion Distortion(Data, Centers). 

Code Challenge: Solve the Squared Error Distortion Problem.
		 Input: Integers k and m, followed by a set of centers Centers and a set of points Data.
		 Output: The squared error distortion Distortion(Data, Centers).
###############
Sample Input:
2 2
2.31 4.55
5.96 9.08
--------
3.42 6.03
6.23 8.25
4.76 1.64
4.47 4.33
3.95 7.61
8.93 2.97
9.74 4.03
1.73 1.28
9.72 5.01
7.27 3.77
###############
Sample Output:
18.246
###############
Lo Kwongho 2018.9
'''

from os.path import dirname
import numpy as np
import math

def  square_EuclideanDistance(vId,wId):
	s = 0
	for i in range(m):
		s += (points[vId][i]-Centers[wId][i])**2
	return s
	
def SquaredErrorDistortion():
	Distortion = 0
	for i in range(k):
		Distortion += square_dist_in_clusters[i]
	return Distortion/points_num
		
def divide():
	clusters = [[] for i in range(k)]
	square_dist_in_clusters = [0 for i in range(k)]
	for i in range(len(points)):
		minVal = INF
		minId = -1
		for c in range(len(Centers)):
			tmp = square_EuclideanDistance(i, c)
			#print(Centers[c],tmp,minVal)
			if tmp < minVal:
				minVal = tmp
				minId = c
			#print(minVal)
			#input()
		clusters[minId].append([i,minVal])
		square_dist_in_clusters[minId] += minVal
	return [clusters,square_dist_in_clusters]

if __name__ == '__main__':
	INF = 999999
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	[k,m] = list( map(int,dataset[0].split()) )
	Centers = [ list(map(float,item.split())) for item in dataset[1:1+k] ]
	dataset = dataset[k+2:]
	points_num = len(dataset)	
	points = [ list(map(float,item.split())) for item in dataset ]
	
	[cluster,square_dist_in_clusters] = divide()

	Distortion = SquaredErrorDistortion()
	print(Distortion)