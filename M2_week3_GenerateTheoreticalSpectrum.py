from os.path import dirname

peptides = 'NQEL'

massTable = open(dirname(__file__)+'integer_mass_table.txt').read().strip().split('\n')
for i in range(len(massTable)):
	massTable[i] = massTable[i].split()
massTable = dict(massTable)

elements = []
for k in range(1,len(peptides)):
	for i in range(len(peptides)):
		element = peptides[i:i+k]
		if k-len(peptides)+i>0:
			element += peptides[:k-len(peptides)+i]
		elements.append(element)
elements.append(peptides)
print(elements)
print(0,end='')

def GetMass(text):
	mass = 0
	for i in text:
		mass += int(massTable[i])
	return mass

for i in elements:
	print(' ',end='')
	print(GetMass(i),end='')
#
print('\n',[[int(i)] for i in massTable.values() ])