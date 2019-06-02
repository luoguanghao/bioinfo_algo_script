'''
Code Challenge: Implement the expectation maximization algorithm for soft k-means clustering.
	>Input: Integers k and m, followed by a stiffness parameter β, followed by a set of points Data in m-dimensional space.
	>Output: A set Centers consisting of k points (centers) resulting from applying the expectation maximization algorithm for soft
	 k-means clustering. Select the first k points from Data as the first centers for the algorithm and run the algorithm for 100
	E-steps and 100 M-steps. Results should be accurate up to three decimal places.
-------------------
Sample Input:
2 2
2.7
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
-------------------
Sample Output:
1.662 2.623
1.075 1.148
-------------------
Lo Kwongho 2018.9
'''
import numpy as np
import math
import copy
from os.path import dirname

def d(vId,wId):
	s = 0
	for i in range(m):
		s += (points[vId][i]-Centers[wId][i])**2
	return math.sqrt(s)
	
def Centers_to_Soft_Clusters():
	global hiddenMatrix
	global Centers
	for i in range(point_num):
		Epsilon = 0
		for j in range(k):
			hiddenMatrix[j][i] = math.exp(-beta*d(i,j))
			Epsilon += hiddenMatrix[j][i]
		for j in range(k):
			hiddenMatrix[j][i] /= Epsilon
			
def count(i,j): ##
	cnt = 0
	divi = 0
	for x in range(point_num):
		cnt += points[x][j]*hiddenMatrix[i][x]
		divi += hiddenMatrix[i][x]
	return cnt/divi
	
def Soft_Clusters_to_Centers():
	global hiddenMatrix
	global Centers
	for i in range(k):
		for j in range(m):
			Centers[i][j] = count(i,j)
			
def Soft_k_Means_Clustering():
	global hiddenMatrix
	global Centers
	Centers = copy.deepcopy(points[:k])
	hiddenMatrix = np.zeros(shape=(k,point_num),dtype=float)
	i = 0
	while(i<100):
		i += 1
		Centers_to_Soft_Clusters()
		Soft_Clusters_to_Centers()
	return Centers

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	[k,m] = list(map(int,dataset[0].split()))
	beta = float(dataset[1])
	dataset = dataset[2:]
	point_num = len(dataset)
	points = [list(map(float,item.split())) for item in dataset]
	Centers = Soft_k_Means_Clustering()
	for c in Centers:
		for i in range(len(c)):
			if i!=0:
				print(' ',end='')
			print('%.3f'%c[i],end='')
		print('')