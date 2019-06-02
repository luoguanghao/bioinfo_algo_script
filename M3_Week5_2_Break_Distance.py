'''
Code Challenge: Solve the 2-Break Distance Problem.
   >>Input: Genomes P and Q.
   >>Output: The 2-break distance d(P, Q).
-------------
Sample Input:
(+1 +2 +3 +4 +5 +6)
(+1 -3 -6 -5)(+2 -4)
----------------
Sample Output:
3
----------------
coder Lo Kwongho 2018.9
'''

from os.path import dirname

def ChromosomeToCycle(Chromosome):
	l = len(Chromosome)-1
	Nodes = [[] for i in range(2*l+1)]
	for j in range(1,len(Chromosome)):
		if Chromosome[j]>0:
			Nodes[2*j-1]=2*Chromosome[j]-1
			Nodes[2*j]=2*Chromosome[j]
		else:
			Nodes[2*j-1] = -2*Chromosome[j]
			Nodes[2*j] = -2*Chromosome[j]-1
	return Nodes
	
def CycleToChromosome(Nodes,l):
	chromo = []
	for i in range(1,2*l+1,2):
		if Nodes[i]<Nodes[i+1]:
			chromo.append(int(Nodes[i+1]/2))
		else:
			chromo.append(-int(Nodes[i]/2))
	return chromo
	
def ColoredEdges(P):
	Edge = []
	for chomo in P:
		tmp = []
		l = len(chomo)-1 # there is a '0' at the front of chomo
		Nodes=ChromosomeToCycle(chomo)
		for i in range(2,2*l+1,2):
			if i!=2*l:
				tmp.append([Nodes[i],Nodes[i+1]])
			else:
				tmp.append([Nodes[i],Nodes[1]])
		Edge.append(tmp)	
	return Edge
	
def GraphToGenome(GenomeGraph):
	P = []
	for cycle in GenomeGraph:
		first = cycle[-1][1]
		tmp = [0,first]
		for i in range(len(cycle)):
			if i == len(cycle)-1:
				tmp += [cycle[i][0]]
			else:	
				tmp+=cycle[i]
		print(tmp)
		
		P.append(CycleToChromosome(tmp, int((len(tmp)-1)/2)))
	return P	
	
def buildGraph():
	Graph = [[] for i in range(maxn)]

	for chromo in Edges:
		for edge in chromo:
			Graph[edge[0]].append(edge[1])
			Graph[edge[1]].append(edge[0])
	return Graph

def DFS(v):	
	stack = [v]
	visited[v] = 1
	while(len(stack)):
		top = stack[-1]
		i=0
		while(i<len(Graph[top])):
			if visited[Graph[top][i]]==0:
				stack.append(Graph[top][i])
				visited[Graph[top][i]] = 1
				break
			i+=1
		if i == 	len(Graph[top]):
			stack.pop()
			
def count_Cycle():
	global visited
	visited = [0]*maxn
	
	visited[0] = 1
	cnt = 0
	while(1):
		try:
			vIdx = visited.index(0)
		except ValueError:
			break
		DFS(vIdx)
		cnt += 1
	return cnt
	
def count_Block(P):
	s = set()
	for chromo in P:
		for synBlock in chromo[1:]:
			s.add(abs(synBlock))
	return len(s)
		
if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	
	Edges = []
	P = [] # 格式转换，转换成染色体list P[]
	for Genome in dataset:
		Genome = Genome.strip('(').strip(')')	
		Genome = Genome.split(')(')	
		for chromo in Genome:
			chromo = [0]+list(map(int,chromo.split()))	#格式输入，从index=1开始，0位留0
			P.append(chromo)
	
	Edges=ColoredEdges(P)
	
	block_cnt = count_Block(P) #
	maxn = block_cnt*2+1
	
	Graph = buildGraph()

	cycle_cnt = count_Cycle() #
	
	print(block_cnt-cycle_cnt)
		