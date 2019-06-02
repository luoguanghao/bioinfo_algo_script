'''
2-Break Sorting Problem: Find a shortest transformation of one genome into another by 2-breaks.
>>Input: Two genomes with circular chromosomes on the same set of synteny blocks.
>>Output: The sequence of genomes resulting from applying a shortest sequence of 2-breaks
     transforming one genome into the other.
-------------
Sample Input:
(+1 -2 -3 +4)
(+1 +2 -4 -3)
-------------
Sample Output:
(+1 -2 -3 +4)
(+1 -2 -3)(+4)
(+1 -2 -4 -3)
(-3 +1 +2 -4)
-------------
coder Lo Kwongho 2018.9
'''
import numpy as np
from os.path import dirname

def GenomeToCyc(genome):
	
	cycGenome = []
	for chromo in genome:
		tmp = []
		for i in range(len(chromo)):
			if chromo[i]>0:
				tmp.append([chromo[i]*2-1,chromo[i]*2])
			else:
				tmp.append([chromo[i]*(-2),chromo[i]*(-2)-1])
		cycGenome.append(tmp)
	return cycGenome

def colorEdges(genome):
	edges = []
	cycGenome = GenomeToCyc(genome)
	for chromo in cycGenome:
		if len(chromo)==1:
			edges.append(chromo[0][::-1])
			continue
		for i in range(len(chromo)-1):
			edges.append([ chromo[i][1],chromo[i+1][0] ])
		edges.append([chromo[i+1][1],chromo[0][0]])
	return edges

def colored_edges_cycles(blue, red):
	size = len(blue)+len(red)+1
	adj = np.zeros(shape=(size,2),dtype=int)
	visited = [0]*(size)
	for e in blue:
		adj[e[0],0] = e[1]
		adj[e[1],0] = e[0]
	for e in red:
		adj[e[0],1] = e[1]
		adj[e[1],1] = e[0]
	cycles = []
	for v in range(1,size):
		if visited[v]==1:
			continue
		visited[v]==1
		head = v
		c = [head]
		color = 0
		while(True):
			v = adj[v,color]
			if v == head:
				cycles.append(c)
				break
			visited[v] = 1
			c.append(v)
			color = (color+1)%2
	return cycles


def count_Block(P,Q):
	s = set()
	for i in P[0]:
		s.add(abs(i))
	for i in Q[0]:
		s.add(abs(i))
	return len(s)
	
def twoBreakDistance(P,Q):
	blue = colorEdges(P)
	red = colorEdges(Q)
	cycles = colored_edges_cycles(blue,red)
	cnt_Cyc = len(cycles)
	cnt_Block = count_Block(P,Q)
	return cnt_Block-cnt_Cyc

def GraphToGenome(g):
	size = len(g)*2+1
	visited = []
	adj = np.zeros(shape=size,dtype=int) ##
	for e in g:
		adj[e[0]] = e[1]
		adj[e[1]] = e[0]
	print('g#=',g)
	Genome = []
	for e in g:
		orig = e[0]
		if orig in visited:
			continue
		visited.append(orig)
		if orig%2 == 0:
			close = orig-1
		else:
			close = orig+1
		tmp = []
		while(True):
			if orig%2 ==0:
				tmp.append(int(orig/2))
			else:
				tmp.append(int(-(orig+1)/2))
			dest = adj[orig]
			visited.append(dest)
			if dest==close:
				Genome.append(tmp)
				break
			
			if dest%2 == 0:
				orig = dest-1
			else:
				orig = dest+1
			visited.append(orig)
	print('Genome=',Genome)
	return Genome

def twoBreakOnGenome(P,i1,i2,j1,j2):
	g = colorEdges(P)
	g = twoBreakOnGraph(g,i1,i2,j1,j2)
	return GraphToGenome(g)

def twoBreakOnGraph(g,i1,i2,j1,j2):
	rem = [[i1,i2],[i2,i1],[j1,j2],[j2,j1]]
	bg = []
	for e in g:
		if e not in rem:
			bg.append(e)
	bg.append([i1,j1])
	bg.append([i2,j2])
	print('bg=',bg)
	return bg

def twoBreakSorting(P,Q):
	red = colorEdges(Q)
	path = [P]
	
	while(twoBreakDistance(P,Q)>0):
		blue = colorEdges(P)
		cycles = colored_edges_cycles(blue,red)
		print('Cycs=',cycles)
		for c in cycles:
			if len(c)>=4:
				P = twoBreakOnGenome(P,c[0],c[1],c[3],c[2])
				print('P=',P)
				print('')
				path.append(P)
				break
	return path

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().split('\n')
	text1 = [list(map(int,dataset[0].strip('(').strip(')').split() ))]
	text2 = [list(map(int,dataset[1].strip('(').strip(')').split() ))]
	
	path = twoBreakSorting(text1,text2)
	for line in path:
		for chromo in line:
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
		print('')