import random
from os.path import dirname
from numpy.random import choice
from collections import Counter
import numpy as np
dict = {'A':0,'C':1,'G':2,'T':3}

def randInitialize(stringSet,k,t):
	martrix = []
	m = len(stringSet[0])-k
	for i in range(t):
		indx = random.randint(0,m)
		martrix.append(stringSet[i][indx:indx+k])
	return martrix

def GetProfile(Motifs,expt,k):
	profile = np.zeros([4,k])
	size = len(Motifs)
	for i in range(k):
		for j in range(size):
			if j != expt:
				profile[dict[ Motifs[j][i] ]][i] += 1
	profile += 1
	profile /= (size+4-1)
	return profile
	
def countTheProbable(pattern,profile):
	cnt=1
	for i in range(len(pattern)):
		cnt *= float(profile[dict[pattern[i]]][i])
	return cnt

def GetTheIndxRand(profile,string,k):
	p = []
	sump=0
	l = len(string)
	for i in range(l-k+1):
		p.append(countTheProbable(string[i:i+k], profile))
		sump += p[-1]
	for i in range(l-k+1):
		p[i]=p[i]/sump
	return np.random.choice(a=range(l-k+1),size=1,replace=False,p=p)
	
def Score(Motifs,k):
	size = len(Motifs)
	cnt = k*len(Motifs)
	for i in zip(*Motifs):
		cnt -= int(Counter(i).most_common(1)[0][1])	
	return cnt
	
####
def countTheProbable(pattern,profile):
	cnt=1
	for i in range(len(pattern)):
		cnt *= float(profile[dict[pattern[i]]][i])
	return cnt
	
def FindMostProbable(text,profile):	
	lt = len(text)
	maxVal = -1
	maxSeq = ''
	for i in range(lt-k+1):
		pattern = text[i:i+k]
		if maxVal<countTheProbable(pattern,profile):
			maxVal=countTheProbable(pattern,profile)
			maxSeq = pattern
		
	return maxSeq

def GetMartix(profile,stringSet,t):
	martrix = []
	for i in range(t):
		martrix.append(FindMostProbable(stringSet[i],profile))
	return martrix
####


dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
k = int(dataset[0])
t = int(dataset[1])
N = int(dataset[2])
'''
stringSet = dataset[3:]
bestK_mers = randInitialize(stringSet,k,t)
profile = GetProfile(bestK_mers,1,k)
print( GetTheIndxRand(profile, stringSet[1], k) )

'''

stringSet = dataset[3:]

allbestScore = 99999999
allbestK_mers = []
'''
for i in range(500):
	bestK_mers = randInitialize(stringSet,k,t)
	bestScore = Score(bestK_mers,k)

	while(1):
		profile = GetProfile(bestK_mers,-1,k)
		martrix = GetMartix(profile,stringSet,t)
		tmpScore = Score(martrix,k)
		if tmpScore < bestScore:
			bestScore = tmpScore
			bestK_mers = martrix
		else:
			break
	if bestScore<allbestScore :
		allbestScore = bestScore
		allbestK_mers = bestK_mers


for i in allbestK_mers:
	print (i)
'''		
allbestScore = 99999999
allbestMotifs = []

for time in range(N):
	#bestK_mers = allbestK_mers
	bestK_mers = randInitialize(stringSet,k,t)
	bestScore = Score(bestK_mers,k)
	K_mers = bestK_mers
	for j in range(N):
		expt = random.randint(0,t-1)
		profile = GetProfile(K_mers,expt,k)
		indx = GetTheIndxRand(profile,stringSet[expt],k)
		K_mers[expt] = stringSet[expt][indx[0]:indx[0]+k]
		tmpScore = Score(K_mers,k)
		if tmpScore < bestScore:
			bestScore = tmpScore
			bestK_mers = K_mers

	if bestScore<allbestScore:
		allbestScore=bestScore
		allbestMotifs = bestK_mers
		
for i in allbestMotifs:
	print (i)
	