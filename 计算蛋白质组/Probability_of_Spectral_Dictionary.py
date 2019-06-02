'''
CODE CHALLENGE: Solve the Probability of Spectral Dictionary Problem.
     Given: A spectral vector Spectrum', an integer threshold, and an integer max_score.
     Return: The probability of the dictionary Dictionarythreshold(Spectrum').

code : Lo Kwongho 2018.12

好好想想这个概率是怎么算出来的
'''
from os.path import dirname
from InPutTable import InPut_Integer_Mass_Table

def Probability(Spectrum_Vector,threshold,max_score):
	IMTable = InPut_Integer_Mass_Table()[0].items()
	l = len(Spectrum_Vector)
	dp =dict([(j,[0 for i in range(l+1)]) for j in range(-(max_score),max_score+1)])
	dp[0][0] = 1
	#print(dp[-1])
	
	
	for i in range(l+1):
		for j in range(-(max_score),max_score+1):
			if dp[j][i]>0:
				for aa in IMTable:
					if aa[1]+i<=l and -max_score<=j+Spectrum_Vector[aa[1]+i-1] and j+Spectrum_Vector[aa[1]+i-1]<=max_score:
						dp[j+Spectrum_Vector[aa[1]+i-1]][aa[1]+i] += (1/20)*dp[j][i]
	#for i in range(-(max_score),max_score+1):
	#	print(i,':',dp[i])
	cnt = 0
	for i in range(threshold,max_score+1):
		cnt += dp[i][-1]
	print("%.9f"%cnt)
	

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	Spectrum_Vector = list(map(int,dataset[0].split()))
	threshold = int(dataset[1])
	max_score = int(dataset[2])
	#print(Spectrum_Vector)
	Probability(Spectrum_Vector,threshold,max_score)
	