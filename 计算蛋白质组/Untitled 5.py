from os.path import dirname
from collections import defaultdict

dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')

d = {'A':'T','T':'A','G':'C','C':'G'}

[k,l,t] = list(map(int,dataset[1].split()))

Genome = dataset[0]
traGenome = ''.join([d[i] for i in Genome])
#print(traGenome)

count = defaultdict(int)

for i in range(len(Genome)-k+1):
	#print(Genome[i:i+k])
	count[Genome[i:i+k]] += 1

'''
for i in range(len(traGenome)-k+1):
	#print(Genome[i:i+k])
	count[traGenome[i:i+k]] += 1
'''
ans = []
for item in count.items():
	if item[1] >= t:
		ans.append(item[0])

print(' '.join(ans))
