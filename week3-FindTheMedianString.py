def HMDisance(a,b):
	cnt = 0
	for i in range(len(a)):
		if(a[i]!=b[i]):
			cnt+=1
	return cnt
	
	
def d(pattern,texts):
	minVal=0
	for text in texts:
		minD=999999
		#minStr=''
		for i in range(len(text)-k+1):
			if  minD>HMDisance(pattern, text[i:i+k]):
				minD=HMDisance(pattern, text[i:i+k])
				#minStr=text[i:i+k]
		minVal+=minD
	
	return minVal
		


from os.path import dirname
import itertools

dataset = open(dirname(__file__)+'dataset.txt').read().split()

k=int(dataset[0])
stringset = dataset[1:]

aset = (itertools.product('ATGC',repeat=k))
s=[]
for i in aset:
	s.append(''.join(i))
	
	
minD=999999
median = set()
for pattern in s:	
	tmp=d(pattern,stringset)
	if tmp<minD:
		minD=tmp
		median.clear()
		median.add(pattern)
	elif tmp==minD:
		median.add(pattern)
		
print(median)
