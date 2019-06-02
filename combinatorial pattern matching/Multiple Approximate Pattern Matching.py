from os.path import dirname
import numpy as np

def PreTreatment(LastColumn):
	rearOrder = [0 for i in range(len(LastColumn))]
	count_d = {'$':0,'A':0,'C':0,'G':0,'T':0}
	for i in range(len(LastColumn)):
		count_d[LastColumn[i]] += 1
		rearOrder[i] = count_d[LastColumn[i]]		
	FirstOccurrence = {'$':0,'A':0,'C':0,'G':0,'T':0}
	cnt = 0
	for key in FirstOccurrence.keys():
		FirstOccurrence[key] = cnt
		cnt += count_d[key]		
	return [FirstOccurrence,count_d,rearOrder]
	
	
def Approx_PatternMatching(pattern):
	'''
	#print(len(disMatch))
	symbol = pattern[-1]
	pattern = pattern[:-1]

	top = FirstOccurrence[symbol]
	bottom = top + count_d[symbol]
	pointer = [[i,0] for i in list(range(top,bottom))]
	#print(pointer)
	'''
	pointer = [[i,0] for i in list(range(len(LastColumn)))]
	while(len(pattern)):
		tmppointer = []
		symbol = pattern[-1]
		#print(symbol,pointer)
		pattern = pattern[:-1]
		flag = False
		for i in pointer:
			#print('#',i)
			if LastColumn[i[0]]==symbol:
				flag = True
				tmppointer.append([FirstOccurrence[LastColumn[i[0]]]+rearOrder[i[0]]-1,i[1]])
				#print(i,tmppointer[-1])
				#input()
			else:
				if i[1]+1 <= k:
					flag = True
					tmppointer.append([FirstOccurrence[LastColumn[i[0]]]+rearOrder[i[0]]-1,i[1]+1])
				
		if not flag:
			return []
		#print('to',tmppointer)
		#input()
		pointer = tmppointer
	#print(symbol,pointer)
	output = []
	for i in pointer:
		output.append(suffixArray[i[0]])	
	return output
		

def Burrows_and_Wheeler(text):
	SuffixList = []
	for i in range(len(text)):
		SuffixList.append([i,text[i:]+text[:i]])
	SuffixList = sorted(SuffixList,key=lambda x: x[1])
	LastColumn = [i[1][-1] for i in SuffixList]
	suffixArray = [i[0] for i in SuffixList]
	#for i in range(len(SuffixList)):
	#	print(i,'***** ',' '.join(SuffixList[i][1]),' ********')
	return [LastColumn,suffixArray]
	
if __name__ == '__main__':
	base2Num = {'$':0,'A':1,'C':2,'G':3,'T':4}
	#text = 'ACATGCTACTTT'
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
	text = dataset[0]
	patterns = dataset[1:-1]
	k = int(dataset[-1])
	text = list(text)+['$']
	#patterns = ['ATT' ,'GCC' ,'GCTA' ,'TATT']
	
	[LastColumn,suffixArray] = Burrows_and_Wheeler(text)
	[FirstOccurrence,count_d,rearOrder] = PreTreatment(LastColumn)
	#print(LastColumn)
	#print(sorted(LastColumn))
	#print('rearorder',rearOrder)
	#print(Approx_PatternMatching('GCC'))
	
	output = []
	for p in patterns:
		output += Approx_PatternMatching(p)
	output.sort()
	for i in output:
		print(i,end=' ')
	