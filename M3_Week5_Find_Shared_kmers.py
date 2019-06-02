'''
Shared k-mers Problem: Given two strings, find all their shared k-mers.
   >>>Input: An integer k and two strings.
   >>>Output: All k-mers shared by these strings, in the form of ordered pairs (x, y) corresponding to starting positions
     of these k-mers in the respective strings.
------------
3
AAACTCATC
TTTCAAATC
------------
(0, 4)
(0, 0)
(4, 2)
(6, 6)
------------
coder Lo Kwongho 2018.9
'''
from os.path import dirname
ComplDict = {'A':'T','T':'A','G':'C','C':'G'}

def reverseComple(kmer):
	rekmer = ''
	for i in range(len(kmer)-1,-1,-1):
		rekmer += ComplDict[kmer[i]]
	return rekmer

def shared_kmers():
	bucket = dict()
	for i in range(len(text1)-k+1):
		kmer = text1[i:i+k]
		if kmer in bucket.keys():
			bucket[kmer][0].append(i)
		elif reverseComple(kmer) in bucket.keys():
			bucket[reverseComple(kmer)][0].append(i)
		else:
			bucket[kmer] = [ [i],[] ]
	for i in range(len(text2)-k+1):
		kmer = text2[i:i+k]
		if kmer in bucket.keys():
			bucket[kmer][1].append(i)
		elif reverseComple(kmer) in bucket.keys():
			bucket[reverseComple(kmer)][1].append(i)
		else:
			bucket[kmer] = [ [],[i] ]
	ans = []
	for item in bucket.values():
		if item[0]!=[] and item[1]!=[]:
			for i in item[0]:
				for j in item[1]:
					ans.append([i,j])
	return ans

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
	k = int(dataset[0])
	text1 = dataset[1]
	text2 = dataset[2]
	
	ans = shared_kmers()
	print(len(ans))
	for i in ans:
		print('(%d, %d)'%(i[0],i[1]))