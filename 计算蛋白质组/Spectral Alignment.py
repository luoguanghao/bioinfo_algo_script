from os.path import dirname
import numpy
import copy
from InPutTable import InPut_Integer_Mass_Table

def SpectralAlignment(peptide,Spectrum_Vector,k):
	MINUS_INF = float('-inf')
	l = len(Spectrum_Vector)+1
	IMTable = InPut_Integer_Mass_Table()[0]
	#print(IMTable)
	
	def InitializeGraph():
		Graph = [(0,[MINUS_INF for i in range(l)])]
		mass_list = [0]
		Diff = [0]
		mass = 0
		for aa in peptide:
			mass += IMTable[aa]
			line = [MINUS_INF for i in range(l)]
			line[0] = MINUS_INF 
			mass_list.append(mass)
			Diff.append(IMTable[aa])
			Graph.append((mass,line))
		Graph = dict(Graph)
		Graph = [copy.deepcopy(Graph) for i in range(k+1)]
		Graph[0][0][0] = 0
		Track = copy.deepcopy(Graph)
		#print(Graph)
		return [Graph, Track, mass_list, Diff]
	
	#InitializeGraph()
	[Graph, Track, mass_list, Diff] = InitializeGraph()
	#Graph[0][4][0]=111
	#print(mass_list,Diff)
	#for i in range(k+1):
	#	print(Graph[i])
	#print(Diff)
	for t in range(k+1):
		for i in range(1,len(peptide)+1):
			if i>0:
				for j in range(l):
					maxval = float('-inf')
					if j-Diff[i]>=0:
						maxval = Graph[t][mass_list[i]-Diff[i]][j-Diff[i]]
					if t>=1:
						for jpi in range(j):
							if maxval<Graph[t-1][mass_list[i]-Diff[i]][jpi]:
								maxval=Graph[t-1][mass_list[i]-Diff[i]][jpi]
								pre = [t-1, mass_list[i]-Diff[i], jpi]
					Graph[t][mass_list[i]][j] = maxval + Spectrum_Vector[j-1]
	t = -1
	maxval = 0
	for i in range(k+1):
		if Graph[i][mass_list[-1]][-1] > maxval:
			maxval = Graph[i][mass_list[-1]][-1]
			t = i
	j = l-1
	i = len(peptide)
	path = []
	#print(j,i)
	while 1:
		path = [j]+path
		if i==0:
			break
		#print(t,i,j)
		if Graph[t][mass_list[i]][j]-Spectrum_Vector[j-1]==Graph[t][mass_list[i-1]][j-Diff[i]]:
			j = j-Diff[i]
			i -=1		
		else:
			for jpi in range(j):
				if Graph[t][mass_list[i]][j]-Spectrum_Vector[j-1]==Graph[t-1][mass_list[i-1]][jpi]:
					i -= 1
					j = jpi
					t -= 1
					break
	print(path)
	cnt = 0
	for i in range(len(peptide)):
		print(peptide[i],end='')
		if (path[i+1]-cnt)-Diff[i+1]>0:
			print("(+%d)"%((path[i+1]-cnt)-Diff[i+1]),end='')
		elif (path[i+1]-cnt)-Diff[i+1]<0:
			print("(%d)"%((path[i+1]-cnt)-Diff[i+1]),end='')
		cnt = path[i+1]	
	#for i in Graph:
	#	print('')
	#	print(i)

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	peptide = dataset[0]
	Spectrum_Vector = list(map(int,dataset[1].split()))
	k = int(dataset[2])
	SpectralAlignment(peptide,Spectrum_Vector,k)