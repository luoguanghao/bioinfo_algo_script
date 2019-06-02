'''
CODE CHALLENGE: Construct the graph of a spectrum.
     Given: A space-delimited list of integers Spectrum.
     Return: Graph(Spectrum).

Note: Throughout this chapter, all dataset problems implicitly use the standard integer-valued mass table for the regular twenty amino acids. Examples sometimes use the toy amino acid alphabet {X, Z} whose masses are 4 and 5, respectively.

Sample Input:
57 71 154 185 301 332 415 429 486
Sample Output:
0->57:G
0->71:A
57->154:P
57->185:K
71->185:N
154->301:F
185->332:F
301->415:N
301->429:K
332->429:P
415->486:A
429->486:G

code : Lo Kwongho 2018.12
'''

from InPutTable import InPut_Integer_Mass_Table
from collections import defaultdict
from os.path import dirname

def inputData():
	dataset=open(dirname(__file__)+'dataset.txt').read().strip().split()
	return list(map(int,dataset))

def build_Graph(IMTable,Spectrum,test=0):
	edges = []	
	for i in range(len(Spectrum)):
		if(IMTable[Spectrum[i]]!=''):
			edges.append([(0,Spectrum[i]),IMTable[Spectrum[i]]])
		for j in range(i+1,len(Spectrum)):
			if(IMTable[abs(Spectrum[i]-Spectrum[j])]!=''):
				edges.append([(Spectrum[i],Spectrum[j]),IMTable[abs(Spectrum[i]-Spectrum[j])]])
	Graph = defaultdict(list)
	for line in edges:
		Graph[line[0][0]].append([line[0][1],line[1]])
	if(test==0):
		return Graph
	else:	
		for line in edges:
			print("%d->%d:%s\n"%(line[0][0],line[0][1],line[1]),end='')

if __name__ == '__main__':
	IMTable = InPut_Integer_Mass_Table()[1]
	Spectrum = inputData()
	build_Graph(IMTable,Spectrum,1)
	