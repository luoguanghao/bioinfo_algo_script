from os.path import dirname
import numpy as np
import math
import random
import matplotlib.pyplot as plt

def  square_EuclideanDistance(vId,wId,Centers):
	s = 0
	for i in range(m):
		s += (points[vId][i]-Centers[wId][i])**2
	return s

def Centers_to_Clusters(Centers):
	global Cluster
	Cluster = [[] for i in range(k)]
	Distortion = 0
	for i in range(len(points)):
		minVal = INF
		minId = -1
		for c in range(k):
			tmp = square_EuclideanDistance(i, c,Centers)
			if tmp < minVal:
				minVal = tmp
				minId = c
		Cluster[minId].append(i)
		Distortion += minVal
	return Distortion/points_num
			
def Clusters_to_Centers():
	#print(Cluster)
	Centers = []
	for i in range(k):
		coordinate = [0 for i in range(m)]
		for pId in Cluster[i]:
			for j in range(m):
				coordinate[j] += points[pId][j]		
		if len(Cluster[i])==0:
			coordinate = [0.5 for item in coordinate]
		else:
			coordinate = [item/len(Cluster[i]) for item in coordinate]
		Centers.append(coordinate)
	#print(Centers)
	return Centers

def LloydClustering():
	global Cluster
	Centers = random.sample(points,k)
	minDistortion = INF	
	Distortion = Centers_to_Clusters(Centers)
	i = 0
	while(Distortion < minDistortion):
		i += 1
		#print('*%d iteration*...'%i)
		minDistortion = Distortion
		Centers = Clusters_to_Centers()
		Distortion = Centers_to_Clusters(Centers)		
	return [Centers,Distortion]

if __name__ == '__main__':
	INF = 999999
	dataset = open(dirname(__file__)+'230genes_log_expression.txt').read().strip().split('\n')
	dataset = [line.split() for line in dataset]
	name = [item[1] for item in dataset[1:]]
	k = 6 # 分成 6 类
	m = 7 # 数据的维度
	#print(m)
	# print(m,k)
	points = []
	for line in dataset[1:]:
		if(len(line)==10):
			points.append(list(map(float,line[3:])))
		elif(len(line)==9):
			points.append(list(map(float,line[2:])))
	for i in points:
		print(i)
	
	points_num = len(points)
	out_Distortion = INF
	out_Centers = []
	out_i = -1
	for i in range(100):
		[Centers,Distortion] = LloydClustering() #Distortion 精确度
		if Distortion<out_Distortion:
			out_Distortion = Distortion
			out_Centers = Centers
			out_i = i
	
	#print(out_i,out_Distortion)
	
	for c in out_Centers:
		for i in range(len(c)):
			if i != 0:
				print(' ',end='')
			print('%.3f'%c[i],end='')
		print('')
	
	x = [i for i in range(1,8)]
	
	plt.rcParams['figure.figsize']=(12,8)
	for i in range(len(points)):
			plt.plot(x,points[i],color='#C0C0C0',linewidth=1.5,linestyle='-',marker='.')

	for i in range(k):
		plt.plot(x,Centers[i],linewidth=1.5,linestyle='-',marker='.')
	plt.show()
	