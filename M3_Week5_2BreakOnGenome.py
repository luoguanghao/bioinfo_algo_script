

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

def twoBreakOnGenomeGraph(edges):
	try:
		i1=edges.index([bp[1],bp[0]]) #[31,33]
	except:
		i1=edges.index([bp[0],bp[1]]) 
	try:
		i2=edges.index([bp[2],bp[3]]) #[100,102]
	except:
		i2=edges.index([bp[3],bp[2]]) #
	
	edges[i1]=[bp[0],bp[2]]
	edges[i2]=[bp[3],bp[1]]
	
	return [edges[i1+1:i2+1],edges[:i1+1]+edges[i2+1:]]
	
def CycleToChromosome(Nodes,l):
	chromo = []
	for i in range(1,2*l+1,2):
		if Nodes[i]<Nodes[i+1]:
			chromo.append(int(Nodes[i+1]/2))
		else:
			chromo.append(-int(Nodes[i]/2))
	return chromo

def GraphToGenome(GenomeGraph):
	P = []
	for chromo in GenomeGraph:
		tmp = []
		for i in range(len(chromo)):
			if i!= len(chromo)-1:
				tmp += chromo[i]
			else:
				tmp.append(chromo[i][0])
				tmp = [0,chromo[i][1]]+tmp
		l = int((len(tmp)-1)/2)
		P.append(CycleToChromosome(tmp,l))
	return P
	
if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	bp = [95, 98, 107, 105]
	Edges = []
	P = [] # 格式转换，转换成染色体list P[]
	for Genome in dataset:
		Genome = Genome.strip('(').strip(')')	
		Genome = Genome.split(')(')	
		for chromo in Genome:
			chromo = [0]+list(map(int,chromo.split()))	#格式输入，从index=1开始，0位留0
			P.append(chromo)

	Edges = ColoredEdges(P)[0]
	print('1#',Edges,'\n')
	Edges = twoBreakOnGenomeGraph(Edges)
	print('2#',Edges)
	
	P = GraphToGenome(Edges)
	#print(P)

	for chromo in P:
		for i in range(len(chromo)):
			if i==0:
				print('(',end='')
			else:
				print(' ',end='')
			if chromo[i]>0:
				print('+'+str(chromo[i]),end='')
			else:
				print(str(chromo[i]),end='')
		print(')',end='')
