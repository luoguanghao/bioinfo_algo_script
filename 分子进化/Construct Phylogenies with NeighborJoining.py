import numpy as np
from os.path import dirname

def Get_totalDist_and_NJMatrix(ptr,n):
	totalDist = [0 for i in range(ptr)]
	for i in range(ptr):
		if delete[i]==False:
			for j in range(ptr):
				if delete[j]==False:
					totalDist[i] += matrix[i][j]
	NJMatrix = np.zeros(shape=(ptr,ptr))
	for x in range(ptr):
		for y in range(ptr):
			if x!=y and delete[x]==False and delete[y]==False:
				NJMatrix[x][y]=(n-2)*matrix[x][y]-totalDist[x]-totalDist[y]
	return [NJMatrix,totalDist]

def locateMin(NJMatrix,ptr):
	minVal = 999999
	minX = minY = -1
	for x in range(ptr):
		for y in range(ptr):
			if delete[x]==False and delete[y]==False and x!=y and NJMatrix[x][y]<minVal:
				minVal = NJMatrix[x][y]
				minX = x
				minY = y
	return [[minX,minY],minVal]

def NeighborJoining(n,ptr):
	global matrix
	global Tree
	global delete
	if n==2:
		for i in range(maxn):
			for j in range(maxn):
				if i!=j and delete[i]==False and delete[j]==False:
					Tree[i].append([j,matrix[i][j]])
		return 
		
	[NJMatrix,totalDist] = Get_totalDist_and_NJMatrix(ptr,n)
	[[minX,minY],minVal] = locateMin(NJMatrix,ptr)
	delta = (totalDist[minX]-totalDist[minY]) / (n-2)
	limbLengthX = (matrix[minX][minY]+delta) / 2
	limbLengthY = (matrix[minX][minY]-delta) / 2
	delete[minX] = delete[minY]=True

	for i in range(ptr):
		if delete[i]==False:
			tmp = (matrix[i][minX]+matrix[i][minY]-matrix[minX][minY])/2
			matrix[ptr][i] = matrix[i][ptr] = tmp
	
	NeighborJoining(n-1,ptr+1)

	Tree[ptr].append([minX,limbLengthX])
	Tree[ptr].append([minY,limbLengthY])
	Tree[minX].append([ptr,limbLengthX])
	Tree[minY].append([ptr,limbLengthY])

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	n = int(dataset[0])
	dataset = dataset[1:]
	maxn = 2*n-2
	matrix = np.zeros(shape=(maxn,maxn))
	for i in range(len(dataset)):
		matrix[i][:n] = list(map(float,dataset[i].split()))

	Tree = [[]for i in range(maxn)]
	delete = [False for i in range(maxn)]
	
	NeighborJoining(n,n)
	
	for i in range(len(Tree)):
		for j in range(len(Tree[i])):
			print("%d->%d:%.3f"%(i,Tree[i][j][0],Tree[i][j][1]))