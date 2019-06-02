'''
Code Challenge: Implement SmallParsimony to solve the Small Parsimony Problem.
     Input: An integer n followed by an adjacency list for a rooted binary tree with n leaves labeled by DNA strings.
     Output: The minimum parsimony score of this tree, followed by the adjacency list of a tree corresponding to labeling
     internal nodes by DNA strings in order to minimize the parsimony score of the tree.  You may break ties however you like.

Note: Remember to run SmallParsimony on each individual index of the strings at the leaves of the tree.
------
Sample Input:
4
4->CAAATCCC
4->ATTGCGAC
5->CTGCGCTG
5->ATGGACGA
6->4
6->5
------
Sample Output:
16
ATTGCGAC->ATAGCCAC:2
ATAGACAA->ATAGCCAC:2
ATAGACAA->ATGGACTA:2
ATGGACGA->ATGGACTA:1
CTGCGCTG->ATGGACTA:4
ATGGACTA->CTGCGCTG:4
ATGGACTA->ATGGACGA:1
ATGGACTA->ATAGACAA:2
ATAGCCAC->CAAATCCC:5
ATAGCCAC->ATTGCGAC:2
ATAGCCAC->ATAGACAA:2
CAAATCCC->ATAGCCAC:5
------
Lo Kwongho 2018.9
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
	for i in range(n):
		if i == 1:
			l = len(dataset[i].split('->')[1])
			Scores = [np.ones(shape=(l,4),dtype=int)*INF for i in range(maxn)]
			stringList[i]=dataset[i].split('->')[1]
			Graph[int(dataset[i].split('->')[0])].append(i)
			Up[i] = int(dataset[i].split('->')[0])
		else:
			stringList[i]=dataset[i].split('->')[1]
			Graph[int(dataset[i].split('->')[0])].append(i)
			Up[i] = int(dataset[i].split('->')[0])
	for i in range(n,len(dataset)):
		Graph[int(dataset[i].split('->')[0])].append(int(dataset[i].split('->')[1]))
		Up[int(dataset[i].split('->')[1])] = int(dataset[i].split('->')[0])
	
	SmallParsimony()
	trackBack()
	cnt=0
	for i in Scores[-1]:
		cnt += min(i)

	print(cnt)
	for i in range(maxn):
		for j in Graph[i]:
			dist = HMDist(stringList[i], stringList[j])
			print("%s->%s:%d"%(stringList[i],stringList[j],dist))
			print("%s->%s:%d"%(stringList[j],stringList[i],dist))
