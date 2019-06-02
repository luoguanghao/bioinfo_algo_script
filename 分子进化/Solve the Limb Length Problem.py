import numpy as np
from os.path import dirname




if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	n = int(dataset[0])
	v2 = int(dataset[1])
	matrix = [list(map(int,line.split())) for line in dataset[2:]]
	#print(matrix)
	limbLen = 999999
	for i in range(n):
		for j in range(n):
			if v2!=i and v2!=j:
				tmp = (matrix[v2][i]+matrix[v2][j]-matrix[i][j])/2
				if tmp<limbLen:
					limbLen = tmp
	print(int(limbLen))