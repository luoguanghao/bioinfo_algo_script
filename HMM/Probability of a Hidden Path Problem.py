'''
Probability of a Hidden Path Problem
>> Given: A hidden path π followed by the states States and transition matrix Transition of an HMM (Σ, States, Transition, Emission).
>> Return: The probability of this path, Pr(π). You may assume that initial probabilities are equal.
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB
--------
A   B
--------
	A   B
A   0.194   0.806
B   0.273   0.727
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
5.01732865318e-19
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
Lo Kwongho 2018.9
'''

from os.path import dirname

def Pr_of_Hidden_Path():
	pr = 1
	current = -1
	for i in path:
		if current==-1:
			current = i
			pr *= 0.5
			continue
		pr *= t_matrix[d[current]][d[i]]
		current = i
	return (pr)


if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n--------\n')
	path = dataset[0]
	states = dataset[1].split()
	d = dict([[states[i],i] for i in range(len(states))])

	dataset = dataset[-1].split('\n')[1:]
	t_matrix = [list(map(float,i.split()[1:])) for i in dataset]
	#print(t_matrix)
	print(Pr_of_Hidden_Path())
	

