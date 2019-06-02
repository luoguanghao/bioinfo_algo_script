from os.path import dirname

dataset = open(dirname(__file__) + 'dataset.txt').read().strip()
condon = open(dirname(__file__) + 'RNA_codon_table_1.txt').read().strip().split('\n')
condon_table = []

for line in condon:
	condon_table.append(line.split())

condon_table = dict(condon_table)
#print(condon_table)

for i in range(0,len(dataset),3):
	if condon_table[dataset[i:i+3]] != '*':
		print(condon_table[dataset[i:i+3]],end='')
	