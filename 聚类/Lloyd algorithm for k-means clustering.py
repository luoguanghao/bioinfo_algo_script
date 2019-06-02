'''
Code Challenge: Implement the Lloyd algorithm for k-means clustering.
     Input: Integers k and m followed by a set of points Data in m-dimensional space.
     Output: A set Centers consisting of k points (centers) resulting from applying the Lloyd algorithm to Data and Centers,
     where the first k points from Data are selected as the first k centers.
------------
Sample Input:
2 2
1.3 1.1
1.3 0.2
0.6 2.8
3.0 3.2
1.2 0.7
1.4 1.6
1.2 1.0
1.2 1.1
0.6 1.5
1.8 2.6
1.2 1.3
1.2 1.0
0.0 1.9
------------
Sample Output:
1.800 2.867
1.060 1.140
------------
Lo Kwongho 2018.9

* this algorithm doesn't always converge to the optimal solution:
try  points {0, 1, 1.9, 3} and the origin center {1,3}
'''
from os.path import dirname
import numpy as np
import math

def  square_EuclideanDistance(vId,wId,Centers):
	s = 0
	for i in range(m):
		s += (points[vId][i]-Centers[wId][i])**2
	return s

def Centers_to_Clusters(Centers):
	global Cluster
	Cluster = [[] for i in range(k)]
	Distortion = 0
	for i in range(len(points)):
		minVal = INF
		minId = -1
		for c in range(len(Centers)):
			tmp = square_EuclideanDistance(i, c,Centers)
			if tmp < minVal:
				minVal = tmp
				minId = c
		Cluster[minId].append(i)
		Distortion += minVal
	return Distortion/points_num
			
def Clusters_to_Centers():
	#print(Cluster)
	Centers = []
	for i in range(k):
		coordinate = [0 for i in range(m)]
		for pId in Cluster[i]:
			for j in range(m):
				coordinate[j] += points[pId][j]
		coordinate = [item/len(Cluster[i]) for item in coordinate]
		Centers.append(coordinate)
	print(Centers)
	return Centers

def LloydClustering():
	global Cluster
	Centers = points[:k]
	minDistortion = INF	
	Distortion = Centers_to_Clusters(Centers)
	i = 0
	while(Distortion < minDistortion):
		i += 1
		print('*%d iteration*...'%i)
		minDistortion = Distortion
		Centers = Clusters_to_Centers()
		Distortion = Centers_to_Clusters(Centers)		
	return [Centers,Distortion]

if __name__ == '__main__':
	INF = 999999
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	[k,m] = list(map( int,dataset[0].split() ))
	dataset = dataset[1:]
	points = [list(map(float,item.split())) for item in dataset]
	points_num = len(points)
	print(points_num)
	[Centers,Distortion] = LloydClustering() #Distortion 精确度
	print(Distortion)
	for c in Centers:
		for i in range(len(c)):
			if i != 0:
				print(' ',end='')
			print('%.3f'%c[i],end='')
		print('')