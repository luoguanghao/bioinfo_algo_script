from os.path import dirname
from collections import defaultdict

def InPut_Integer_Mass_Table():
	dataset = open(dirname(__file__)+'/integer_mass_table.txt').read().strip().split('\n')
	dataset = [i.split() for i in dataset]
	traTbl = []
	for i in dataset:
		i[1]=int(i[1])
		traTbl.append([i[1],i[0]])
	
	return [defaultdict(int,dataset),defaultdict(str,traTbl)]
	
if __name__ == '__main__':
	#print(InPut_Integer_Mass_Table())
	pass
	
'''
G 57
A 71
S 87
P 97
V 99
T 101
C 103
I 113
L 113
N 114
D 115
K 128
Q 128
E 129
M 131
H 137
F 147
R 156
Y 163
W 186
'''