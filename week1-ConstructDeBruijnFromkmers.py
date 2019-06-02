## python 图的表示 ###

from os.path import dirname
dict1 = {'A':0,'C':1,'G':2,'T':3}
dict2 = {0:'A',1:'C',2:'G',3:'T'}

def GetIndx(s):
	
	out = 0
	for i in s:
		out = out*4 + dict1[i]
		
	return out
	
def GetS(num,k):
	s = ''
	
	for i in range(k):
		s += dict2[num%4]
		num = int(num/4)
	return s[::-1]
	
	
dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
k = len(dataset[0])
dataset = dataset[1:]
n = len(dataset)
''' 这是映射成数的方法，当k大的时候不能用
Graph = [[] for i in range(4**(k-1))]

for item in dataset:
	Graph[GetIndx(item[0:-1])].append(item[1:])
	
for i in range(4**(k-1)):
	if Graph[i]!=[]:
		print(GetS(i, k-1),'-> ',end='')
		cnt=0
		for item in Graph[i]:
			if cnt:
				print(',',end='')
			print(item,end='')
			cnt+=1
		print('')
'''
Graph = {}

for item in dataset:
	print('*',item)
	if item[0:-1] in Graph.keys():
		Graph[item[0:-1]].append(item[1:])
	else:
		Graph[item[0:-1]] = [item[1:]]

for item in Graph.items():
	print(item[0],'-> ',end='')
	for i in range(len(item[1])):
		if i!=0:
			print(',',end='')
		print(item[1][i],end='')
	print('')


	