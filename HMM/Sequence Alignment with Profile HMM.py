'''
不完善
Sequence Alignment with Profile HMM Problem

Given: A string Text, a multiple alignment Alignment, a threshold θ, and a pseudocount σ.

Return: An optimal hidden path emitting Text in HMM(Alignment,θ,σ).

http://rosalind.info/problems/ba10g/

@ Lo Kwongho 2018.9
'''

from os.path import dirname
import numpy
import math

def preTreat(mutli_Alig):
	tmpMutli_Align = [i for i in zip(*mutli_Alig)]
	miss = [0 for i in range(len(tmpMutli_Align))]
	miss_cnt = 0
	for i in range(len(tmpMutli_Align)):
		if float(tmpMutli_Align[i].count('-')) >= threshold*len(tmpMutli_Align[i]):
			miss[i] = 1
			miss_cnt += 1
	
	return [miss,miss_cnt]

def ProfileHMM():
	size = (len(mutli_Alig[0])-miss_cnt)*3+3
	print((len(mutli_Alig[0])-miss_cnt))
	l = len(mutli_Alig[0])
	n = len(mutli_Alig)
	
	state_num = {}
	state_num['S0'] = 0
	state_num['I0'] = 1
	idx = 2
	for i in range(l-miss_cnt):
		state_num['M'+str(i+1)] = idx
		idx += 1
		state_num['D'+str(i+1)] = idx
		idx += 1
		state_num['I'+str(i+1)] = idx
		idx += 1
	state_num['E'] = idx
	emission = numpy.zeros(shape=(size,len(alphabet)))
	transition = numpy.zeros(shape=(size,size),dtype=float)
	for text in mutli_Alig:
		state = 'S'
		p = 0	
		for i in range(l):
			if miss[i]==1:
				if text[i]!='-':
					transition[state_num[state+str(p)]][state_num['I'+str(p)]] += 1
					emission[state_num['I'+str(p)]][alphabet[text[i]]] += 1
					state = 'I'
			else:
				p += 1
				if text[i]=='-':
					transition[state_num[state+str(p-1)]][state_num['D'+str(p)]] += 1
					state = 'D'
				else:
					transition[state_num[state+str(p-1)]][state_num['M'+str(p)]] += 1
					emission[state_num['M'+str(p)]][alphabet[text[i]]] += 1
					state = 'M'
		if state=='I':
			transition[state_num[state+str(p)]][state_num['E']] += 1
		else:
			transition[state_num[state+str(p)]][state_num['E']] += 1
	# transition
	for i in range(size):
		csum = float(sum(transition[i]))
		if csum > 0:
			for j in range(size):
				transition[i][j] /= csum	
	for x in range(2):
		csum = 0
		for y in range(1,4):
			transition[x][y] += theta
			csum += transition[x][y]
		for y in range(1,4):
			transition[x][y] /= csum
	for i in range(2,size-4,3):
		for x in range(i,i+3):
			csum = 0
			for y in range(i+2,i+5):
				transition[x][y] += theta
				csum += transition[x][y]
			for y in range(i+2,i+5):
				transition[x][y] /= csum
	for x in range(size-4,size-1):
		csum = 0
		for y in range(size-2,size):
			transition[x][y] += theta
			csum += transition[x][y]
		for y in range(size-2,size):
			transition[x][y] /= csum		
	#
	# emission
	for i in range(size):
		csum = sum(emission[i])
		if csum > 0:
			for j in range(len(alphabet)):
				emission[i][j] /= csum
	for x in range(1,size-1):
		if x%3 != 0:
			csum = 0
			for y in range(len(alphabet)):
				emission[x][y] += theta
				csum += emission[x][y]
			for y in range(len(alphabet)):
				emission[x][y] /= csum
				if 0.005<=emission[x][y] and emission[x][y]<0.01:
					emission[x][y] = 0.01
	
	keys = list(state_num.keys())
	keys[0] = 'S'
	
	'''
	print('\t'+'\t'.join(keys))
	for i in range(size):
		print(keys[i],end='')
		for j in range(size):
			if 0.005<=transition[i][j] and transition[i][j]<0.01:
				transition[i][j]=0.01
			elif 0.005>transition[i][j]:
				transition[i][j] = 0
			print('\t%.3g'%transition[i][j],end='')
		print('')
		
	print('--------\n')
	
	print('\t'+'\t'.join(list(alphabet.keys())))
	for i in range(size):
		print(keys[i],end='')
		for j in range(len(alphabet)):
			#if 0.005<=emission[i][j] and emission[i][j]<0.01:
			#	emission[i][j]=0.01
			print('\t%.3g'%emission[i][j],end='')
		print('')
	'''	
	return [transition,emission,state_num]		
	
########### Sequence Alignment with Profile HMM
def Prepare_for_HMM_Path():
	h = (len(mutli_Alig[0])-miss_cnt)*3+1
	l = len(text)
	Graph = numpy.zeros(shape=(h,l),dtype=float)
	track = [[(-1,-1) for i in range(l)] for j in range(h)]

	state_num = {}

	state_num['I0'] = 0
	idx = 1
	for i in range(len(mutli_Alig[0])-miss_cnt):
		state_num['M'+str(i+1)] = idx
		idx += 1
		state_num['D'+str(i+1)] = idx
		idx += 1
		state_num['I'+str(i+1)] = idx
		idx += 1
	return [h,l,state_num,Graph,track]	
		
def HMM_Path():
	[h,l,state_num,Graph,track] = Prepare_for_HMM_Path()
		
	# #0 column
	Graph[2][0] = math.log(transition[sn['S0']][sn['D1']])
	track[2][0] = (0,0)
	for x in range(5,h,3):
		pre = sn['D'+str(math.ceil((x-3)/3))]
		rear = sn['D'+str(math.ceil(x/3))]
		Graph[x][0] = Graph[x-3][0]+math.log(transition[pre][rear])
		track[x][0] = ((x-3),0)
		
	# #1 column
	c = alphabet[text[1]]
	Graph[0][1] = math.log(transition[sn['S0']][sn['I0']]*emission[sn['I0']][c])
	track[0][1] = (0,0)
	for x in range(1,h):
		idx = str(math.ceil(x/3))
		preIdx = str(math.ceil((x-3)/3))
		if x%3==1:   # M ##########
			if x <= 2:
				Graph[x][1]=math.log( transition[0][sn['M'+idx]]*emission[sn['M'+idx]][c] )
				track[x][1]=(0,0)
				continue
			Graph[x][1]=Graph[state_num['D'+preIdx]][0]+math.log( transition[sn['D'+preIdx]][sn['M'+idx]]*emission[sn['M'+idx]][c] )
			track[x][1]=(state_num['D'+preIdx],0)
		elif x%3==2: # D ###########
			if x <= 2:
				Graph[x][1]=Graph[state_num['I0']][1]+math.log( transition[sn['I'+preIdx]][sn['D'+idx]] )
				track[x][1]=(state_num['I0'],1)
				continue
			Graph[x][1]=max(Graph[state_num['M'+preIdx]][1]+math.log(transition[sn['M'+preIdx]][sn['D'+idx]]),
							Graph[state_num['D'+preIdx]][1]+math.log(transition[sn['D'+preIdx]][sn['D'+idx]]),
							Graph[state_num['I'+preIdx]][1]+math.log(transition[sn['I'+preIdx]][sn['D'+idx]]) )
			
			if Graph[x][1]==Graph[state_num['M'+preIdx]][1]+math.log(transition[sn['M'+preIdx]][sn['D'+idx]]):
				track[x][1] = (state_num['M'+preIdx],1)
			elif Graph[x][1]==Graph[state_num['D'+preIdx]][1]+math.log(transition[sn['D'+preIdx]][sn['D'+idx]]):
				track[x][1] = (state_num['D'+preIdx],1)
			else:
				track[x][1] = (state_num['I'+preIdx],1)
		else:	     # I ###########
			Graph[x][1]=Graph[state_num['D'+idx]][0]+math.log(transition[sn['D'+idx]][sn['I'+idx]]*emission[sn['I'+idx]][c])
			track[x][1] = (state_num['D'+idx],0)
	# common
	
	for y in range(2,l):
		c = alphabet[text[y]]
		Graph[0][y] = Graph[0][y-1]+math.log(transition[sn['I0']][sn['I0']]*emission[sn['I0']][c])
		track[0][y] = (0,y-1)
		for x in range(1,h):
			idx = str(math.ceil(x/3))
			preIdx = str(math.ceil((x-3)/3))
			if x%3==1:   # M
				if x <= 2:
					Graph[x][y]=Graph[state_num['I0']][y-1]+math.log(transition[sn['I'+preIdx]][sn['M1']]*emission[sn['M1']][c])
					track[x][y] = (state_num['I0'],y-1)
					continue
				Graph[x][y]=max(Graph[state_num['M'+preIdx]][y-1]+math.log(transition[sn['M'+preIdx]][sn['M'+idx]]*emission[sn['M'+idx]][c]),
								Graph[state_num['D'+preIdx]][y-1]+math.log(transition[sn['D'+preIdx]][sn['M'+idx]]*emission[sn['M'+idx]][c]),
								Graph[state_num['I'+preIdx]][y-1]+math.log(transition[sn['I'+preIdx]][sn['M'+idx]]*emission[sn['M'+idx]][c]) )
				
				if Graph[x][y]==Graph[state_num['M'+preIdx]][y-1]+math.log(transition[sn['M'+preIdx]][sn['M'+idx]]*emission[sn['M'+idx]][c]):
					track[x][y]=(state_num['M'+preIdx],y-1)
				elif Graph[x][y]==Graph[state_num['D'+preIdx]][y-1]+math.log(transition[sn['D'+preIdx]][sn['M'+idx]]*emission[sn['M'+idx]][c]):
					track[x][y]=(state_num['D'+preIdx],y-1)
				else:
					track[x][y]=(state_num['I'+preIdx],y-1)
				
			elif x%3==2: # D
				if x <= 2:
					Graph[x][y]=Graph[state_num['I0']][y]+math.log(transition[sn['I0']][sn['D'+idx]])
					track[x][y]=(state_num['I0'],y)
					continue
				Graph[x][y]=max(Graph[state_num['M'+preIdx]][y]+math.log(transition[sn['M'+preIdx]][sn['D'+idx]]),
								Graph[state_num['D'+preIdx]][y]+math.log(transition[sn['D'+preIdx]][sn['D'+idx]]),
								Graph[state_num['I'+preIdx]][y]+math.log(transition[sn['I'+preIdx]][sn['D'+idx]]) )
				
				if Graph[x][y]==Graph[state_num['M'+preIdx]][y]+math.log(transition[sn['M'+preIdx]][sn['D'+idx]]):
					track[x][y]=(state_num['M'+preIdx],y)
				elif Graph[x][y]==Graph[state_num['D'+preIdx]][y]+math.log(transition[sn['D'+preIdx]][sn['D'+idx]]):
					track[x][y]=(state_num['D'+preIdx],y)
				else:
					track[x][y]=(state_num['I'+preIdx],y)
				
			else:	     # I
				Graph[x][y]=max(Graph[state_num['M'+idx]][y-1]+math.log(transition[sn['M'+idx]][sn['I'+idx]]*emission[sn['I'+idx]][c]),
								Graph[state_num['D'+idx]][y-1]+math.log(transition[sn['D'+idx]][sn['I'+idx]]*emission[sn['I'+idx]][c]),
								Graph[state_num['I'+idx]][y-1]+math.log(transition[sn['I'+idx]][sn['I'+idx]]*emission[sn['I'+idx]][c]) )
								
				if Graph[x][y]==Graph[state_num['M'+idx]][y-1]+math.log(transition[sn['M'+idx]][sn['I'+idx]]*emission[sn['I'+idx]][c]):
					track[x][y]=(state_num['M'+idx],y-1)
				elif Graph[x][y]==Graph[state_num['D'+idx]][y-1]+math.log(transition[sn['D'+idx]][sn['I'+idx]]*emission[sn['I'+idx]][c]):
					track[x][y]=(state_num['D'+idx],y-1)
				else:
					track[x][y]=(state_num['I'+idx],y-1)
	'''
	for i in Graph:
		for j in i:
			print('{:.2f}'.format(j),end=' ')
		print('')
	print('-_'*20)
	for i in track:
		for j in i:
			print(j,end=' ')
		print('')
	'''	
	return [Graph,track]

def TrackBack(Graph,track):
	[h,l] = numpy.shape(Graph)
	maxId = -1
	maxValue = -999
	for i in range(h-3,h):
		if Graph[i][-1]>maxValue:
			maxValue=Graph[i][-1]
			maxId=i
	#print(maxId,maxValue)
	output = []
	y = l-1
	x = maxId
	print('MAX',maxValue)
	#print(x)
	d = {0:'I',1:'M',2:'D'}
	while(x>0 and y>0):		
		output.append(d[x%3]+str(math.ceil(x/3)))
		#print((x,y),output[-1],'->',track[x][y])
		[x,y] = track[x][y]
	print(' '.join(output[::-1]))	
	
if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n--------\n')
	text = dataset[0]
	text = '0'+text # !!!
	dataset = dataset[1:]
	[threshold,theta] = list(map(float,dataset[0].split()))
	alphabet = dict([[dataset[1].split()[i],i] for i in range(len(dataset[1].split()))])
	mutli_Alig = dataset[2].split()
	#mutli_Alig=['BABADBEEC','-BDABADEB','BADADAAAB','BD-ADAEE-','DADADEDED','B-DAAACE-','BA-ADADEB','BADAD-DEB','B-DADADEB','BADA-CD-B']
	#theta = 0.01
	#threshold = 0.374
	print(mutli_Alig)
	[miss,miss_cnt] = preTreat(mutli_Alig)
	[transition ,emission,sn] = ProfileHMM()
	
	[Graph,track]=HMM_Path()
	
	TrackBack(Graph,track)