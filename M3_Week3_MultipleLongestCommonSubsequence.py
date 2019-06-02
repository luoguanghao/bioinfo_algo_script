'''
Code Challenge: Solve the Multiple Longest Common Subsequence Problem.
   >>Input: Three DNA strings of length at most 10.
   >>Output: The length of a longest common subsequence of these three strings, followed by a multiple alignment of the three strings
     corresponding to such an alignment.
-----------
Sample Input:
ATATCCG
TCCGA
ATGTACTG
-----------
Sample Output:
3
ATATCC-G-
---TCC-GA
ATGTACTG-
-----------
coder : Lo Kwongho 2018.9
'''

from os.path import dirname
import numpy

def initGraph():
	Graph = numpy.zeros([l1,l2,l3],dtype=int)
	return Graph
	
def initPath():
	Path = numpy.ones([l1,l2,l3],dtype=int) * -1
	
	return Path
	
def multipleAlignment():
	otext1 = ''
	otext2 = ''
	otext3 = ''
	Graph = initGraph()
	path = initPath()
	for x in range(1,l1):
		for y in range(1,l2):
			for z in range(1,l3):
				if text1[x]==text2[y]==text3[z]:
					Graph[x][y][z]=max(Graph[x-1][y-1][z-1]+1,
										Graph[x][y-1][z-1],
										Graph[x][y][z-1],
										Graph[x][y-1][z],
										Graph[x-1][y][z-1],
										Graph[x-1][y-1][z],
										Graph[x-1][y][z])
				else:
					Graph[x][y][z]=max(Graph[x-1][y-1][z-1],
										Graph[x][y-1][z-1],
										Graph[x][y][z-1],
										Graph[x][y-1][z],
										Graph[x-1][y][z-1],
										Graph[x-1][y-1][z],
										Graph[x-1][y][z])
					
				if Graph[x][y][z]==Graph[x][y-1][z-1]:
					path[x][y][z] = 1
				elif Graph[x][y][z]==Graph[x-1][y][z-1]:
					path[x][y][z] = 2
				elif Graph[x][y][z]==Graph[x-1][y-1][z]:
					path[x][y][z] = 3
				elif Graph[x][y][z]==Graph[x][y][z-1]:
					path[x][y][z] = 4
				elif Graph[x][y][z]==Graph[x][y-1][z]:
					path[x][y][z] = 5
				elif Graph[x][y][z]==Graph[x-1][y][z]:
					path[x][y][z] = 6
				else:
					path[x][y][z] = 0
				
	return [Graph,path]
	
def trackBackPath(Graph,Path):
	x = l1-1
	y = l2-1
	z = l3-1
	otext1 = ''
	otext2 = ''
	otext3 = ''
	
	while(x!=0 or y!=0 or z!=0):
		
		#print(x,y,z)
		if y!=0 and z!=0 and Graph[x][y][z]==Graph[x][y-1][z-1]:
			otext1 += '-'
			otext2 += text2[y]
			otext3 += text3[z]
			y -= 1
			z -= 1
		elif x!=0 and z!=0 and Graph[x][y][z]==Graph[x-1][y][z-1]:
			otext1 += text1[x]
			otext2 += '-'
			otext3 += text3[z]
			x -= 1
			z -= 1
		elif x!=0 and y!=0 and Graph[x][y][z]==Graph[x-1][y-1][z]:
			otext1 += text1[x]
			otext2 += text2[y]
			otext3 += '-'
			x -= 1
			y -= 1
		elif z!=0 and Graph[x][y][z]==Graph[x][y][z-1]:
			otext1 += '-'
			otext2 += '-'
			otext3 += text3[z]
			z -= 1
		elif y!=0 and Graph[x][y][z]==Graph[x][y-1][z]:
			otext1 += '-'
			otext2 += text2[y]
			otext3 += '-'
			y -= 1
		elif x!=0 and Graph[x][y][z]==Graph[x-1][y][z]:
			otext1 += text1[x]
			otext2 += '-'
			otext3 += '-'
			x -= 1
		else:
			otext1 += text1[x]
			otext2 += text2[y]
			otext3 += text3[z]
			x -= 1
			y -= 1
			z -= 1
	return [otext1[::-1],otext2[::-1],otext3[::-1]]

			
if __name__ =='__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
	text1 = '0'+dataset[0]
	text2 = '0'+dataset[1]
	text3 = '0'+dataset[2]
	
	l1 = len(text1)
	l2 = len(text2)
	l3 = len(text3)
	
	[Graph,Path] = multipleAlignment()
	
	[otext1,otext2,otext3] = trackBackPath(Graph,Path)
	print(Graph[-1][-1][-1])
	print(otext1)
	print(otext2)
	print(otext3)