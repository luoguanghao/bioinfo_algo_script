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
	
	for outDegreeKey in outDegree.keys():
		if not(outDegreeKey in inDegree.keys()):
			break;		
	start = outDegreeKey
	for inDegreeKey in inDegree.keys():
		if not(inDegreeKey in outDegree.keys()):
			break
	end = inDegreeKey
	Graph[end] = []
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
k = int(dataset[0])
dataset = dataset[1:]
n = len(dataset)

[DeBruijnGraph,start,end,inDegree,outDegree] = BuildDeBruijnGraph(dataset, k)
#print(DeBruijnGraph)
print(DeBruijnGraph)
EulerCyc = FindTheEulerianCycle_DFS(DeBruijnGraph,n,start)[::-1]
print(start)

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
s.add(start)
		
print(s)
for v in s:
	'''
