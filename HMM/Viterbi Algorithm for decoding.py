'''
Implement the Viterbi Algorithm  Decoding Problem

>> Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
>> Return: A path that maximizes the (unconditional) probability Pr(x, π) over all possible paths π.
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
xyxzzxyxyy
--------
x   y   z
--------
A   B
--------
	A   B
A   0.641   0.359
B   0.729   0.271
--------
	x   y   z
A   0.117   0.691   0.192   
B   0.097   0.42    0.483
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
AAABBAAAAA
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
Lo Kwongho 2018.9
'''

from os.path import dirname
import numpy as np
import math

def ViterbiAlgorithm():
	graph = np.zeros(shape=(len(states),len(text)),dtype=float)
	for k in range(len(states)):
		graph[k][0] = math.log(e_matrix[k][alphabet[text[0]]])
	for i in range(1,len(text)):
		for k in range(len(states)):
			graph[k][i] = max([graph[l][i-1]+math.log(t_matrix[l][k]*e_matrix[k][alphabet[text[i]]]) for l in range(len(states))])
	lastValue = [i[-1] for i in graph]
	track = lastValue.index(max(lastValue))
	for i in range(len(text)):
		print(graph[0][i],graph[1][i])
	#print(track_back_s)
	output = tra_states[track]
	for i in range(len(text)-2,-1,-1):
		for l in range(len(states)):
			if graph[track][i+1]==graph[l][i]+math.log(t_matrix[l][track]*e_matrix[track][alphabet[text[i+1]]]):
				track = l
				break
		output += tra_states[track]
	return output[::-1]		
				
			

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n--------\n')
	text = dataset[0]
	alphabet = dict([[dataset[1].split()[i],i] for i in range(len(dataset[1].split()))] )#alphabet
	states = dict([[dataset[2].split()[i],i] for i in range(len(dataset[2].split()))]) #states
	tra_states = dict([[i,dataset[2].split()[i]] for i in range(len(dataset[2].split()))])
	t_matrix = [list(map(float,i[1:].split())) for i in dataset[3].split('\n')[1:]]
	e_matrix = [list(map(float,i[1:].split())) for i in dataset[4].split('\n')[1:]]
	HiddenPath = ViterbiAlgorithm()
	print(HiddenPath)