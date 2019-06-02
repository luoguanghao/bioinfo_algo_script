'''
Code Challenge: Solve the Middle Edge in Linear Space Problem (for protein strings).
     Input: Two amino acid strings.
     Output: A middle edge in the alignment graph in the form "(i, j) (k, l)", where (i, j) connects to (k, l). To compute scores, use the
     BLOSUM62 scoring matrix and a (linear) indel penalty equal to 5.
------------------
Sample Input:
PLEASANTLY
MEASNLY
------------------
Sample Output:
(4, 3) (5, 4)
------------------
coder : Lo Kwongho 2018.9
'''

from os.path import dirname
import numpy
#
indel = -5
#

def Grade(Symb1,Symb2):
	Indx1 = symbolList[Symb1]
	Indx2 = symbolList[Symb2]
	return matrix[Indx1][Indx2]
	
def initGraph(l1,l2):
	Graph = [numpy.zeros([l1,l2],dtype=int) for i in range(2)]
	for x in range(1,l1):
		Graph[0][x][0] = Graph[0][x-1][0] + indel
	for y in range(1,l2):
		Graph[0][0][y] = Graph[0][0][y-1] + indel
	for x in range(l1-2,-1,-1):
		Graph[1][x][0]=Graph[1][x+1][0] +indel
	for y in range(l2-2,-1,-1):
		Graph[1][0][y]=Graph[1][0][y+1] +indel
	return Graph

def middleEdge(text1,text2,l1,l2):
	Graph = initGraph(l1,l2)
	m = int((l2-1)/2)
	for y in range(1,m+1):
		for x in range(1,l1):
			Graph[0][x][y] = max(Graph[0][x-1][y-1]+Grade(text1[x],text2[y]),Graph[0][x-1][y]+indel,Graph[0][x][y-1]+indel)
	
	for y in range(l2-2,m-1,-1):
		for x in range(l1-2,-1,-1):
			Graph[1][x][y]=max(Graph[1][x+1][y+1]+Grade(text1[x+1], text2[y+1]),Graph[1][x+1][y]+indel,Graph[1][x][y+1]+indel)
	maxVal=0
	maxIndx=-1
	for i in range(l1):
		if maxVal<Graph[0][i][m]+Graph[1][i][m]:
			maxVal=Graph[0][i][m]+Graph[1][i][m]
			maxIndx=i
	#track back the orientation
	path = -1  
	if Graph[1][maxIndx][m]==Graph[1][maxIndx+1][m]+indel:
		path=1
	elif Graph[1][maxIndx][m]==Graph[1][maxIndx][m+1]+indel:
		path=2
	else:
		path=0
		# print the graph
	for g in Graph:
		print(g)
		#print the edge
	print(maxIndx)
	if path == 1:
		print('(%d, %d) (%d, %d)'%(maxIndx,m,maxIndx+1,m))
	elif path == 2:
		print('(%d, %d) (%d, %d)'%(maxIndx,m,maxIndx,m+1))
	else:
		print('(%d, %d) (%d, %d)'%(maxIndx,m,maxIndx+1,m+1))
		
		
def ImportScoreMatrix():
	dataset = open(dirname(__file__)+'BLOSUM62.txt').read().strip().split('\n')
	symbolList = dataset[0].split()
	for i in range(len(symbolList)):
		symbolList[i]=[symbolList[i],i]
	symbolList = dict(symbolList)
	#print(symbolList)
	matrix = []
	for i in range(1,len(dataset)):
		matrix.append(dataset[i].split()[1:])
	for l in range(len(matrix)):
		for i in range(len(matrix[l])):
			matrix[l][i]=int(matrix[l][i])
	return [matrix,symbolList]

if __name__ == '__main__':
	[matrix,symbolList] = ImportScoreMatrix()
	
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
	text1 = '0'+dataset[0]
	text2 = '0'+dataset[1]
	l1 = len(text1) # X
	l2 = len(text2) # Y
	middleEdge(text1,text2,l1,l2)
	