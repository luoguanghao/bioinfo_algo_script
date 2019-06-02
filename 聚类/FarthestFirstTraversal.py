'''
Code Challenge: Implement the FarthestFirstTraversal clustering heuristic.
     Input: Integers k and m followed by a set of points Data in m-dimensional space.
     Output: A set Centers consisting of k points (centers) resulting from applying FarthestFirstTraversal(Data, k),
     where the first point from Data is chosen as the first center to initialize the algorithm.
--------------
Sample Input:
3 2
0.0 0.0
5.0 5.0
0.0 5.0
1.0 1.0
2.0 2.0
3.0 3.0
1.0 2.0
--------------
Sample Output:
0.0 0.0
5.0 5.0
0.0 5.0
--------------
Lo Kwongho 2018.9
'''

import numpy as np
import math
from os.path import dirname

def  EuclideanDistance(vId,wId):
	s = 0
	for i in range(m):
		s += (points[vId][i]-points[wId][i])**2
	return math.sqrt(s)

def FindMaxDistancePoint(points,Centers):
	clusters = [ [] for i in range(len(Centers)) ]
	for i in range(len(points)):
		if visited[i] == 0:
			minVal = 999
			minId = -1
			for j in range(len(Centers)):
				dist = EuclideanDistance(i, Centers[j])
				if dist < minVal:
					minVal = dist
					minId = j
			clusters[minId].append([i,minVal])
	
	maxVal = 0
	maxId = -1
	for i in clusters:
		for j in i:
			if j[1]>maxVal:
				maxVal = j[1]
				maxId = j[0]
	return maxId

def  FarthestFirstTraversal():
	global visited
	Centers = [0]
	visited = [0 for i in range(len(points))]	
	while(len(Centers)<k):
		maxId = FindMaxDistancePoint(points, Centers)
		Centers.append(maxId)
		visited[maxId] = 1
	return Centers
		
	
if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	[k,m] = list(map(int,dataset[0].split() ))
	dataset = dataset[1:]
	points = [list(map(float,item.split())) for item in dataset]
	Centers = FarthestFirstTraversal()
	
	for i in Centers:
		print('%.1f %.1f'%(points[i][0],points[i][1]))