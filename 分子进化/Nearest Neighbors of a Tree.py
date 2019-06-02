from os.path import dirname
import numpy as np
import copy

def nearestNeighborsExchange():
	global Graph
	NeighborGraph1 = copy.deepcopy(Graph[:])	
	candidate1 = Graph[n[0]]
	candidate2 = Graph[n[1]]
	candidate1.remove(n[1])
	candidate2.remove(n[0])
	NeighborGraph1[candidate1[0]].remove(n[0])
	NeighborGraph1[candidate1[1]].remove(n[0])
	NeighborGraph1[candidate2[0]].remove(n[1])
	NeighborGraph1[candidate2[1]].remove(n[1])
	NeighborGraph2 = copy.deepcopy(NeighborGraph1[:])
	
	#print(candidate1,candidate2)
	NeighborGraph1[n[0]]=[candidate1[0],candidate2[0],n[1]]
	NeighborGraph1[candidate1[0]].append(n[0])
	NeighborGraph1[candidate2[0]].append(n[0])
	
	NeighborGraph1[n[1]]=[candidate1[1],candidate2[1],n[0]]
	NeighborGraph1[candidate1[1]].append(n[1])
	NeighborGraph1[candidate2[1]].append(n[1])
	
	NeighborGraph2[n[0]]=[candidate1[0],candidate2[1],n[1]]
	NeighborGraph2[candidate1[0]].append(n[0])
	NeighborGraph2[candidate2[1]].append(n[0])
	
	NeighborGraph2[n[1]]=[candidate1[1],candidate2[0],n[0]]
	NeighborGraph2[candidate1[1]].append(n[1])
	NeighborGraph2[candidate2[0]].append(n[1])
	
	for i in range(maxn):
		for j in NeighborGraph1[i]:
			print("%d->%d"%(i,j))
	print('')
	for i in range(maxn):
		for j in NeighborGraph2[i]:
			print("%d->%d"%(i,j))

def buildGraph():
	global dataset
	n = list(map(int,dataset[0].split()))
	dataset = dataset[1:]
	maxn = len(dataset)//2 + 1
	Graph = [[]for i in range(maxn)]
	for line in dataset:
		Graph[int(line.split('->')[0])].append(int(line.split('->')[1]))
	return [Graph,maxn,n]

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	[Graph,maxn,n] = buildGraph()
	nearestNeighborsExchange()
