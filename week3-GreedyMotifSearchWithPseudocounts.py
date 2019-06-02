'''
Code Challenge: Implement GreedyMotifSearch.
	Input: Integers k and t, followed by a collection of strings Dna.
	Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t).
	If at any step you find more than one Profile-most probable k-mer in a given string, use the
	one occurring first.

Note: If you are not satisfied with the performance of ﻿GreedyMotifSearch — even if you implemented it correctly — then wait until we discuss this algorithm in the next lesson.
-------
Sample Input:
3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG
-------
Sample Output:
CAG
CAG
CAA
CAA
CAA
-------
coder Lo Kwongho 2018.9
'''

dict = {'A':0,'C':1,'G':2,'T':3}

from os.path import dirname
import numpy as np
from collections import Counter

def Score(Motifs,k):
	size = len(Motifs)
	cnt = k*len(Motifs)
	for i in zip(*Motifs):
		cnt-=int(Counter(i).most_common(1)[0][1])	
	return cnt

def GetProfile(Motifs,k):
	profile = np.zeros([4,k])
	size = len(Motifs)
	for i in range(k):
		for j in range(size):
			profile[dict[ Motifs[j][i] ]][i] += 1
	profile += 1
	profile /= (size+4)
	return profile

def InitializeBestMotifs(stringSet,k,t):
	bestMotifs = []
	for i in range(t):
		bestMotifs.append(stringSet[i][0:k])
	return bestMotifs

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
	
def GreedyMotifSearchWithPseudocounts():
	bestMotifs = InitializeBestMotifs(stringSet,k,t)
	bestScore = Score(bestMotifs, k)
	lt = len(stringSet[0])
	bestScore = Score(bestMotifs, k)
	for i in range(lt-k+1):
		Motifs = [stringSet[0][i:i+k]]
		for j in range(1,t):
			profile = GetProfile(Motifs,k)
			Motifs.append(FindMostProbable(stringSet[j],profile))
		score = Score(Motifs,k)
		if score<bestScore:
			bestMotifs = Motifs
			bestScore = score
	return [bestScore,bestMotifs]
	

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()

	k=int(dataset[0])
	t = int(dataset[1])
	stringSet = dataset[2:]

	[bestScore,bestMotifs] = GreedyMotifSearchWithPseudocounts()
	
	for i in bestMotifs:
		print(i,)
	print(bestScore)
	