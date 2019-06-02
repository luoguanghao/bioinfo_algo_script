'''
Code Challenge: Implement HierarchicalClustering.
  >>>Input: An integer n, followed by an n x n distance matrix.
  >>>Output: The result of applying HierarchicalClustering to this distance matrix (using Davg), with each newly created cluster listed
     on each line.
-------------------
Sample Input:
7
0.00 0.74 0.85 0.54 0.83 0.92 0.89
0.74 0.00 1.59 1.35 1.20 1.48 1.55
0.85 1.59 0.00 0.63 1.13 0.69 0.73
0.54 1.35 0.63 0.00 0.66 0.43 0.88
0.83 1.20 1.13 0.66 0.00 0.72 0.55
0.92 1.48 0.69 0.43 0.72 0.00 0.80
0.89 1.55 0.73 0.88 0.55 0.80 0.00
-------------------
Sample Output:
4 6
5 7
3 4 6
1 2
5 7 3 4 6
1 2 5 7 3 4 6
-------------------
Lo Kwongho 2018.9

* Just like the UPGMA
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

		[[minX,minY],minVal] = locateMin(ptr)
		Tree[ptr].append([minX,minVal/2-weight[minX]])
		Tree[ptr].append([minY,minVal/2-weight[minY]])
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

def traversalTree(v):

	global visited
	if v < n:
		return [v+1]
	items = []
	for i in Tree[v]:
		items += traversalTree(i[0])
	'''
	for i in range(len(items)):
		if i!=0:
			print(' ',end='')
		print(items[i]+1,end='')
	print('')
	'''
	'''
	print('#',v)
	print(items)
	input()
	'''
	return [items]


def tree(lst):
	# 树状图输出列表
	l = len(lst)
	if l == 0:
		print('-' * 3)
	else:
		for i, j in enumerate(lst):
			if i != 0:
				#f.write(tabs[0])
				print(tabs[0], end='')
			if l == 1:
				s = '=' * 3
			elif i == 0:
				s = '┬' + '-' * 2
			elif i + 1 == l:
				s = '└' + '─' * 2
			else:
				s = '├' + '─' * 2
			#f.write(s)
			print(s, end='')
			if isinstance(j, list) or isinstance(j, tuple):
				if i + 1 == l:
					tabs[0] += blank[0] * 3
				else:
					tabs[0] += '│' + blank[0] * 2
				tree(j)
			else:
				print(j)
				#f.write(j + "\n")
	tabs[0] = tabs[0][:-3]

def outPut():
	global visited
	global tabs
	global blank
	visited = [0 for i in range(maxn)]
	TreeList=traversalTree(maxn-1)
	
	blank = [
			chr(183)]  ##此处为空格格式;Windows控制台下可改为chr(12288) ;linux系统中可改为chr(32)【chr(32)==' ' ;chr(183)=='·' ;chr(12288)=='　'】
	tabs = ['']	
	
	tree(TreeList)

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	n = int(dataset[0])
	dataset = dataset[1:]
	maxn = 2*n-1
	matrix = np.zeros(shape=(maxn,maxn))
	for i in range(len(dataset)):
		matrix[i][:n] = list(map(float,dataset[i].split()))
		
	
	Tree = buildTree()
	'''
	for i in range(maxn):
		print(i,[a for a in Tree[i]])
	'''
	
	

	
	outPut()
	'''
	print('**** Tree ****')
	for i in range(2*n-1):
		for j in range(len(Tree[i])):
			print("%d->%d:%.3f"%(i,Tree[i][j][0],Tree[i][j][1]))
	'''