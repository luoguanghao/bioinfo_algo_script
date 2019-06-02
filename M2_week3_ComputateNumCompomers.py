import numpy
from os.path import dirname
#import the mass table of amino acids
massTable = open(dirname(__file__)+'integer_mass_table.txt').read().strip().split('\n')
for i in range(len(massTable)):
	massTable[i] = massTable[i].split()
	
#set the total mass
Mass = 1024

#set the matrix
a = [[0,0]]+massTable
m = [i for i in range(Mass+1)]
matrix = numpy.zeros([len(a),len(m)])
for yi in range(len(a)):
	matrix[yi][0] = 1
	

for yi in range(1,len(a)):
	for xm in range(1,len(m)):
		if m[xm] >= int(a[yi][1]):
			matrix[yi][xm] = matrix[yi-1][xm]+matrix[yi][xm-int(a[yi][1])]
		else:
			matrix[yi][xm] = matrix[yi-1][xm]
			

for i in matrix:
	print(i)
	