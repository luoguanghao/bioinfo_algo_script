
from os.path import dirname

dataset = open(dirname(__file__) + 'dataset.txt').read().strip().split()

l = int(dataset[0])
dataset = dataset[1:]

prefix = {}
#suffix = [[]]*4**(l-1)


for string in dataset:
	preSlice = string[0:l-1]
	if preSlice in prefix.keys():
		prefix[preSlice].append(string)
	else:
		prefix[preSlice] = [string]



for string in dataset:
	sufSlice = string[1:]
	print(string[1:-1])
	if sufSlice in prefix.keys():
		print(string,'->',end=' ')
		
		for item in prefix[sufSlice]:
			
			if item!=prefix[sufSlice][0]:
				print(',',end='')
			print(item,end='')
		print('\n',end='')
