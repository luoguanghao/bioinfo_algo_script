from os.path import dirname
import numpy as np



if __name__ == '__main__':	
	Base = {'A':0,'T':1,'G':2,'C':3}
	traBase = {0:'A',1:'T',2:'G',3:'C'}
	INF = 999999
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	n = int(dataset[0])
	l = len(dataset[1])
	dataset = dataset[2:]

	maxn = 2*n - 1
	# build the Tree
	Origin_stringList = ['' for i in range(maxn)]
	Origin_Scores = [np.ones(shape=(l,4),dtype=int)*INF for i in range(maxn)]
	Origin_Graph = [[] for i in range(maxn)]
	visited = [0 for i in range(maxn)]
	idx = 0
	for line in dataset:
		if line.split('->')[0][0]<='Z' and line.split('->')[0][0]>='A':	
			Origin_stringList[idx]=line.split('->')[0]
			Origin_Graph[idx].append(int(line.split('->')[1]))
			Origin_Graph[int(line.split('->')[1])].append(idx)
			visited[idx] = 1
			idx += 1
		elif line.split('->')[1][0]<='Z' and line.split('->')[1][0]>='A':
			continue
		else:
			Origin_Graph[int(line.split('->')[0])].append(int(line.split('->')[1]))			
	#
	# find all internal edge
	in_edge = []
	for i in Origin_Graph:
		print(i)
	for i in range(n,maxn-1):
		for j in Origin_Graph[i]:
			if visited[j]==0:
				try:
					in_edge.index([j,i])
				except ValueError:
					in_edge.append([i,j])
	print('#',in_edge)
	print('maxn =',maxn)
	#