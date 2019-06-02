from sklearn.cluster import AgglomerativeClustering
import numpy as np
from os.path import dirname
import matplotlib.pyplot as plt

def InputData(dataset):
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
	return points

if __name__ == '__main__':
	
	f = open("output","w")
	
	INF = 999999
	dataset = open(dirname(__file__)+'230genes_log_expression.txt').read().strip().split('\n')
	
	X = np.array(InputData(dataset))
	
	clustering = AgglomerativeClustering(n_clusters=6).fit(X)
	
	print(clustering.labels_)
	
	lb = clustering.labels_
	
	clusters = [[] for i in range(6)]
	
	for i in range(len(X)):
		clusters[lb[i]].append(i)
	
	fig=plt.figure()
	
	colors = ['#0000CD','#FF00FF','#00FA9A','#FFD700','#FFEFD5','#00FFFF']
	x = [i for i in range(1,8)]
	for c in range(6):
		plt.subplot(231+c)
		for i in clusters[c]:		
			plt.plot(x,X[i],linewidth=0.5,linestyle='-',marker='')
	plt.show()