'''
Code Challenge: Solve the Multiple Pattern Matching Problem.
     Input: A string Text followed by a collection of strings Patterns.
     Output: All starting positions in Text where a string from Patterns appears as a substring.
_-_-_-_-_-_-_-_-_-_-_-_-
Sample Input:
AATCGGGTTCAATCGGGGT
ATCG
GGGT
_-_-_-_-_-_-_-_-_-_-_-_-
Sample Output:
1 4 11 15
_-_-_-_-_-_-_-_-_-_-_-_-
Lo Kwongho 2018.9
'''

from os.path import dirname
import numpy as np

def BetterBWMatching(FirstOccurrence, LastColumn, Pattern, Count):
	top = 0
	bottom = len(LastColumn)-1
	while(len(Pattern)):
		symbol = Pattern[-1]
		Pattern = Pattern[:-1]
		topRank = Count[top][base2Num[symbol]]+1
		bottomRank = Count[bottom+1][base2Num[symbol]]
		if bottomRank > 0:
			top = FirstOccurrence[symbol] + topRank - 1
			bottom = FirstOccurrence[symbol] + bottomRank - 1
		else:
			return []
		#print(symbol,top,bottom)
		#input()
	output = []
	for i in range(top,bottom+1):
		output.append(suffixArray[i])
	return output
	
def PreTreatment(LastColumn):
	count_d = {'$':0,'A':0,'C':0,'G':0,'T':0}
	for i in LastColumn:
		count_d[i] += 1
	FirstOccurrence = {'$':0,'A':0,'C':0,'G':0,'T':0}
	cnt = 0
	for key in FirstOccurrence.keys():
		FirstOccurrence[key] = cnt
		cnt += count_d[key]
	Count = np.zeros(shape=(len(LastColumn)+1,5),dtype=int)
	for i in range(1,len(LastColumn)+1):
		Count[i] = Count[i-1]
		Count[i][base2Num[LastColumn[i-1]]] += 1
		
	return [FirstOccurrence,Count]

def Burrows_and_Wheeler(text):
	SuffixList = []
	for i in range(len(text)):
		SuffixList.append([i,text[i:]+text[:i]])
	SuffixList = sorted(SuffixList,key=lambda x: x[1])
	LastColumn = [i[1][-1] for i in SuffixList]
	suffixArray = [i[0] for i in SuffixList]
	return [LastColumn,suffixArray]

if __name__ == '__main__':
	base2Num = {'$':0,'A':1,'C':2,'G':3,'T':4}
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
	text = list(dataset[0])
	patterns = dataset[1:]
	[LastColumn, suffixArray] = Burrows_and_Wheeler(text)
	[FirstOccurrence,Count] = PreTreatment(LastColumn)
	#print(FirstOccurrence)
	#for i in Count:
	#	print(i)
	output = []
	for p in patterns:
		output += BetterBWMatching(FirstOccurrence, LastColumn, p, Count)
	
	output.sort()
	for i in output:
		print(i,end=' ')	
	