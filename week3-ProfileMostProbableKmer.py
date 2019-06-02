dict = {'A':0,'C':1,'G':2,'T':3}

from os.path import dirname
import numpy as np

dataset = open(dirname(__file__)+'dataset.txt').read().split()

text = dataset[0]
k=int(dataset[1])
#profile=np.reshape(dataset[2:],(4,k))
profile =[(0.5, 0.0, 0.5, 0.0), (0.5, 0.0, 0.5, 0.0), (0.0, 0.5, 0.5, 0.0)]


def countTheProbable(pattern):
	cnt=1
	for i in range(len(pattern)):
		cnt *= float(profile[dict[pattern[i]]][i])
	return cnt

lt = len(text)
maxVal = 0
maxSet = set()
for i in range(lt-k+1):
	pattern = text[i:i+k]
	if maxVal<countTheProbable(pattern):
		maxVal=countTheProbable(pattern)
		maxSet.clear()
		maxSet.add(pattern)
	elif maxVal==countTheProbable(pattern):
		maxSet.add(pattern)

print(maxSet)
'''
pattern = 'AAG'
cnt=1.0
for i in range(len(pattern)):
	cnt *= float(profile[dict[pattern[0]]][0])
	print(cnt)
print(cnt)
'''