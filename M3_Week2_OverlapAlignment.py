'''
Code Challenge: Solve the Overlap Alignment Problem.
   >>Input: Two strings v and w, each of length at most 1000.
   >>Output: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v' of v and a prefix w' of w.
	achieving this maximum score. Use an alignment score in which matches count +1 and both the mismatch and indel penalties are 2.
-------------------
Sample Input:
PAWHEAE
HEAGAWGHEE
-------------------
Sample Output:
1
HEAE
HEAG
-------------------
coder: Lo Kwongho
'''

import numpy
from os.path import dirname

def Init_Graph_Overlap(l1,l2):
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

def buildOverlapAlignmentGraph(text1,text2):
	l1 = len(text1)
	l2 = len(text2)
	Graph = Init_Graph_Overlap(l1, l2)
	Path = Init_Path(l1,l2)
	for x in range(1,l1):
		for y in range(1,l2):
			if text1[x]==text2[y]:
				Graph[x][y]=max(Graph[x-1][y-1]+1,Graph[x-1][y]-2,Graph[x][y-1]-2)
			else:
				Graph[x][y]=max(Graph[x-1][y-1]-2,Graph[x-1][y]-2,Graph[x][y-1]-2)
			if Graph[x][y]==Graph[x-1][y]-2:
				Path[x][y]=1
			elif Graph[x][y]==Graph[x][y-1]-2:
				Path[x][y]=2
			else:
				Path[x][y]=3
		
	maxVal = 0
	maxIndx = -1
	for i in range(l2):
		if Graph[l1-1][i]>maxVal:
			maxVal=Graph[l1-1][i]
			maxIndx=i
					
	return [Graph,Path,maxIndx,maxVal]	
	
def OutputOverlapAligement(Path,Graph,text1,text2,maxIndx):
	outT1 = ''
	outT2 = ''
	l1 = len(text1)
	l2 = len(text2)
	x = l1-1
	y = maxIndx
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
	[Graph,Path,maxIndx,maxVal] = buildOverlapAlignmentGraph(text1,text2)
	#print(Graph)
		
	[outText1,outText2]=OutputOverlapAligement(Path, Graph, text1, text2, maxIndx)

	print(int(maxVal))
	print(outText1)
	print(outText2)