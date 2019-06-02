
def Sigma(m,a,matrix):
	sig = 0
	for ai in a:
		sig += matrix[m-ai]
	return sig
# weight
a = [0,57,71,87,97,99,101,103,113,114,115,
	 128,129,131,137,147,156,163,186]
#
Mass = int(input())
matrix = [0]*(Mass+1)
matrix[0] = 1

for m in range(1,len(matrix)):
	matrix[m] = Sigma(m,a,matrix)
print(matrix)
