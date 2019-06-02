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

if __name__ == '__main__':	
	#text = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	text = 'ATAAATG$'
	#text = 'panama#bananas$'
	#maxn = 2*len(text)+5
	maxn = 300
	patterns = [text[i:] for i in range(len(text))]
	Tree = BuildTrie()