'''
Code Challenge: Solve the Alignment with Affine Gap Penalties Problem.
   >>Input: Two amino acid strings v and w (each of length at most 100).
   >>Output: The maximum alignment score between v and w, followed by an alignment of v and w achieving this maximum score. Use the
     BLOSUM62 scoring matrix, a gap opening penalty of 11, and a gap extension penalty of 1.
---------------------
Sample Input:
PRTEINS
PRTWPSEIN
---------------------
Sample Output:
8
PRT---EINS
PRTWPSEIN-
---------------------
coder: Lo Kwongho
'''
import numpy
from os.path import dirname
negINFINITY = -999
#Penalties
gs = -10 #gap_Start
ge = -1  #gap_Extend
#
def Grade(Symb1,Symb2):
	Indx1 = symbolList[Symb1]
	Indx2 = symbolList[Symb2]
	return matrix[Indx1][Indx2]

def initGraph(l1,l2):
	Graph = [numpy.zeros([l1,l2]	,dtype=int) for i in range(3)]

	Graph[1][0][0] = negINFINITY
	Graph[2][0][0] = negINFINITY
	for x in range(1,l1):
		Graph[0][x][0]=negINFINITY
		if x==1:
			Graph[1][x][0]=ge+gs
		else:
			Graph[1][x][0]=Graph[1][x-1][0]+ge
		Graph[2][x][0]=negINFINITY
	for y in range(1,l2):
		Graph[0][0][y]=negINFINITY
		if y ==1:
			Graph[2][0][y]=ge+gs
		else:
			Graph[2][0][y]=Graph[2][0][y-1]+ge
		Graph[1][0][y]=negINFINITY
	return Graph
	
def Init_Path(l1,l2):
	Path = [numpy.ones([l1,l2])*-1 for i in range(3)]
	'''for x in range(1,l1):
		Path[x][0] = 1
	for y in range(1,l2):
		Path[0][y] = 2'''
	return Path
	
def buildAlignmentGraph(text1,text2,l1,l2):

	Graph = initGraph(l1,l2)
	#Path = #Init_Path(l1,l2)
	for x in range(1,l1):
		for y in range(1,l2):				
			# X ######
			Graph[1][x][y]=max(gs+ge+Graph[0][x-1][y],gs+ge+Graph[2][x-1][y],ge+Graph[1][x-1][y])

				
			# Y ###### 
			Graph[2][x][y]=max(gs+ge+Graph[0][x][y-1],gs+ge+Graph[1][x][y-1],ge+Graph[2][x][y-1])

			# M ######
			Graph[0][x][y]=Grade(text1[x], text2[y])+max(Graph[0][x-1][y-1],Graph[1][x-1][y-1],Graph[2][x-1][y-1])

	maxVal = 0
	maxIndx = -1
	for i in range(3):
		if Graph[i][l1-1][l2-1]>maxVal:
			maxVal=Graph[i][l1-1][l2-1]
			maxIndx=i
	return [Graph,maxIndx,maxVal]

def trackBack(Graph,maxIndx,text1,text2):
	x = len(text1)-1
	y = len(text2)-1
	otext1 = ''
	otext2 = ''
	Indx = maxIndx
	while(1):
		if Indx==0:
			otext1 += text1[x]
			otext2 += text2[y]
			if x ==1:
				break
			if Graph[0][x][y]==Graph[1][x-1][y-1]+Grade(text1[x], text2[y]):
				Indx = 1
			elif Graph[0][x][y]==Graph[2][x-1][y-1]+Grade(text1[x], text2[y]):
				Indx = 2
			else:
				Indx = 0
			x -= 1
			y -= 1
		elif Indx==1:
			otext1 += text1[x]
			otext2 += '-'
			if x == 1:
				break
			if Graph[1][x][y]==Graph[0][x-1][y]+ge+gs:
				Indx = 0
			elif Graph[1][x][y]==Graph[2][x-1][y]+ge+gs:
				Indx = 2
			else:
				Indx = 1
			x -= 1
		else:
			otext1 += '-'
			otext2 += text2[y]
			if y == 1:
				break
			if Graph[2][x][y]==Graph[0][x][y-1]+ge+gs:
				Indx = 0
			elif Graph[2][x][y]==Graph[1][x][y-1]+ge+gs:
				Indx = 1
			else:
				Indx = 2
			y -= 1
				
	return [otext1[::-1],otext2[::-1]]
		
def ImportScoreMatrix():
	dataset = open(dirname(__file__)+'BLOSUM62.txt').read().strip().split('\n')
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
	[matrix,symbolList] = ImportScoreMatrix() # 打分矩阵
	
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
	text1 = '0'+dataset[0]
	text2 = '0'+dataset[1]
	l1 = len(text1)
	l2 = len(text2)
	[Graph,maxIndx,maxVal] = buildAlignmentGraph(text1, text2, l1, l2)
	#print(Graph)
	
	[output_text1,output_text2] = trackBack(Graph,maxIndx,text1,text2)
	print(maxVal)
	print(output_text1)
	print(output_text2)
	