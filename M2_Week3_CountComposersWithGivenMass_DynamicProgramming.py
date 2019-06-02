import numpy
Mass = 1024
#weight
a1 = [0,2,3,7,10]
a = [0,57,71,87,97,99,101,103,113,113,114,115,128,
	 128,129,131,137,147,156,163,186]
#
m = [i for i in range(Mass+1)]
Matrix = numpy.zeros([len(a),len(m)])
	
for y in range(len(a)):
	Matrix[y][0] = 1
'''	
for i in Matrix:
	print(i)
'''

for yi in range(1,len(a)):
	for xm in range(1,len(m)):
		if m[xm]>=a[yi]:
			Matrix[yi][xm] = Matrix[yi-1][xm] + Matrix[yi][xm-a[yi]]
		else:
			Matrix[yi][xm] = Matrix[yi-1][xm]
		
for i in Matrix:
	print(i)