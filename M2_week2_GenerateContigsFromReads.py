from os.path import dirname

def BuildDeBruijnGraph(dataset,k):
	Graph = {}
	inDegree = {}
	outDegree = {}
	for item in dataset:
		if item[0:-1] in Graph.keys():
			
			if item[1:] in inDegree.keys():
				inDegree[item[1:]] += 1
			else:
				inDegree[item[1:]] = 1
				
			outDegree[item[0:-1]] += 1
			
			Graph[item[0:-1]].append([item[1:],0])
		else:
			if item[1:] in inDegree.keys():
				inDegree[item[1:]] += 1
			else:
				inDegree[item[1:]] = 1
				
			outDegree[item[0:-1]] = 1
			
			Graph[item[0:-1]] = [[item[1:],0]]
			
	#print(inDegree)
	#print(outDegree)
	start = []
	for outDegreeKey in outDegree.keys():
		if not(outDegreeKey in inDegree.keys()):
			start.append(outDegreeKey)		
	end = []
	for inDegreeKey in inDegree.keys():
		if not(inDegreeKey in outDegree.keys()):
			end.append(inDegreeKey)
	for i in end:
		Graph[i] = []
	return [Graph,start,end,inDegree,outDegree]

def FindTheEulerianCycle_DFS(Graph,n,start):
	stack = []
	stack.append(start)
	output = []
	while(len(stack)>0):
		top = stack[-1]
		i=0
		while(i<len(Graph[top])):
			if Graph[top][i][1]==0:
				stack.append(Graph[top][i][0])
				Graph[top][i][1] = 1
				break
			i+=1
		if i == len(Graph[top]):
			output.append(stack.pop())			
	return output

dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
k = len(dataset[0])
n = len(dataset)

[DeBruijnGraph,start,end,inDegree,outDegree] = BuildDeBruijnGraph(dataset, k)
#print(DeBruijnGraph)
#print(DeBruijnGraph)
EulerCyc = FindTheEulerianCycle_DFS(DeBruijnGraph,n,start[0])[::-1]
#print(start)
'''
for item in EulerCyc:
	if item == EulerCyc[0]:
		print(item,end='')
	else:
		print(item[-1],end='')
'''
s = set()
for inDKey in inDegree:
	if inDegree[inDKey]!=1:
		s.add(inDKey)
for outDKey in outDegree:
	if outDegree[outDKey]!=1:
		s.add(outDKey)
for i in start:	
	s.add(i)	
for i in end:
	s.add(i)
		
#print(s)
########### Contigs ###########
Contigs = []
def BuildContigs(v,w):
	contig = []
	if not(w in s):
		for wItem in DeBruijnGraph[w]:
			contig+=(BuildContigs(w, wItem[0]))
	contig.append(w)
	return contig
	

for v in s:
	if not(v in end):
		for wItem in DeBruijnGraph[v]:
			#print(BuildContigs(v,wItem[0],[v]))
			contig = BuildContigs(v,wItem[0])
			contig.append(v)
			Contigs.append(contig[::-1])

#print(Contigs)
output = []
for i in range(len(Contigs)):
	line = Contigs[i][0]
	for j in range(1,len(Contigs[i])):
		line += Contigs[i][j][-1]
	output.append(line)
	
output.sort()
for line in output:
	print(line)		
		
		
		