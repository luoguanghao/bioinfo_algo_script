
def BuildDeBruijnGraph(dataset,k,d):
	Graph = {}
	inDegree = {}
	outDegree = {}
	for item in dataset:
		prefix = item[0][0:-1]+'-'+item[1][0:-1]
		suffix = item[0][1:]+'-'+item[1][1:]
		if prefix in Graph.keys():
			if suffix in inDegree.keys():
				inDegree[suffix] += 1
			else:
				inDegree = 1			
			outDegree[prefix] += 1	
			Graph[prefix].append([suffix,0])
		else:			
			if suffix in inDegree.keys():
				inDegree[suffix] += 1
			else:
				inDegree[suffix] = 1	
			outDegree[prefix] = 1				
			Graph[prefix] = [[suffix,0]]
		
	for outDKey in outDegree.keys():
		if not(outDKey in inDegree.keys()):
			break
	start = outDKey
	
	for inDKey in inDegree.keys():
		if not(inDKey in outDegree.keys()):
			break
	Graph[inDKey] = []	
	return [Graph,start]

def DFS(Graph,start):
	output = []
	stack = []
	stack.append(start)
	while(len(stack)):
		top = stack[-1]
		i = 0
		while(i<len(Graph[top])):
			if Graph[top][i][1] == 0:
				stack.append(Graph[top][i][0])
				Graph[top][i][1] = 1
				break
			i += 1
		if i == len(Graph[top]):
			output.append(stack.pop())
	return output[::-1]

from os.path import dirname

dataset = open(dirname(__file__) + 'dataset.txt').read().strip().split()

k = int(dataset[0])
d = int(dataset[1])

dataset = dataset[2:]
for i in range(len(dataset)):
	dataset[i] = dataset[i].split('|')

#print(dataset)

[Graph,start] = BuildDeBruijnGraph(dataset,k,d)
#print(start)
#print(Graph)
EulerianPath = DFS(Graph,start)
#print(Graph)
#print(EulerianPath)

prestr = ''
for i in range(len(EulerianPath)):
	if i == 0:
		prestr += EulerianPath[i].split('-')[0]
	else:
		prestr += EulerianPath[i].split('-')[0][-1]
sufstr = ''	
for i in range(len(EulerianPath)):
	if i == 0:
		sufstr += EulerianPath[i].split('-')[1]
	else:
		sufstr += EulerianPath[i].split('-')[1][-1]

flag = 1
for i in range(k+d+1, len(prestr)):
	if prestr[i] != sufstr[i-k-d]:
		print('No Solution!\n')
		flag = 0
		break
if flag:
	print(prestr[:k+d+1]+sufstr[1:])