'''
Profile HMM with Pseudocounts Problem:
Construct a profile HMM with pseudocounts from a multiple alignment.
Input: A multiple alignment Alignment, a threshold value q, and a pseudo- count value s.
Output: HMM(Alignment, q, s).

http://rosalind.info/problems/ba10f/

@ Lo Kwongho 2018.9
'''
from os.path import dirname
import numpy
import math
	
def preTreat(mutli_Alig):
	tmpMutli_Align = [i for i in zip(*mutli_Alig)]
	miss = [0 for i in range(len(tmpMutli_Align))]
	miss_cnt = 0
	for i in range(len(tmpMutli_Align)):
		if float(tmpMutli_Align[i].count('-')) > threshold*len(tmpMutli_Align[i]):
			miss[i] = 1
			miss_cnt += 1
	
	return [miss,miss_cnt]

def ProfileHMM():
	size = (len(mutli_Alig[0])-miss_cnt)*3+3
	l = len(mutli_Alig[0])
	n = len(mutli_Alig)
	
	state_num = {}
	state_num['S0'] = 0
	state_num['I0'] = 1
	idx = 2
	for i in range(l-miss_cnt):
		state_num['M'+str(i+1)] = idx
		idx += 1
		state_num['D'+str(i+1)] = idx
		idx += 1
		state_num['I'+str(i+1)] = idx
		idx += 1
	state_num['E'] = idx
	#for i in state_num.items():
	#	print(i)
	emission = numpy.zeros(shape=(size,len(alphabet)))
	transition = numpy.zeros(shape=(size,size),dtype=float)
	for text in mutli_Alig:
		#print(text)
		state = 'S'
		p = 0	
		for i in range(l):
			#print(i)
			if miss[i]==1:
				if text[i]!='-':
					transition[state_num[state+str(p)]][state_num['I'+str(p)]] += 1
					emission[state_num['I'+str(p)]][alphabet[text[i]]] += 1
					state = 'I'
			else:
				p += 1
				if text[i]=='-':
					transition[state_num[state+str(p-1)]][state_num['D'+str(p)]] += 1
					state = 'D'
				else:
					transition[state_num[state+str(p-1)]][state_num['M'+str(p)]] += 1
					emission[state_num['M'+str(p)]][alphabet[text[i]]] += 1
					state = 'M'
		if state=='I':
			transition[state_num[state+str(p)]][state_num['E']] += 1
		else:
			transition[state_num[state+str(p)]][state_num['E']] += 1
	# transition
	for i in range(size):
		csum = float(sum(transition[i]))
		if csum > 0:
			for j in range(size):
				transition[i][j] /= csum	
	for x in range(2):
		csum = 0
		for y in range(1,4):
			#print(transition[x][y])
			transition[x][y] += theta
			csum += transition[x][y]
		#print('csum =',csum)
		for y in range(1,4):
			transition[x][y] /= csum

	for i in range(2,size-4,3):
		for x in range(i,i+3):
			csum = 0
			for y in range(i+2,i+5):
				transition[x][y] += theta
				csum += transition[x][y]
			for y in range(i+2,i+5):
				transition[x][y] /= csum

	for x in range(size-4,size-1):
		csum = 0
		for y in range(size-2,size):
			transition[x][y] += theta
			csum += transition[x][y]
		for y in range(size-2,size):
			transition[x][y] /= csum
			
	#
	# emission
	for i in range(size):
		csum = sum(emission[i])
		if csum > 0:
			for j in range(len(alphabet)):
				emission[i][j] /= csum
	for x in range(1,size-1):
		if x%3 != 0:
			csum = 0
			for y in range(len(alphabet)):
				emission[x][y] += theta
				csum += emission[x][y]
			for y in range(len(alphabet)):
				emission[x][y] /= csum
				if 0.005<=emission[x][y] and emission[x][y]<0.01:
					emission[x][y] = 0.01
	
	keys = list(state_num.keys())
	keys[0] = 'S'
	
	#for i in emission:
	#	print(i)
	#for i in transition:
	#	print(i)
	print('\t'+'\t'.join(keys))
	for i in range(size):
		print(keys[i],end='')
		for j in range(size):
			if 0.005<=transition[i][j] and transition[i][j]<0.01:
				transition[i][j]=0.01
			elif 0.005>transition[i][j]:
				transition[i][j] = 0
			print('\t%.3g'%transition[i][j],end='')
		print('')
		
	print('--------\n')
	
	print('\t'+'\t'.join(list(alphabet.keys())))
	for i in range(size):
		print(keys[i],end='')
		for j in range(len(alphabet)):
			#if 0.005<=emission[i][j] and emission[i][j]<0.01:
			#	emission[i][j]=0.01
			print('\t%.3g'%emission[i][j],end='')
		print('')
		
	return [transition,emission]		
		
if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n--------\n')
	[threshold,theta] = list(map(float,dataset[0].split()))
	alphabet = dict([[dataset[1].split()[i],i] for i in range(len(dataset[1].split()))])
	mutli_Alig = dataset[2].split()
	
	[miss,miss_cnt] = preTreat(mutli_Alig)
	[t_matrix ,e_matrix] = ProfileHMM()
	
