import numpy as np
from os.path import dirname
import copy


def delta(a,b):
	if a==b:
		return 0
	else:
		return 1
		
def HMDist(a,b):
	cnt = 0
	for i in range(len(a)):
		cnt += delta(a[i], b[i])
	return cnt

def findTag(i,v):
	for j in range(v,len(Graph[i])):
		if tag[Graph[i][j]]==1:
			return j

def SmallParsimony():
	global stringList
	global tag
	global Scores
	stringList = copy.deepcopy(Origin_stringList)
	Scores = copy.deepcopy(Origin_Scores)
	tag = copy.deepcopy(visited)
	for i in range(n):
		for j in range(l):
			Id = Base[stringList[i][j]]
			for a in range(4):
				if a==Id:
					Scores[i][j][a]=0
	print('tag=',tag)
	for i in range(n,maxn):
		tag[i]=1
		#print('#',Graph[i])
		IDson = findTag(i,0)
		IDdaughter = findTag(i,IDson+1)
		#print(Graph[i][IDson],Graph[i][IDdaughter])
		son = Scores[Graph[i][IDson]]
		daughter = Scores[Graph[i][IDdaughter]]
		delt = 0
		for j in range(l):
			minVal = INF
			minId = -1
			for a in range(4):
				minDVal = INF
				minDId = -1
				minSVal = INF
				minSId = -1
				for b in range(4):
					tmp=daughter[j][b]+delta(a,b)
					if tmp<minDVal:
						minDVal=tmp
						minDId=b
					tmp = son[j][b]+delta(a,b)
					if tmp<minSVal:
						minSVal=tmp
						minSId=b
				Scores[i][j][a] = minSVal+minDVal
				if Scores[i][j][a]<minVal:
					minVal = Scores[i][j][a]
					minId = a
			#stringList[i] += traBase[minId]
			'''
			if minVal==Scores[i][j][Base[stringList[IDson][j]]]:
				stringList[i] += stringList[IDson][j]
			else:
				stringList[i] += traBase[minId]
			'''
			
def findFootPrint(i):
	for j in range(len(Graph[i])):
		if footprint[Graph[i][j]]==1:
			return Graph[i][j]
	
def trackBack():
	global footprint
	tag = copy.deepcopy(visited)
	footprint = [0 for i in range(maxn)]
	#
	for i in Graph:
		print(i)
	#
	#print(Scores[-1])
	
	for j in range(l):
		minVal = INF
		minId = -1
		for a in range(4):
			if Scores[maxn-1][j][a] < minVal:
				minVal = Scores[maxn-1][j][a]
				minId = a
		stringList[maxn-1] += traBase[minId]
	#print(stringList[maxn-1])
	footprint[maxn-1]=1
	print(footprint)
	for i in range(maxn-2,n-1,-1):
		IDpatent=findFootPrint(i)
		footprint[i] = 1
		print(IDpatent)
		#a=input()
		for j in range(l):
			minVal = INF
			minId = -1
			for a in range(4):
				if Scores[i][j][a] < minVal:
					minVal = Scores[i][j][a]
					minId = a
			
			if i!=(maxn-1):
				if Scores[i][j][Base[stringList[IDpatent][j]]]==minVal:
					stringList[i] += stringList[IDpatent][j]
				else:
					stringList[i] += traBase[minId]
			else:
				stringList[i] += traBase[minId]
			
def SmallParsimonyUnrootedTree(edge):
	global Graph
	
	Graph = copy.deepcopy(Origin_Graph)
	#edge = [maxn-2,maxn-3]
	# add a root
	Graph[maxn-1].append(edge[0])
	Graph[maxn-1].append(edge[1])
	Graph[edge[0]].append(maxn-1)
	Graph[edge[1]].append(maxn-1)
	Graph[edge[0]].remove(edge[1])
	Graph[edge[1]].remove(edge[0])

	#
	SmallParsimony()
	trackBack()
	Graph[edge[0]].remove(maxn-1)
	Graph[edge[1]].remove(maxn-1)
	Graph[edge[0]].append(edge[1])
	Graph[edge[1]].append(edge[0])

	#print(stringList)
	cnt=0
	
	for i in Scores[-1]:
		cnt += min(i)
	print(cnt)
	c=0
	for i in range(maxn-1):
		for j in Graph[i]:
			#print(i,j)
			dist = HMDist(stringList[i], stringList[j])
			c += dist
			print("%s->%s:%d"%(stringList[i],stringList[j],dist))
	#print(c)



if __name__ == '__main__':
	
	Base = {'A':0,'T':1,'G':2,'C':3}
	traBase = {0:'A',1:'T',2:'G',3:'C'}
	INF = 999999
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	n = int(dataset[0])
	l = len(dataset[1])
	maxn = 2*n - 1
	# build the Tree
	Origin_stringList = ['' for i in range(maxn)]
	Origin_Scores = [np.ones(shape=(l,4),dtype=int)*INF for i in range(maxn)]
	Origin_Graph = [[] for i in range(maxn)]
	visited = [0 for i in range(maxn)]
	dataset = dataset[2:]
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
	
	
	
	SmallParsimonyUnrootedTree([maxn-2,maxn-3])
	'''
	for i in Graph:
		print(i)
		'''	
	