'''
CODE CHALLENGE: Solve the Decoding an Ideal Spectrum Problem.
     Given: A space-delimited list of integers Spectrum.
     Return: An amino acid string that explains Spectrum.

Sample Input:
57 71 154 185 301 332 415 429 486
Sample Output:
GPFNA

code Lo Kwongho 2018.12
'''

from Construct_Graph_of_Spectrum import build_Graph
from InPutTable import InPut_Integer_Mass_Table
from collections import defaultdict
from os.path import dirname
from IdealSpectrum import IdealSpectrum

def inputData():
	dataset=open(dirname(__file__)+'dataset.txt').read().strip().split()
	return list(map(int,dataset))
	
def problem(dataset):
	stack = []
	peptide = []
	ans = []
	def dfs(Graph,v,aa):
		stack.append(v)
		peptide.append(aa)
		if(Graph[v]==[]):
			ISpectrum=IdealSpectrum(peptide[1:])
			if(dataset==ISpectrum):
				ans.append(''.join(peptide[1:]))
			stack.pop()
			peptide.pop()
			return;
		for i in range(len(Graph[v])):
			dfs(Graph, Graph[v][i][0], Graph[v][i][1])
		stack.pop()
		peptide.pop()
		return
	dfs(Graph, 0, '')	
	
	return ans
	
if __name__ == '__main__':
	IMTable = InPut_Integer_Mass_Table()[1]
	Spectrum = inputData()
	Graph = build_Graph(IMTable, Spectrum)
	#print(Graph)
	dataset = sorted(list(map(int,open(dirname(__file__)+'dataset.txt').read().strip().split())))
	#print(dataset)
	ans=problem(dataset)
	print(ans)