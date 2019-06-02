from os.path import dirname
from InPutTable import InPut_Integer_Mass_Table


def problem(Spectral_Vector):
	INF = float('inf')
	m = len(Spectral_Vector)
	IMTable = list((InPut_Integer_Mass_Table()[0]).items())
	l = len(IMTable)
	dp = [-INF for i in range(m+1)]
	pre = [-1 for i in range(m+1)]
	dp[0] = 0
	for i in range(m+1):
		for aa in range(l):
			if i-IMTable[aa][1]>=0 and dp[i]<dp[i-IMTable[aa][1]]+Spectral_Vector[i-1]:
				dp[i] = dp[i-IMTable[aa][1]]+Spectral_Vector[i-1]
				pre[i] = i-IMTable[aa][1]
	
	IMTable = InPut_Integer_Mass_Table()[1]
	path = []
	while i!=0:
		path = [i]+path
		i = pre[i]
	cnt = 0
	for i in path:
		print(IMTable[i-cnt],end='')
		cnt = i

if __name__ == '__main__':
	Spectral_Vector = list(map(int,open(dirname(__file__)+'dataset.txt').read().strip().split()))
	
	#print(len(Spectral_Vector))
	
	problem(Spectral_Vector)