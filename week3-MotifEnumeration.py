
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


from os.path import dirname

dataset = open(dirname(__file__)+'dataset.txt').read().split()

k = int(dataset[0])
d = int(dataset[1])

s=set()
for i in range(2,len(dataset)):
	l1=len(dataset[i])
	for indx in range(l1-k+1):
		neighborhood = Neighbors(dataset[i][indx:indx+k],d)
		for pattern in neighborhood:
			tolflag=0
			for line in range(2,len(dataset)):
				if line!=i:
					flag=0
					l2=len(dataset[line])
					for j in range(l2-k+1):
						if HMDisance(pattern, dataset[line][j:j+k])<=d:
							flag=1
					tolflag+=flag
			if tolflag+1==len(dataset)-2:
				s.add(pattern)
			
						
for i in s:
	print(i,end=' ')