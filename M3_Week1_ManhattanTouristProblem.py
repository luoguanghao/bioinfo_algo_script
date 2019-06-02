from os.path import dirname
import numpy

dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
n = int(dataset[0].split()[0])
m = int(dataset[0].split()[1])

matrixDown = numpy.zeros([n,(m+1)])
matrixRight = numpy.zeros([(n+1),m])

for i in range(n):
	matrixDown[i] = dataset[i+1].split()
	
for i in range(n+1):
	matrixRight[i] = dataset[i+n+2].split()

Graph = numpy.zeros([n+1,m+1])

for i in range(1,m+1):
	Graph[0][i] = matrixRight[0][i-1]+Graph[0][i-1]
for i in range(1,n+1):
	Graph[i][0] = matrixDown[i-1][0]+Graph[i-1][0]

for x in range(1,n+1):
	for y in range(1,m+1):
		Graph[x][y] = max(Graph[x-1][y]+matrixDown[x-1][y],Graph[x][y-1]+matrixRight[x][y-1])
	
print(Graph[-1][-1])