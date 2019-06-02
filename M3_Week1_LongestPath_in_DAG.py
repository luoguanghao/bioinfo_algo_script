'''
Code Challenge: Solve the Longest Path in a DAG Problem.
	 >>Input: An integer representing the starting node to consider in a graph, followed by an integer representing the ending node to 
	consider, followed by a list of edges in the graph. The edge notation "0->1:7" indicates that an edge connects node 0 to node 1
	 with weight 7.  You may assume a given topological order corresponding to nodes in increasing order.
	 >>Output: The length of a longest path in the graph, followed by a longest path. (If multiple longest paths exist, you may return any one.)
	---------------
Sample Input:
0
4
0->1:7
0->2:4
2->3:2
1->4:1
3->4:3	
	---------------
Sample Output:
9
0->2->3->4
'''
## iteration and recursion two method:
def DP_Recursion(node,Graph):
	if vis[node]:
		return nodeCount[node]
	vis[node] = 1
	for i in range(maxn):
		if Graph[i][node]!=-1:
			tmp = DP_Recursion(i, Graph)+Graph[i][node]
			if tmp > nodeCount[node]:
				nodeCount[node] = tmp
				path[node] = i
	return (nodeCount[node])

def DP_Iteration():
	for node in nodeSet:
		for i in range(maxn):
			if Graph[node][i] != -1:
				if nodeCount[i]<nodeCount[node]+Graph[node][i]:
					nodeCount[i]=nodeCount[node]+Graph[node][i]
					path[i]=node

if __name__ == '__main__':
	maxn = 50
	nodeCount = [-999999]*maxn
	path = [-1]*maxn
	vis = [0]*maxn
	
	from os.path import dirname
	import numpy
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	sNode = int(dataset[0])
	eNode = int(dataset[1])
	nodeSet = set()
	Graph = numpy.ones([maxn,maxn])*-1
	#Build Graph
	for i in range(2,len(dataset)):
		preNode = int(dataset[i].split('->')[0])
		nexNode = int(dataset[i].split('->')[1].split(':')[0])
		w = int(dataset[i].split('->')[1].split(':')[1])
		Graph[preNode][nexNode] = w
		nodeSet.add(preNode)
	nodeSet.add(eNode)	
	print(Graph)
	
	nodeCount[sNode] = 0 #固定起点的LongestPath寻找方法
	
# Recursion:	
	Longest = int(DP_Recursion(eNode, Graph))
	print(Longest)
	#printPath
	output = []
	node = eNode
	while(path[node]!=-1):
		output.append(node)
		node = path[node]
	output.append(node)
	output=output[::-1]
	for i in range(len(output)):
		if i != 0:
			print('->',end='')
		print(output[i],end='')

	'''
# Iteration:
	DP_Iteration()
	
	print(nodeCount[eNode])	
	#Output
	output = []
	i = eNode
	while(path[i]!=-1):
		output.append(i)
		i=path[i]
	output.append(i)
	output=output[::-1]
	for i in range(len(output)):
		if i!=0:
			print('->',end='')
		print(output[i],end='')
		'''