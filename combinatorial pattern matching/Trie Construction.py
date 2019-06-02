'''
Code Challenge: Implement TrieMatching to solve the Multiple Pattern Matching Problem.
  >> Input: A string Text and a collection of strings Patterns.
  >> Output: All starting positions in Text where a string from Patterns appears as a substring.
----------------
Sample Input:
AATCGGGTTCAATCGGGGT
ATCG
GGGT
----------------
Sample Output:
1 4 11 15
----------------
Lo Kwongho 2018.9
'''

from os.path import dirname

def BuildTrie():
	Trie = [[] for i in range(maxn)]
	root = 0
	exist_node_num = 1
	for i in range(len(patterns)):
		currentNode = root
		for j in range(len(patterns[i])):
			flag = True
			for e in range(len(Trie[currentNode])):
				if Trie[currentNode][e][1]==patterns[i][j]:
					currentNode = Trie[currentNode][e][0]
					flag = False
					break
			if flag:
				Trie[currentNode].append([ exist_node_num,patterns[i][j] ])
				currentNode = exist_node_num
				exist_node_num += 1
	return [Trie,root,exist_node_num]

def PrefixTrieMatching(subtext):
	currentNode = root
	for i in range(len(subtext)):
		if len(Trie[currentNode])==0:
			return 1
		flag = False
		for e in Trie[currentNode]:
			if e[1]==subtext[i]:
				currentNode = e[0]
				flag = True
				break
		if not flag:
			return -1

def TrieMatching():
	output = []
	for i in range(len(text)-patrn_l+1):
		index = PrefixTrieMatching(text[i:])
		if index != -1:
			output.append(i)
	return output	

if __name__ == '__main__':
	maxn = 10000
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	text = dataset[0]
	patterns = dataset[1:]
	patrn_num = len(patterns)
	patrn_l = len(patterns[0])
	
	[Trie,root,tSize] = BuildTrie()
	
	output = TrieMatching()
	
	print(' '.join(list(map(str,output))))
	'''
	for i in range(tSize):
		for j in range(len(Trie[i])):
			print('%d->%d:%s'%(i,Trie[i][j][0],Trie[i][j][1]))
	'''