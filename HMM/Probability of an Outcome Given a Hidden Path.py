'''
Probability of an Outcome Given a Hidden Path Problem

Given: A string x, followed by the alphabet Σ from which x was constructed, followed by a hidden path π, followed by the states States and emission matrix Emission of an HMM (Σ, States, Transition, Emission).

Return: The conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π.
-_-_-_-_-_-_-_-_-_-_-_-_
yzyxxyzzyzxxyyzxyxyxzxzyyyyxxxyyyyxyzzzzyzxxzzyxyx
--------
x	y	z
--------
ABBAAABAABBBAABAAAABAABABBBABABAAABAAABBABBBAABABB
--------
A	B
--------
	x	y	z
A	0.195	0.547	0.258	
B	0.39	0.426	0.184
-_-_-_-_-_-_-_-_-_-_-_-_
4.332683876974376e-25
-_-_-_-_-_-_-_-_-_-_-_-_
Lo Kwongho 2018.9
'''

from os.path import dirname

def Probability():
	pr = 1
	for i in range(len(text)):
		pr *= t_matrix[states[path[i]]][alphabet[text[i]]]
	print(pr)

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n--------\n')
	text = dataset[0]
	alphabet =  dict([[dataset[1].split()[i],i] for i in range(len(dataset[1].split()))])
	path = dataset[2]
	states = dict([[dataset[3].split()[i],i] for i in range(len(dataset[3].split()))])
	dataset = dataset[-1].split('\n')[1:]
	t_matrix = [list(map(float,i.split()[1:])) for i in dataset]
	Probability()	