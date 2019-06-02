import numpy as np
from os.path import dirname

dict = {'A':0,'C':1,'G':2,'T':3}
dict2 = {0:'A',1:'C',2:'G',3:'T'}

def GetIndx(s):
	
	out = 0
	for i in s:
		out = out*4 + dict[i]
		
	return out
	
def GetS(num,k):
	s = ''
	
	for i in range(k):
		s += dict2[num%4]
		num = int(num/4)
	return s[::-1]
	

dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
k = int(dataset[0])
text = dataset[1]
lt = len(text)
k_mers = [[] for i in range(4**k)]
graph = [[] for i in range(4**(k-1))]

prefix = []
'''
for i in range(lt-k+1):
	kmer = text[i:i+k]
	k_mers.append(kmer)
	prefix[GetIndx(kmer[0:-1])].append(kmer)
'''
nodes = []
for i in range(lt-(k-1)+1):
	node = text[i:i+k-1]
	nodes.append(node)
	
for i in range(len(nodes)-1):
	indx = GetIndx(nodes[i])
	graph[indx].append(nodes[i+1])
	#print(graph[indx])


# print the Graph
for i in range( 4**(k-1) ):
	if graph[i]!=[]:
		print(GetS(i, k-1),'-> ',end='')
		cnt=0
		for item in graph[i]:
			if cnt:
				print(',',end='')
			print(item,end='')
			cnt+=1
		print('\n',end='')
		
# Find the begin >>>
flag = [0 for i in range(4**(k-1))]
for i in range(len(nodes)):
	indx = GetIndx(nodes[i])
	for item in graph[indx]:
		flag[GetIndx(item)]=1

for i in range(len(nodes)):
	if flag[GetIndx(nodes[i])]==0:
		print('** ',nodes[i])
	
