'''
HMM Parameter Learning Problem:
Estimate the parameters of an HMM explaining an emitted string.
Input: A string x = x1 . . . xn emitted by an HMM with unknown transition and emission probabilities.
Output: A transition matrix Transition and an emission matrix Emission that maximize Pr(x, p) over all possible transition and emission matrices and over all hidden paths p.

@ Lo Kwongho
'''

from os.path import dirname
import numpy as np
import math

def ViterbiAlgorithm(t_matrix,e_matrix,alphabet,states,text):
	graph = np.zeros(shape=(len(states),len(text)),dtype=float)
	for k in range(len(states)):
		#print(e_matrix[k][alphabet[text[0]]])
		graph[k][0] = math.log(e_matrix[k][alphabet[text[0]]])
	for i in range(1,len(text)):
		for k in range(len(states)):
			graph[k][i] = max([graph[l][i-1]+math.log(t_matrix[l][k]*e_matrix[k][alphabet[text[i]]]) for l in range(len(states))])
	lastValue = [i[-1] for i in graph]
	track = lastValue.index(max(lastValue))

	output = tra_states[track]
	for i in range(len(text)-2,-1,-1):
		for l in range(len(states)):
			if graph[track][i+1]==graph[l][i]+math.log(t_matrix[l][track]*e_matrix[track][alphabet[text[i+1]]]):
				track = l
				break
		output += tra_states[track]
	return output[::-1]

def HMM_ParameterEstimation(pseudocount,alphabet,states,HiddenPath,text):
	transition = np.zeros(shape=(len(states),len(states)))
	for i in range(len(HiddenPath)-1):
		transition[states[HiddenPath[i]]][states[HiddenPath[i+1]]] += 1
	for i in range(len(states)):
		csum = sum(transition[i])
		if csum==0:
			#transition[i]=[1/len(states)]*len(states)
			continue
		for j in range(len(states)):
			transition[i][j] /= csum
	for i in range(len(states)):
		csum = 0
		for j in range(len(states)):
			transition[i][j] += pseudocount
			csum += transition[i][j]
		for j in range(len(states)):
			transition[i][j] /= csum
		
	emission = np.zeros(shape=(len(states),len(alphabet)))		
	for i in range(len(HiddenPath)):
		emission[states[HiddenPath[i]]][alphabet[text[i]]] += 1
	for i in range(len(states)):
		csum = sum(emission[i])
		if csum==0:
			#emission[i]=[1/len(alphabet)]*len(alphabet)
			continue
		for j in range(len(alphabet)):
			emission[i][j] /= csum
	for i in range(len(states)):
		csum = 0
		for j in range(len(alphabet)):
			emission[i][j] += pseudocount
			csum += emission[i][j]
		for j in range(len(alphabet)):
			emission[i][j] /= csum
		
	return [transition,emission]

def Viterbi_Learning(init_t,init_e,iterTime,text,alphabet,states):
	pseudocount = 0.0001
	
	transition = init_t
	emission = init_e
	for i in range(iterTime):		
		HiddenPath = ViterbiAlgorithm(transition,emission,alphabet,states, text)
		[transition,emission] = HMM_ParameterEstimation(pseudocount,alphabet,states,HiddenPath,text)
	#HiddenPath = ViterbiAlgorithm(transition,emission,alphabet,states, text)
	return [transition,emission]

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n--------\n')
	iterTime = int(dataset[0])
	text = dataset[1]
	alphSet = dataset[2].split()
	alphabet = dict([[alphSet[i],i] for i in range(len(alphSet))])
	stateSet = dataset[3].split()
	states = dict([[stateSet[i],i] for i in range(len(stateSet))])
	tra_states = dict([[i,stateSet[i]] for i in range(len(stateSet))])
	
	init_t = [list(map(float,line.split()[1:])) for line in dataset[4].split('\n')[1:]]
	init_e = [list(map(float,line.split()[1:])) for line in dataset[5].split('\n')[1:]]
	
	[transition,emission] = Viterbi_Learning(init_t,init_e,iterTime,text,alphabet,states)

	# print
	print('\t'+'\t'.join(stateSet))
	for i in range(len(states)):
		print(stateSet[i],end='')
		for j in range(len(states)):
			if transition[i][j]<0.001:
				print('\t%.3g'%0,end='')
				continue
			print('\t%.3g'%transition[i][j],end='')
		print('')
	print('--------')
	print('\t'+'\t'.join(alphSet))
	for i in range(len(states)):
		print(stateSet[i],end='')
		for j in range(len(alphSet)):
			if emission[i][j]<0.001:
				print('\t%.3g'%0,end='')
				continue
			print('\t%.3g'%emission[i][j],end='')
		print('')
	
	