'''
Code Challenge: Solve the Global Alignment Problem.
	 Input: Two protein strings written in the single-letter amino acid alphabet.
	 Output: The maximum alignment score of these strings followed by an alignment achieving this maximum score. Use the
	BLOSUM62 scoring matrix for matches and mismatches as well as the indel penalty σ = 5.
----------
Sample Input:
PLEASANTLY
MEANLY
----------
Sample Output:
8
PLEASANTLY
-MEA--N-LY
----------
@ Lo Kowngho  2018.9
'''
import numpy
from os.path import dirname

def Grade(Symb1,Symb2):
	Indx1 = symbolList[Symb1]
	Indx2 = symbolList[Symb2]
	return matrix[Indx1][Indx2]
	
def Init_Graph_Global(l1,l2):
	Graph = numpy.zeros([l2,l1])
	for x in range(1,l2):
		Graph[x][0] = Graph[x-1][0]-5
	for y in range(1,l1):
		Graph[0][y] = Graph[0][y-1]-5
	return Graph
		
def Init_Path(l1,l2):
	Path = numpy.zeros([l2,l1])
	for x in range(1,l2):
		Path[x][0] = 1
	for y in range(1,l1):
		Path[0][y] = 2
	return Path

def buildGlobalAlignmentGraph(text1,text2):
	
	l1 = len(text1)
	l2 = len(text2)
	Graph = Init_Graph_Global(l1, l2)
	Path = Init_Path(l1, l2)
		
	for x in range(1,l2):
		for y in range(1,l1):
			Graph[x][y] = max(Graph[x-1][y]-5, Graph[x][y-1]-5, Graph[x-1][y-1]+Grade(text1[y],text2[x]))
			if Graph[x-1][y]-5==Graph[x][y]:
				Path[x][y]=1
			elif Graph[x][y-1]-5==Graph[x][y]:
				Path[x][y]=2
			else:
				Path[x][y]=3
	return [Graph,Path]
	
	
def OutputGlobalAligement(Path,Graph,text1,text2):
	outT1 = ''
	outT2 = ''
	l1 = len(text1)
	l2 = len(text2)
	x = l2-1
	y = l1-1
	while(x!=0 or y!=0):
		if Path[x][y]==1:
			outT1 += '-'
			outT2 += text2[x]
			x -= 1			
		elif Path[x][y]==2:
			outT1 += text1[y]
			outT2 += '-'
			y -= 1
		else:
			outT1 += text1[y]
			outT2 += text2[x]
			x -= 1
			y -= 1
	return [outT1[::-1],outT2[::-1]]	
	
def ImportScoreMatrix():
	dataset = open(dirname(__file__)+'BLOSUM62.txt').read().strip().split('\n')
	symbolList = dataset[0].split()
	for i in range(len(symbolList)):
		symbolList[i]=[symbolList[i],i]
	symbolList = dict(symbolList)
	print(symbolList)
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
	
	[Graph,Path] = buildGlobalAlignmentGraph(text1, text2)
	
	[outT1,outT2] = OutputGlobalAligement(Path,Graph,text1,text2)
	
	print(int(Graph[-1][-1]))
	print(outT1)
	print(outT2)