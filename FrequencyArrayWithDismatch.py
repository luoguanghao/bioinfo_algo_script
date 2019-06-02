dict = {'A':0,'C':1,'G':2,'T':3}
dict2 = {0:'A',1:'C',2:'G',3:'T'}

def GetIndx(s):
	
	out = 0
	for i in s:
		out = out*4 + dict[i]
		
	return out
	
	
def GetS(num,k):
	s = ''
	
	for i in range(k):
		s += dict2[num%4]
		num = int(num/4)
	return s[::-1]
	
	
def HMDisance(a,b):
	cnt = 0
	for i in range(len(a)):
		if(a[i]!=b[i]):
			cnt+=1
	return cnt

def Neighbors(a,d):
	if d==0:
		return [a]
	if len(a)==1:
		return ['G','A','C','T']
		
	neighborhood = []
	
	suffixNeibh = Neighbors(a[1:], d)
	
	for item in suffixNeibh:
		if HMDisance(item, a[1:])<d:
			for x in ['C','T','G','A']:
				neighborhood.append(x+item)
		elif HMDisance(item, a[1:])==d:
			neighborhood.append(a[0]+item)
		
	return neighborhood
	

def SFWMP(text,k,d):
	lt = len(text)
	lp = k
	
	frequencyArray = [0]*4**k
	
	for i in range(lt-k+1):
		similarArray=Neighbors(text[i:i+k],d)
		for item in similarArray:
			frequencyArray[GetIndx(item)] += 1
	
	dict={'A':'T','T':'A','G':'C','C':'G'}
	text=text[::-1]
	retext=''
	for i in text:
		retext+=dict[i]
	
	
	for i in range(lt-k+1):
		similarArray=Neighbors(retext[i:i+k],d)
		for item in similarArray:
			frequencyArray[GetIndx(item)] += 1
	
	return frequencyArray

from os.path import dirname

dataset = open(dirname(__file__)+'dataset.txt').read().split()
text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
d=1
k=4
'''
rawtext=''
for i in dataset:
	rawtext+=i
text=rawtext[3764790:3764910]
d=1
k=9
'''

frequencyArray = SFWMP(text, k, d)
out = []
maxVal=0
for i in range(len(frequencyArray)):
	#if frequencyArray[i]>0:
		#print(GetS(i, k),frequencyArray[i])
	if frequencyArray[i]>maxVal:
		maxVal=frequencyArray[i]
		out.clear()
		out.append(GetS(i, k))
	elif frequencyArray[i]==maxVal:
		out.append(GetS(i, k))

for i in out:
	print(i,end=' ')