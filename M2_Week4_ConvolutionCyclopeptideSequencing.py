'''
有瑕疵！！
Code Challenge: Implement ConvolutionCyclopeptideSequencing.
     Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
     Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of
     Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).
----------------
Sample Input:
20
60
57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493
----------------
Sample Output:
99-71-137-57-72-57
'''

maxn = 6000
def getMass(Peptide):
	return sum(Peptide)
	
def cyclospectrum(Peptide):
	spectrum = []
	for k in range(1,len(Peptide)):
		for i in range(len(Peptide)):
			element = Peptide[i:i+k]
			if k-len(Peptide)+i>0:
				element += Peptide[:k-len(Peptide)+i]
			spectrum.append(sum(element))
	spectrum += [0,sum(Peptide)]
	spectrum.sort()
	return spectrum

def linearSpectrum(Peptide):
	output = []
	for k in range(1,len(Peptide)):
		for i in range(len(Peptide)):
			element = Peptide[i:i+k]
			output.append(sum(element))
	output += [0,sum(Peptide)]
	return output

def cycScore(Peptide,Spectrum):
	TheorSpectrum = cyclospectrum(Peptide)
	bucketThSptm = [0]*maxn
	for item in TheorSpectrum:
		bucketThSptm[item] += 1
	bucketSptm = [0]*maxn
	for item in Spectrum:
		bucketSptm[item] += 1
	score = 0
	for i in range(maxn):
		if bucketSptm[i]<bucketThSptm[i]:
			score += bucketSptm[i]
		else:
			score += bucketThSptm[i]
	return score

def linearScore(Peptide,Spectrum):
	TheorSpectrum = linearSpectrum(Peptide)
	bucketThSptm = [0]*maxn
	for item in TheorSpectrum:
		bucketThSptm[item] += 1
	bucketSptm = [0]*maxn
	for item in Spectrum:
		bucketSptm[item] += 1
	score = 0
	for i in range(maxn):
		if bucketSptm[i]<bucketThSptm[i]:
			score += bucketSptm[i]
		else:
			score += bucketThSptm[i]
	return score

def Trim(Leaderboard,Spectrum,N):
	LBwithSocre = []
	for item in Leaderboard:
		LBwithSocre.append([item,linearScore(item, Spectrum)])
	LBwithSocre = sorted(LBwithSocre,key=lambda x:x[1],reverse=True)
	output = []
	if N < len(LBwithSocre):
		scoreLast = LBwithSocre[N-1][1]
		i = 0
		while(LBwithSocre[i][1]>=scoreLast):
			output.append(LBwithSocre[i][0])
			i+=1
			#?
			if i>=len(LBwithSocre):
				break
			#?
	else:
		output = [i[0] for i in LBwithSocre]
					
	return output
	
def Expand(Leaderboard):
	if Leaderboard == []:
		return [i for i in AminoAcids]
	output = []
	for aa in AminoAcids:
		for item in Leaderboard:
			output.append(item+aa)
	return output



def ComputeConvolutionOfSpectrum(dataset,n):
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
	bucket = [[0,0]for i in range(2500)]

	for item in output:
		bucket[item][1] += 1
		bucket[item][0] = item
	bucket = sorted(bucket,key=lambda x:x[1],reverse=True)
	lastCnt = bucket[n-1][1]

	i=0
	output = []
	while(i<2500):
		if bucket[i][1]<lastCnt:
			break
		if 57<=bucket[i][0] and bucket[i][0]<=200:
			output.append(bucket[i][0])
		i+=1
	
	return output



from os.path import dirname
dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
m = int(dataset[0]) #leaderboard restrict
n = int(dataset[1]) #Amino acids restrict
Spectrum = [int(i) for i in dataset[2:]]
AminoAcids = [[i] for i in  ComputeConvolutionOfSpectrum(Spectrum,n)]


Spectrum.sort()
parentMass = Spectrum[-1]
Leaderboard = []
LeaderPeptide = []
flag = True
while(len(Leaderboard)>0 or flag):
	flag = False
	Leaderboard = Expand(Leaderboard)
	tmpLeaderboard = Leaderboard[:] ##deep Copy
	for item in tmpLeaderboard:
		if getMass(item)==parentMass:
			if cycScore(item, Spectrum) > cycScore(LeaderPeptide, Spectrum):
				LeaderPeptide = item
		elif getMass(item)>parentMass:
			Leaderboard.remove(item)
	Leaderboard = Trim(Leaderboard,Spectrum,m)
	
#print(LeaderPeptide)
for i in range(len(LeaderPeptide)):
	if i != 0:
		print('-',end='')
	print(LeaderPeptide[i],end='')
