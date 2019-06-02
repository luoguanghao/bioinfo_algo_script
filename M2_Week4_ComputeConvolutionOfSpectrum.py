'''
Spectral Convolution Problem: Compute the convolution of a spectrum.
	 Input: A collection of integers Spectrum.
	 Output: The list of elements in the convolution of Spectrum. If an element has multiplicity k, it should appear exactly k times;
	you may return the elements in any order.
---------------
Sample Input:
0 137 186 323
---------------
Sample Output:
137 137 186 186 323 49
'''


def ComputeConvolutionOfSpectrum(dataset):
	import numpy
	matrix = numpy.zeros([len(dataset),len(dataset)])
	for i in range(len(dataset)):
		for j in range(i):
			matrix[i][j] = dataset[i]-dataset[j]
	output = []
	for i in range(len(dataset)):
		for j in range(len(dataset)):
			if matrix[i][j]!=0:
				output.append(abs(int(matrix[i][j])))
	return output


from os.path import dirname
dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
dataset = [int(i) for i in dataset]
result = ComputeConvolutionOfSpectrum(dataset)
for i in result:
	print(i,end=' ')