
from os.path import dirname
import numpy

def OpNumber(a):
	return -a

def Print(P):
	for i in range(len(P)):
		if i == 0:
			print('(',end='')
		else:
			print(' ',end='')
		if P[i]<0:
			print(str(P[i]),end='')
		else:
			print('+'+str(P[i]),end='')
	print(')')

def GreedySorting():
	global P
	global cnt
	for i in range(1,len(P)):
		if P[i]!=i:
			if P[i]==-i:
				P[i] = i
				cnt += 1
				Print(P[1:])
			else:
				try:
					indx = P.index(i)
				except ValueError:
					indx = P.index(-i)
				# reverse
				P[i:indx+1]=P[i:indx+1][::-1]
				P[i:indx+1]=list(map(OpNumber, P[i:indx+1]))
				cnt += 1
				Print(P[1:])
				#
				if P[i] == -i:
					P[i] = i
					cnt += 1
					Print(P[1:])
			

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip()
	P = [0]+dataset[1:-1].split()
	P = list(map(int,P))
	cnt=0
	print(P)
	GreedySorting()
	