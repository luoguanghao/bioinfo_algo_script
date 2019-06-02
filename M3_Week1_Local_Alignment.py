'''
Code Challenge: Solve the Local Alignment Problem.
     Input: Two protein strings written in the single-letter amino acid alphabet.
     Output: The maximum score of a local alignment of the strings, followed by a local alignment of these strings achieving the maximum
     score. Use the PAM250 scoring matrix for matches and mismatches as well as the indel penalty σ = 5.
---------------
Sample Input:
MEANLY
PENALTY
---------------
Sample Output:
15
EANL-Y
ENALTY
---------------
Lo Kwongho 2018.9
'''
import numpy
from os.path import dirname

def Grade(Symb1,Symb2):
	Indx1 = symbolList[Symb1]
	Indx2 = symbolList[Symb2]
	return matrix[Indx1][Indx2]

def Init_Graph_Local(l1,l2):
	Graph = numpy.zeros([l1,l2])
	return Graph
		
def Init_Path(l1,l2):
	Path = numpy.ones([l1,l2])*-1
	for x in range(1,l1):
		Path[x][0] = 1
	for y in range(1,l2):
		Path[0][y] = 2
	return Path

def buildLocalAlignmentGraph(text1,text2):
	l1 = len(text1)
	l2 = len(text2)
	Graph = Init_Graph_Local(l1, l2)
	Path = Init_Path(l1, l2)
	
	for x in range(1,l1):
		for y in range(1,l2):
			Graph[x][y] = max(Graph[x-1][y]-5, Graph[x][y-1]-5, Graph[x-1][y-1]+Grade(text1[x],text2[y]),0)
			if Graph[x-1][y]-5 == Graph[x][y]:
				Path[x][y] = 1
			elif Graph[x][y-1]-5==Graph[x][y]:
				Path[x][y] = 2
			elif Graph[x][y] == 0:
				Path[x][y] = 0
			else:
				Path[x][y] = 3
	maxVal = 0
	maxIndx = [-1,-1]
	for x in range(1,l1):
		for y in range(1,l2):
			if Graph[x][y]>maxVal:
				maxVal=Graph[x][y]
				maxIndx=[x,y]
				
	return [Graph,Path,maxIndx]

def OutputLocalAligement(Path,Graph,text1,text2,maxIndx):
	outT1 = ''
	outT2 = ''
	l1 = len(text1)
	l2 = len(text2)
	x = maxIndx[0]
	y = maxIndx[1]
	while(x!=0 or y!=0):
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


def ImportScoreMatrix():
	dataset = open(dirname(__file__)+'PAM250.txt').read().strip().split('\n')
	symbolList = dataset[0].split()
	for i in range(len(symbolList)):
		symbolList[i]=[symbolList[i],i]
	symbolList = dict(symbolList)
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
	
	[Graph,Path,maxIndx] = buildLocalAlignmentGraph(text1,text2)
	
	[outT1,outT2]=OutputLocalAligement(Path,Graph,text1,text2,maxIndx)
	print(int(Graph[maxIndx[0]][maxIndx[1]]))
	print(outT1)
	print(outT2)