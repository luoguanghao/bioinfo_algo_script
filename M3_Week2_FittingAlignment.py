'''
Fitting Alignment Problem: Construct a highest-scoring fitting alignment between two strings.
   >>Input: Strings v and w as well as a matrix Score.
   >>Output: A highest-scoring fitting alignment of v and w as defined by the scoring matrix Score.
-------------------
Sample Input:
GTAGGCTTAAGGTTA
TAGATA
-------------------
Sample Output:
2
TAGGCTTA
TAGA--TA
-------------------
coder: Lo Kwongho
'''

import numpy
from os.path import dirname

def Init_Graph_Fiting(l1,l2):
	Graph = numpy.zeros([l1,l2])
	for y in range(1,l2):
		Graph[0][y] = Graph[0][y-1]-1
	return Graph
		
def Init_Path(l1,l2):
	Path = numpy.ones([l1,l2])*-1
	for x in range(1,l1):
		Path[x][0] = 1
	for y in range(1,l2):
		Path[0][y] = 2
	return Path

def buildFittingAlignmentGraph(text1,text2):
	l1 = len(text1)
	l2 = len(text2)
	Graph = Init_Graph_Fiting(l1, l2)
	Path = Init_Path(l1,l2)
	for x in range(1,l1):
		for y in range(1,l2):
			if text1[x]==text2[y]:
				Graph[x][y]=max(Graph[x-1][y-1]+1,Graph[x-1][y]-1,Graph[x][y-1]-1)
			else:
				Graph[x][y]=max(Graph[x-1][y-1]-1,Graph[x-1][y]-1,Graph[x][y-1]-1)
			if Graph[x][y]==Graph[x-1][y]-1:
				Path[x][y]=1
			elif Graph[x][y]==Graph[x][y-1]-1:
				Path[x][y]=2
			else:
				Path[x][y]=3
	
	maxVal = 0
	maxIndx = -1
	for i in range(l1):
		if Graph[i][l2-1]>maxVal:
			maxVal=Graph[i][l2-1]
			maxIndx=i
	return [Graph,Path,maxIndx,maxVal]	
	
def OutputFittingAligement(Path,Graph,text1,text2,maxIndx):
	outT1 = ''
	outT2 = ''
	l1 = len(text1)
	l2 = len(text2)
	x = maxIndx
	y = l2-1
	while(y!=0):
		if Path[x][y]==1:
			outT1 += text1[x]
			outT2 += '-'
			x -= 1			
		elif Path[x][y]==2:
			outT1 += '-'
			outT2 += text2[y]
			y -= 1
		elif Path[x][y]==3:
			outT1 += text1[x]
			outT2 += text2[y]
			x -= 1
			y -= 1
		else:
			x=0
			y=0
	return [outT1[::-1],outT2[::-1]]	
		

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
	text1 = '0'+dataset[0]
	text2 = '0'+dataset[1]
	l1 = len(text1)
	l2 = len(text2)
	[Graph,Path,maxIndx,maxVal] = buildFittingAlignmentGraph(text1,text2)
	
	[outText1,outText2]=OutputFittingAligement(Path, Graph, text1, text2, maxIndx)
	#print(Graph)
	print(int(maxVal))
	print(outText1)
	print(outText2)