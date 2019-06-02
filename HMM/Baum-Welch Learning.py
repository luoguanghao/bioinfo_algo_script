import math
import numpy as np
from os.path import dirname
import itertools

def Likelihood_DP(t_matrix,e_matrix,alphabet,states,text):
	graph = np.zeros(shape=(len(states),len(text)),dtype=float)
	for k in range(len(states)):
		graph[k][0] = 1/len(states) * e_matrix[k][alphabet[text[0]]]
	for i in range(1,len(text)):
		for k in range(len(states)):
			graph[k][i] = sum([graph[l][i-1]*t_matrix[l][k]*e_matrix[k][alphabet[text[i]]] for l in range(len(states))])
	lastValue = sum([i[-1] for i in graph])

	return [lastValue,graph] # ??? what ???
	
def tra_Likelihood_DP(t_matrix,e_matrix,alphabet,states,text):
	l = len(text)
	graph = np.zeros(shape=(len(states),len(text)),dtype=float)
	for k in range(len(states)):
		graph[k][l-1] = 1  #1/len(states) * e_matrix[k][alphabet[text[-1]]]
	for i in range(l-2,-1,-1):
		for k in range(len(states)):
			graph[k][i] = sum([graph[kk][i+1]*t_matrix[k][kk]*e_matrix[kk][alphabet[text[i+1]]] for kk in range(len(states))])
	lastValue = sum([i[0] for i in graph])

	return [lastValue,graph] # ??? what ???

def responsibility_profile(text,transition,emission):
	tran = dict([[''.join(list(itertools.product(stateSet,repeat=2))[i]),i] for i in range(len(list(itertools.product(stateSet,repeat=2))))])

	#print(tran)
	pi_star_star = np.zeros(shape=(len(tran),len(text)-1),dtype=float)
	pi_star = np.zeros(shape=(len(states),len(text)),dtype=float)
	
	[lastValue,graph] = Likelihood_DP(transition,emission,alphabet,states,text)
	[tra_lastValue,tra_graph] = tra_Likelihood_DP(transition,emission,alphabet,states,text)
	
	for i in range(len(text)):
		for j in range(len(states)):
			pi_star[j][i] = graph[j][i]*tra_graph[j][i]/lastValue
			
	for i in range(len(text)-1):
		for k in range(len(states)): # pre
			for kk in range(len(states)): # rear
				t = stateSet[k]+stateSet[kk] 
				weight = transition[k][kk]*emission[kk][alphabet[text[i+1]]]
				pi_star_star[tran[t]][i]=graph[k][i]*tra_graph[kk][i+1]*weight/lastValue
	'''
	for i in pi_star_star:
		for j in i:
			print('{:.8f}'.format(j),end=' ')
		print('')
	'''
	return [pi_star,pi_star_star]
	
def ParameterEstimation(text,pi_star,pi_star_star):
	transition = np.zeros(shape=(len(states),len(states)),dtype=float)
	emission = np.zeros(shape=(len(states),len(alphabet)),dtype=float)
	tra_tran = dict([[i,''.join(list(itertools.product(stateSet,repeat=2))[i])] for i in range(len(list(itertools.product(stateSet,repeat=2))))])
	[h,l] = np.shape(pi_star_star)
	for i in range(l):
		for j in range(h):
			k = states[tra_tran[j][0]]
			kk = states[tra_tran[j][1]]
			transition[k][kk] += pi_star_star[j][i]
	for j in range(len(states)):
		csum = sum(transition[j])
		for i in range(len(states)):
			transition[j][i] /= csum
		
	[h,l] = np.shape(pi_star)
	for i in range(l):
		for j in range(h):
			emission[j][alphabet[text[i]]] += pi_star[j][i]
	for j in range(len(states)):
		csum = sum(emission[j])
		for i in range(len(alphabet)):
			emission[j][i] /= csum		
	return [transition,emission]

def Baum_Welch_Learning(text,iterTime,init_t,init_e):

	transition = init_t
	emission = init_e
	for i in range(iterTime):
		[pi_star,pi_star_star] = responsibility_profile(text,transition,emission)
		[transition,emission] = ParameterEstimation(text,pi_star,pi_star_star)
	return [transition,emission]

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n--------\n')
	iterTime = int(dataset[0])
	text = dataset[1]
	
	alphSet = dataset[2].split()	
	stateSet = dataset[3].split()
	alphabet = dict([[alphSet[i],i] for i in range(len(alphSet))])
	states = dict([[stateSet[i],i] for i in range(len(stateSet))])
		
	init_t = [list(map(float,line.split()[1:])) for line in dataset[4].split('\n')[1:]]
	init_e = [list(map(float,line.split()[1:])) for line in dataset[5].split('\n')[1:]]
		
	[transition,emission] = Baum_Welch_Learning(text, iterTime, init_t, init_e)
	
	print('\t'+'\t'.join(stateSet))
	for i in range(len(states)):
		print(stateSet[i],end='')
		for j in range(len(states)):
			if transition[i][j]<0.001:
				print('\t%.3f'%0,end='')
				continue
			print('\t%.3f'%transition[i][j],end='')
		print('')
	print('--------')
	print('\t'+'\t'.join(alphSet))
	for i in range(len(states)):
		print(stateSet[i],end='')
		for j in range(len(alphSet)):
			if emission[i][j]<0.001:
				print('\t%.3f'%0,end='')
				continue
			print('\t%.3f'%emission[i][j],end='')
		print('')