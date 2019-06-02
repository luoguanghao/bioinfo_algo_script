'''
Edit Distance Problem: Find the edit distance between two strings.
    >>Input: Two strings.
    >>Output: The edit distance between these strings.
-----------------
Sample Input:
PLEASANTLY
MEANLY
-----------------
Sample Output:
5
'''
from os.path import dirname
import numpy

def InitGraph(l1,l2):
	Graph = numpy.zeros([l1,l2])
	for x in range(1,l1):
		Graph[x][0] = Graph[x-1][0]+1
	for y in range(1,l2):
		Graph[0][y] = Graph[0][y-1]+1
	return Graph

def buildEditDistGraph(text1,text2):
	l1 = len(text1)
	l2 = len(text2)
	Graph = InitGraph(l1,l2)
	for x in range(1,l1):
		for y in range(1,l2):
			if text1[x]==text2[y]:
				Graph[x][y]=min(Graph[x][y-1]+1,Graph[x-1][y]+1,Graph[x-1][y-1])
			else:
				Graph[x][y]=min(Graph[x][y-1]+1,Graph[x-1][y]+1,Graph[x-1][y-1]+1)
	return Graph

if __name__ == '__main__':	
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
	
	text1 = '0'+dataset[0]
	text2 = '0'+dataset[1]
	
	Graph = buildEditDistGraph(text1,text2)
	print(int(Graph[-1][-1]))