'''
GO BACK SEE
'''
from os.path import dirname
import numpy as np

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

def SmallParsimony():
	global stringList
	global Scores
	global Graph
	tag = [0 for i in range(maxn)]
	visited = n
	for i in range(maxn):
		if(i<n):
			tag[i]=1
			for j in range(l):
				Id = Base[stringList[i][j]]
				for a in range(4):
					if a==Id:
						Scores[i][j][a]=0

	for i in range(n,maxn):
		daughter = Scores[Graph[i][0]]
		son = Scores[Graph[i][1]]
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

def trackBack(): # why???
	for i in range(maxn-1,n-1,-1):
		for j in range(l):
			minVal = INF
			minId = -1
			for a in range(4):
				if Scores[i][j][a] < minVal:
					minVal = Scores[i][j][a]
					minId = a
			if i!=(maxn-1):
				if Scores[i][j][Base[stringList[Up[i]][j]]]==minVal:
					stringList[i] += stringList[Up[i]][j]
				else:
					stringList[i] += traBase[minId]
			else:
				stringList[i] += traBase[minId]

if __name__ == '__main__':
	edge = [4,5]
	Base = {'A':0,'T':1,'G':2,'C':3}
	traBase = {0:'A',1:'T',2:'G',3:'C'}
	INF = 999999
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	n = int(dataset[0])
	maxn = 2*n-1
	dataset = dataset[1:]
	stringList = ['' for i in range(maxn)]
	Scores = []
	Graph = [[] for i in range(maxn)]
	Up = [0 for i in range(maxn)]
	l = 0
	#build Graph
	for i in range(1,2*n,2):
		if i == 1:
			l = len(dataset[i].split('->')[1])
			Scores = [np.ones(shape=(l,4),dtype=int)*INF for i in range(maxn)]
			stringList[i//2]=dataset[i].split('->')[1]
			Graph[int(dataset[i].split('->')[0])].append(i//2)
			Up[i//2] = int(dataset[i].split('->')[0])
		else:
			#print(dataset[i].split('->')[1])
			stringList[i//2]=dataset[i].split('->')[1]
			Graph[int(dataset[i].split('->')[0])].append(i//2)
			Up[i//2] = int(dataset[i].split('->')[0])
	for i in range(2*n+1,len(dataset)-2,2):
		Graph[int(dataset[i].split('->')[0])].append(int(dataset[i].split('->')[1]))
		Up[int(dataset[i].split('->')[1])] = int(dataset[i].split('->')[0])
	#
	# add a root
	Graph[maxn-1].append(edge[0])
	Graph[maxn-1].append(edge[1])
	Up[edge[0]] = (maxn-1)
	Up[edge[1]] = (maxn-1)
	#
	SmallParsimony()
	trackBack()
	Graph[edge[0]].append(edge[1])
	Up[edge[0]] = edge[1]
	Up[edge[1]] = edge[0]
	cnt=0
	for i in Scores[-1]:
		cnt += min(i)
	'''
	
	print(stringList)
	for i in range(maxn):
		print(i,Graph[i])
	'''
	print(cnt)
	'''
	for i in range(maxn-1):
		for j in Graph[i]:
			dist = HMDist(stringList[i], stringList[j])
			print("%s->%s:%d"%(stringList[i],stringList[j],dist))
			print("%s->%s:%d"%(stringList[j],stringList[i],dist))
			
'''