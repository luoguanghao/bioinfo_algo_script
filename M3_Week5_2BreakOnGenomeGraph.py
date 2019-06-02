


if __name__ == '__main__':
	from os.path import dirname
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	edges = dataset[0].strip('(').strip(')').split('), (')
	bp = list(map(int,dataset[1].split(', ')))
	edges = [list(map(int,i.split(', '))) for i in edges]
	#print(edges)
	
	try:
		i1=edges.index([bp[1],bp[0]])
	except:
		i1=edges.index([bp[0],bp[1]])
	try:
		i2=edges.index([bp[2],bp[3]])
	except:
		i2=edges.index([bp[3],bp[2]])
	
	edges[i1]=[bp[2],bp[0]]
	edges[i2]=[bp[1],bp[3]]
	for e in edges:
		print('(%d, %d), '%(e[0],e[1]),end='')