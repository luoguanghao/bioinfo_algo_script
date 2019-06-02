'''
Code Challenge: Implement LeaderboardCyclopeptideSequencing.
     Input: An integer N and a collection of integers Spectrum.
     Output: LeaderPeptide after running LeaderboardCyclopeptideSequencing(Spectrum, N).
-------------------------------------------------
Sample Input:
10
0 71 113 129 147 200 218 260 313 331 347 389 460
-------------------------------------------------
Sample Output:
113-147-71-129

'''
maxn = 6000
AminoAcids = [[57], [71], [87], [97], [99], [101], [103], [113], [114], [115], [128], [129], [131], [137], [147], [156], [163], [186]]

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
			'''
			if i>=len(LBwithSocre):
				break
			'''
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


from os.path import dirname
massTable = open(dirname(__file__) + 'integer_mass_table.txt').read().strip().split('\n')
for i in range(len(massTable)):
	massTable[i] = massTable[i].split()
	massTable[i][1] = int(massTable[i][1])
massTable = dict(massTable)

dataset = open(dirname(__file__) + 'dataset.txt').read().strip().split()
N = int(dataset[0])
Spectrum = [int(i) for i in dataset[1:]]
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
	Leaderboard = Trim(Leaderboard,Spectrum,N)
	
	
#print(LeaderPeptide)
for i in range(len(LeaderPeptide)):
	if i != 0:
		print('-',end='')
	print(LeaderPeptide[i],end='')