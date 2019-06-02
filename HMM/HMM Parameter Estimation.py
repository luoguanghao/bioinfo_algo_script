import math
import numpy
from os.path import dirname
import itertools

def HMM_ParameterEstimation():
	transition = numpy.zeros(shape=(len(states),len(states)))
	for i in range(len(HMM_Path)-1):
		transition[states[HMM_Path[i]]][states[HMM_Path[i+1]]] += 1
	for i in range(len(states)):
		csum = sum(transition[i])
		if csum==0:
			transition[i]=[1/len(states)]*len(states)
			continue
		for j in range(len(states)):
			transition[i][j] /= csum
	
	emission = numpy.zeros(shape=(len(states),len(alphabet)))		
	for i in range(len(HMM_Path)):
		emission[states[HMM_Path[i]]][alphabet[text[i]]] += 1
	for i in range(len(states)):
		csum = sum(emission[i])
		if csum==0:
			emission[i]=[1/len(alphabet)]*len(alphabet)
			continue
		for j in range(len(alphabet)):
			emission[i][j] /= csum
	return [transition,emission]	

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n--------\n')
	text = dataset[0]
	HMM_Path = dataset[2]
	alphSet = dataset[1].split()
	alphabet = dict([[dataset[1].split()[i],i] for i in range(len(dataset[1].split()))])
	stateSet = dataset[3].split()
	states = dict([[dataset[3].split()[i],i] for i in range(len(dataset[3].split()))])
	[transition,emission] = HMM_ParameterEstimation()
	print('\t'+'\t'.join(stateSet))
	for i in range(len(states)):
		print(stateSet[i],end='')
		for j in range(len(states)):
			print('\t%.3g'%transition[i][j],end='')
		print('')
	print('--------')
	print('\t'+'\t'.join(alphSet))
	for i in range(len(states)):
		print(stateSet[i],end='')
		for j in range(len(alphSet)):
			print('\t%.3g'%emission[i][j],end='')
		print('')