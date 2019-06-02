'''
Compute the Probability of a String Emitted by an HMM
Outcome Likelihood Problem
	Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
	Return: The probability Pr(x) that the HMM emits x.
[][][][][][][][][][][]
Sample Dataset
xzyyzzyzyy
--------
x   y   z
--------
A   B
--------
	A   B
A   0.303   0.697 
B   0.831   0.169 
--------
	x   y   z
A   0.533   0.065   0.402 
B   0.342   0.334   0.324
[][][][][][][][][][][]
Sample Output
1.1005510319694847e-06
[][][][][][][][][][][]
Lo Kowngho 2018.9
'''
from os.path import dirname
import numpy as np
import math

def Likelihood_DP(t_matrix,e_matrix,alphabet,states,text):
	graph = np.zeros(shape=(len(states),len(text)),dtype=float)
	for k in range(len(states)):
		graph[k][0] = 1/len(states) * e_matrix[k][alphabet[text[0]]]   ## ????
	for i in range(1,len(text)):
		for k in range(len(states)):
			graph[k][i] = sum([graph[l][i-1]*t_matrix[l][k]*e_matrix[k][alphabet[text[i]]] for l in range(len(states))])
	lastValue = sum([i[-1] for i in graph])
	return lastValue # ??? what ???
					
			

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n--------\n')
	text = dataset[0]
	alphabet = dict([[dataset[1].split()[i],i] for i in range(len(dataset[1].split()))] )#alphabet
	states = dict([[dataset[2].split()[i],i] for i in range(len(dataset[2].split()))]) #states
	tra_states = dict([[i,dataset[2].split()[i]] for i in range(len(dataset[2].split()))])
	t_matrix = [list(map(float,i[1:].split())) for i in dataset[3].split('\n')[1:]]
	e_matrix = [list(map(float,i[1:].split())) for i in dataset[4].split('\n')[1:]]
	Likelihood = Likelihood_DP(t_matrix,e_matrix,alphabet,states,text)
	print(Likelihood)