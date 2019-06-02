'''
Code Challenge: Use OutputLCS (reproduced below) to solve the Longest Common Subsequence Problem.
     >>Input: Two strings s and t.
     >>Output: A longest common subsequence of s and t. (Note: more than one solution may exist, in which case you may output any one.)
----------------
Sample Input:
AACCTTGG
ACACTGTGA
----------------
Sample Output:
AACTGG
'''

def Build_LCS_Graph(text1,text2,l1,l2):
	import numpy
	Path = numpy.zeros([l2-1,l1-1])
	Graph = numpy.zeros([l2,l1])
	for x in range(1,l2):
		for y in range(1,l1):
			if text1[y] == text2[x]:
				Graph[x][y] = max(Graph[x-1][y],Graph[x][y-1],Graph[x-1][y-1]+1)
			else:
				Graph[x][y] = max(Graph[x-1][y],Graph[x][y-1])
	return Graph

def OutputLCS(Graph,l1,l2):
	x = l2-1
	y = l1-1
	output = ''
	while(x!=0 and y!=0):
		if Graph[x][y]==Graph[x-1][y]:
			x-=1
		elif Graph[x][y]==Graph[x][y-1]:
			y-=1
		else:
			output+=text1[y]
			x-=1
			y-=1

	print(output[::-1])		

if __name__ == "__main__":
		from os.path import dirname
		
		dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
		text1 = '0'+dataset[0]
		text2 = '0'+dataset[1]
		l1 = len(text1)
		l2 = len(text2)
		Graph = Build_LCS_Graph(text1,text2,l1,l2)
		OutputLCS(Graph, l1, l2)