'''
Code Challenge: Implement BetterBWMatching.
  >> Input: A string BWT(Text) followed by a collection of strings Patterns.
  >> Output: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns
     in Text.
-------------
Sample Input:
GGCGCCGC$TAGTCACACACGCCGTA
ACC CCG CAG
-------------
Sample Output:
1 2 1
-------------
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
			return 0
		#print(symbol,top,bottom)
		#input()
	return bottom - top + 1
	
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
	
if __name__ == '__main__':
	base2Num = {'$':0,'A':1,'C':2,'G':3,'T':4}
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
	LastColumn = list(dataset[0])
	patterns = dataset[1:]
	[FirstOccurrence,Count] = PreTreatment(LastColumn)
	#print(FirstOccurrence)
	#for i in Count:
	#	print(i)
	for p in patterns:
		output=BetterBWMatching(FirstOccurrence, LastColumn, p, Count)
		print(output,end = ' ')