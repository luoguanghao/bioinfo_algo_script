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
	#print('tag=',tag)
	for i in range(n,maxn):
		tag[i]=1
		#print('#',Graph[i])
		IDson = findTag(i,0)
		IDdaughter = findTag(i,IDson+1)
		#print(Graph[i])
		#print(i,tag,'son =',IDson,'dau = ',IDdaughter)
		#input()
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

def Recursive(v):
	
	tag[v] = 1
	if visited[v] == 1: 
		return Scores[v]
	idx = 0
	for i in range(len(Graph[v])):
		if tag[Graph[v][i]] == 0:
			sonScores = Recursive(Graph[v][i])
			
			for j in range(l):
				for a in range(4):
					minSonVal = INF
					minSonId = -1
					for b in range(4):
						tmp=sonScores[j][b]+delta(a,b)
						if tmp<minSonVal:
							minSonVal = tmp
							minSonId = b
					Scores[v][j][a] += minSonVal
	return Scores[v]


def newSmallParsimony(stringList):

	global tag
	global Scores
	Scores = copy.deepcopy(Origin_Scores)
	tag = [0 for i in range(maxn)]
	for i in range(n): # Initialize the Score
		for j in range(l):
			Id = Base[stringList[i][j]]
			for a in range(4):
				if a != Id:
					Scores[i][j][a] = INF
	Recursive(maxn-1)

def findFootPrint(i):
	for j in range(len(Graph[i])):
		if footprint[Graph[i][j]]==1:
			return Graph[i][j]

def newTrackBack(stringList):

	queue = [] # 队列 层序遍历用
	
	global footprint
	tag = copy.deepcopy(visited)
	footprint = [0 for i in range(maxn)]
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
	
	queue = Graph[maxn-1]
	while(len(queue)):	
		#print('queue =',queue)
		v = queue.pop()
		if visited[v]==1:
			continue
		footprint[v] = 1
		parent = -1
		for i in Graph[v]:
			if footprint[i]==0:
				queue = [i]+queue
			else:
				parent = i
		for j in range(l):
			minVal = INF
			minId = -1
			for a in range(4):
				if Scores[v][j][a]<minVal:
					minVal = Scores[v][j][a]
					minId = a
			if Scores[v][j][Base[stringList[parent][j]]]==minVal:
				stringList[v] += stringList[parent][j]
			else:
				stringList[v] += traBase[minId]	
	return stringList
	
			
def SmallParsimonyUnrootedTree(neiborGraph,edge):
	global Graph
	stringList = copy.deepcopy(Origin_stringList)
	Graph = copy.deepcopy(neiborGraph)
	#edge = [maxn-2,maxn-3]
	# add a root
	Graph[maxn-1].append(edge[0])
	Graph[maxn-1].append(edge[1])

	Graph[edge[0]].append(maxn-1)
	Graph[edge[1]].append(maxn-1)
	Graph[edge[0]].remove(edge[1])
	Graph[edge[1]].remove(edge[0])
	'''print('#')
	for i in range(len(Graph)):
		print(i,Graph[i])
	print('#')'''
	#
	newSmallParsimony(stringList)

	outSL = newTrackBack(stringList)
	#print(outSL)
	Graph[edge[0]].remove(maxn-1)
	Graph[edge[1]].remove(maxn-1)
	Graph[edge[0]].append(edge[1])
	Graph[edge[1]].append(edge[0])
	Graph[maxn-1] = []
	#print(stringList)
	cnt=0
	
	for i in Scores[-1]:
		cnt += min(i)
	'''print(cnt)
	c=0
	for i in range(maxn-1):
		for j in Graph[i]:
			#print(i,j)
			#print('$',stringList[6])
			dist = HMDist(stringList[i], stringList[j])
			c += dist
			print("%s->%s:%d"%(stringList[i],stringList[j],dist))
	#print(c)
	'''
	return [cnt,Graph,outSL]

def nearestNeighborsExchange(Origin_Graph,en):

	NeighborGraph1 = copy.deepcopy(Origin_Graph[:])	
	candidate1 = NeighborGraph1[en[0]]
	candidate2 = NeighborGraph1[en[1]]
	candidate1.remove(en[1])
	candidate2.remove(en[0])
	NeighborGraph1[candidate1[0]].remove(en[0])
	NeighborGraph1[candidate1[1]].remove(en[0])
	NeighborGraph1[candidate2[0]].remove(en[1])
	NeighborGraph1[candidate2[1]].remove(en[1])
	NeighborGraph2 = copy.deepcopy(NeighborGraph1[:])
	
	#print(candidate1,candidate2)
	NeighborGraph1[en[0]]=[candidate1[0],candidate2[0],en[1]]
	NeighborGraph1[candidate1[0]].append(en[0])
	NeighborGraph1[candidate2[0]].append(en[0])
	
	NeighborGraph1[en[1]]=[candidate1[1],candidate2[1],en[0]]
	NeighborGraph1[candidate1[1]].append(en[1])
	NeighborGraph1[candidate2[1]].append(en[1])


	NeighborGraph2[en[0]]=[candidate1[0],candidate2[1],en[1]]
	NeighborGraph2[candidate1[0]].append(en[0])
	NeighborGraph2[candidate2[1]].append(en[0])
	
	NeighborGraph2[en[1]]=[candidate1[1],candidate2[0],en[0]]
	NeighborGraph2[candidate1[1]].append(en[1])
	NeighborGraph2[candidate2[0]].append(en[1])

	[s1,t1,sl1]=SmallParsimonyUnrootedTree(NeighborGraph1,en)
	[s2,t2,sl2]=SmallParsimonyUnrootedTree(NeighborGraph2,en)
	if s1<s2:
		return [s1,t1,sl1]
	else:
		return [s2,t2,sl2]


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
	Origin_Scores = [np.zeros(shape=(l,4),dtype=int) for i in range(maxn)]
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
	#print('#',in_edge)
	#print('maxn =',maxn)
	#

	#[NeighborGraph1,NeighborGraph2] = nearestNeighborsExchange(Origin_Graph,[6,7])
	#for i in range(len(NeighborGraph1)):
	#	print(i,NeighborGraph1[i])
	#[s1,t1]=SmallParsimonyUnrootedTree(NeighborGraph1,[6,7])
	#[s2,t2]=SmallParsimonyUnrootedTree(NeighborGraph2,[6,7])
	#print(s1,s2)

	
	[NewSc,NewTree,NewStrList] = SmallParsimonyUnrootedTree(Origin_Graph,in_edge[0])
	Sc = INF
	print('#',NewSc)
	#print('$$',NewStrList)
	while NewSc < Sc:
		#print('inedge',in_edge)
		Sc = NewSc
		Tree = NewTree
		SList = NewStrList

		for edge in in_edge:
			#print(edge)
			[neighborSc,neighborTree,NewStrList] = nearestNeighborsExchange(Tree, edge)
			#print(neighborSc)
			if neighborSc<NewSc:
				NewSc = neighborSc
				NewTree = neighborTree
		# renew the in_edge!!
		in_edge.clear()		
		for i in range(n,maxn-1):
			for j in NewTree[i]:
				if visited[j]==0:
					try:
						in_edge.index([j,i])
					except ValueError:
						in_edge.append([i,j])
		print(Sc)
		#print(NewStrList)
		cnt=0
		for i in range(maxn-1):
			for j in Graph[i]:
				dist = HMDist(NewStrList[i], NewStrList[j])
				print("%s->%s:%d"%(NewStrList[i],NewStrList[j],dist))
				cnt+=1
		print('')

		