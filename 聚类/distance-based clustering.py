'''
coder Lokwongho 2018.11

'''

from os.path import dirname
import numpy as np
import math
import random
import matplotlib.pyplot as plt

######## Get the Distance Matrix ########
def PearsonCorrelationDistance(Expres):		
	n = len(Expres)
	l = len(Expres[0])
	Distance = np.zeros(shape=[n,n],dtype=float)

	u = [ sum(i)/l for i in Expres ]
	Sigma = []
	for i in range(n):
		sig=0;
		for x in range(l):
			sig += (Expres[i][x]-u[i])**2;
		Sigma.append(sig)
		
	for i in range(n):
		for j in range(i,n):
			sigU=0
			for x in range(l):
				sigU += (Expres[i][x]-u[i])*(Expres[j][x]-u[j])
			Distance[i][j]=1-(sigU)/math.sqrt(Sigma[i]*Sigma[j])
			Distance[j][i]=Distance[i][j]				

	return Distance

######## Build the Hierarchical Tree ########
def locateMin(size): # calculate the diatance between two cluster: minimum distance method
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

def HierarchicalClustering(DMatrix):
	global maxn
	global n
	global Tree
	global matrix

	
	n = len(DMatrix)
	maxn = 2*n-1
	matrix = np.zeros(shape=(maxn,maxn))
	for i in range(n):
		matrix[i][:n] = DMatrix[i]
	Tree = buildTree()
	
######## Input and output Data ########
def InputData(dataset):
	dataset = [line.split() for line in dataset]
	name = [item[1] for item in dataset[1:]]
	#print(m)
	# print(m,k)
	points = []
	for line in dataset[1:]:
		if(len(line)==10):
			points.append(list(map(float,line[3:])))
		elif(len(line)==9):
			points.append(list(map(float,line[2:])))
	return [points,name]

'''
Reference to 'whoami_T' in csdn for print the tree
https://blog.csdn.net/weixin_39722498/article/details/81534247
'''
def tree(lst):
	# 树状图输出列表
	l = len(lst)
	if l == 0:
		print('-' * 3)
	else:
		for i, j in enumerate(lst):
			if i != 0:
				f.write(tabs[0])
				print(tabs[0], end='')
			if l == 1:
				s = '=' * 3
			elif i == 0:
				s = '┬' + '-' * 2
			elif i + 1 == l:
				s = '└' + '─' * 2
			else:
				s = '├' + '─' * 2
			f.write(s)
			print(s, end='')
			if isinstance(j, list) or isinstance(j, tuple):
				if i + 1 == l:
					tabs[0] += blank[0] * 3
				else:
					tabs[0] += '│' + blank[0] * 2
				tree(j)
			else:
				print(name[j])
				f.write(name[j] + "\n")
	tabs[0] = tabs[0][:-3]
	
def traversalTree(v):

	global visited
	if v < n:
		return [v]
	visited[v] = 1
	items = []
	for i in Tree[v]:
		if visited[i[0]] == 0:
			items += traversalTree(i[0])

	return [items]	
	
def outPut():
	global visited
	global tabs
	global blank
	
	blank = [
			chr(183)]  ##此处为空格格式;Windows控制台下可改为chr(12288) ;linux系统中可改为chr(32)【chr(32)==' ' ;chr(183)=='·' ;chr(12288)=='　'】
	tabs = ['']	
	visited = [0 for i in range(maxn)]
	TreeList = traversalTree(maxn-1)
	#print(Tree)
	tree(TreeList)
###########################

if __name__ == '__main__':
	
	f = open("output","w")
	
	INF = 999999
	dataset = open(dirname(__file__)+'230genes_log_expression.txt').read().strip().split('\n')
	
	[points,name] = InputData(dataset)
		
	DMatrix = PearsonCorrelationDistance(points)
	
	HierarchicalClustering(DMatrix)
	
	outPut()