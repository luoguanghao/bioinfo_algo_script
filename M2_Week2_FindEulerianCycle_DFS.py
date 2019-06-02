'''
Find an Eulerian cycle in a graph.

Given: An Eulerian directed graph, in the form of an adjacency list.

Return: An Eulerian cycle in this graph.
-------
0 -> 3
1 -> 0
2 -> 1,6
3 -> 2
4 -> 2
5 -> 4
6 -> 5,8
7 -> 9
8 -> 7
9 -> 6
-------
6->8->7->9->6->5->4->2->1->0->3->2->6
'''

from os.path import dirname

dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
#Build the Graph
Graph = [ [] for i in range(3100) ]

outDegree = [0]*3100
inDegree = [0]*3100

for line in dataset:
	line = line.split()
	preNode = int(line[0])
	nextNodeSet = line[2].split(',')
	outDegree[preNode] = len(nextNodeSet)
	for item in nextNodeSet:
		Graph[preNode].append([int(item),0])
		inDegree[int(item)]+=1
	#print(Graph[preNode])
'''
for i in range(3100):
	if outDegree[i]>inDegree[i]:
		break;
'''
i=6
#print(i)
#DFS
stack = []
stack.append(i)
output = []
#print(Graph)
while(len(stack)>0):
	#print(stack)
	top = stack[-1]
	i=0
	while(i<len(Graph[top])):
		if Graph[top][i][1]==0:
			stack.append(Graph[top][i][0])
			Graph[top][i][1]=1
			break
		i+=1
	
	if i == len(Graph[top]):
		output.append(stack.pop())

#print(output)		
output = output[::-1]
for i in range(len(output)):
	if i!=0:
		print('->',end='')
	print(output[i],end='')
'''
for i in range(len(output)):
	if output[i]==4 and output[i+1]==6:
		break
print(i)
start = i+1
cnt = 0
i=start
while(cnt<len(output)):
	if i == len(output):
		i=1
	print(output[i],end='')
	if cnt!=len(output)-1:
		print('->',end='')
	cnt+=1
	i+=1
	'''