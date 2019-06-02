'''
Code Challenge: Implement UPGMA.
     Input: An integer n followed by a space separated n x n distance matrix.
     Output: An adjacency list for the ultrametric tree returned by UPGMA. Edge weights should be accurate to two decimal places
     (answers in the sample dataset below are provided to three decimal places).

Note on formatting: The adjacency list must have consecutive integer node labels starting from 0. The n leaves must be labeled 0, 1, ..., n - 1 in order of their appearance in the distance matrix. Labels for internal nodes may be labeled in any order but must start from n and increase consecutively.
----------------
Sample Input:
4
0	20	17	11
20	0	20	13
17	20	0	10
11	13	10	0
----------------
Sample Output:
0->5:7.000
1->6:8.833
2->4:5.000
3->4:5.000
4->2:5.000
4->3:5.000
4->5:2.000
5->0:7.000
5->4:2.000
5->6:1.833
6->5:1.833
6->1:8.833
-------------
Lo Kwongho 2018.9
'''

import numpy as np
from os.path import dirname
import termios
import sys
import os

def locateMin(size):
	minVal = 999999
	minId = [-1,-1]
	for x in range(size):
		for y in range(size):
			if x!=y and matrix[x][y]<minVal and delete[x]==False and delete[y]==False:
				minVal = matrix[x][y]
				minId = [x,y]
	#print(minId,size)
	return [minId,minVal]

def buildTree():
	Tree = [[]for i in range(maxn)]
	global matrix
	global delete
	ptr = n
	delete = [False for i in range(maxn)]
	num = [0 for i in range(maxn)]
	for i in range(n):
		num[i] = 1
	weight = [0 for i in range(maxn)]
	while(ptr<maxn):
		'''
		for i in matrix:
			print(i)
		press_any_key_exit("按任意键继续...\n")
		'''
		[[minX,minY],minVal] = locateMin(ptr)
		Tree[ptr].append([minX,minVal/2-weight[minX]])
		Tree[ptr].append([minY,minVal/2-weight[minY]])
		Tree[minX].append([ptr,minVal/2-weight[minX]])
		Tree[minY].append([ptr,minVal/2-weight[minY]])
		weight[ptr]=minVal/2
		delete[minX]=True
		delete[minY]=True
		#print(minX,minY,minVal)
		#print(delete)
		for i in range(ptr+1):
			if delete[i]==False:
				tmp=(matrix[minX][i]*num[minX]+matrix[minY][i]*num[minY])/(num[minX]+num[minY])
				matrix[ptr][i] = tmp
				matrix[i][ptr] = tmp
		num[ptr] = num[minX]+num[minY]
		ptr += 1		
	return Tree



if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	n = int(dataset[0])
	dataset = dataset[1:]
	maxn = 2*n-1
	matrix = np.zeros(shape=(maxn,maxn))
	for i in range(len(dataset)):
		matrix[i][:n] = list(map(float,dataset[i].split()))

	Tree = buildTree()
	print('**** Tree ****')
	for i in range(2*n-1):
		for j in range(len(Tree[i])):
			print("%d->%d:%.3f"%(i,Tree[i][j][0],Tree[i][j][1]))
