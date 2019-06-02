'''
Longest Shared Substring Problem: Find the longest substring shared by two strings.
     Input: Strings Text1 and Text2.
     Output: The longest substring that occurs in both Text1 and Text2.

Code Challenge: Solve the Longest Shared Substring Problem. (Multiple solutions may exist, in which case you may return any one.)

--Sample Input:
TCGGTAGATTGCGCCCACTC
AGGGGCTCGCAGTGTAAGAA
--Sample Output:
AGA
----------------
Lo Kwongho 2018.9
'''
from os.path import dirname

def SuffixTreeConstruct():
	Tree = [ [] for i in range(maxn) ]
	v_num = 1
	root = 0
	for i in range(len(text)):
		currentNode = root
		suffix = text[i:]

		while len(suffix):
			flag = False
			for e in range(len(Tree[currentNode])):
				if Tree[currentNode][e][1][0]==suffix[0]:
					if len(Tree[currentNode][e][1])<len(suffix) and Tree[currentNode][e][1]==suffix[:len(Tree[currentNode][e][1])]:
						## 小段匹配
						suffix = suffix[len(Tree[currentNode][e][1]):]
						currentNode =  Tree[currentNode][e][0]
						flag = True
						break
					elif Tree[currentNode][e][1]==suffix:
						flag = True
						break
						
					for j in range(1,len(suffix)):					
						if suffix[j]!=Tree[currentNode][e][1][j]:
							Tree[currentNode].append([v_num,suffix[:j]])							
							Tree[v_num].append([v_num+1,suffix[j:]])
							Tree[v_num].append([Tree[currentNode][e][0],Tree[currentNode][e][1][j:]])
							v_num += 2
							Tree[currentNode].pop(e)
							suffix = ''
							flag = True
							break
							
				if flag == True:
					break
			if not flag:
				Tree[currentNode].append([v_num,suffix])
				v_num += 1
				suffix = ''
			
	return [Tree,root]

def colorEdge(v):
	global colorList
	color = ''
	for e in range(len(Tree[v])):
		if len(Tree[Tree[v][e][0]])==0: #leave
			if '#' in Tree[v][e][1]:
				colorList[Tree[v][e][0]]='blue'
				if color=='':
					color='blue'
				elif color=='red':
					color='purple'
			else:
				colorList[Tree[v][e][0]]='red'
				if color=='':
					color='red'
				elif color=='blue':
					color='purple'
		else:
			tmpColor = colorEdge(Tree[v][e][0])
			if color=='':
				color=tmpColor
			elif color!=tmpColor:
				color='purple'
	colorList[v]=color
	return color
	
def dfs(v,output):
	if len(Tree[v])==0:
		print(output)
	for i in range(len(Tree[v])):
		dfs(Tree[v][i][0],output+Tree[v][i][1])
		
def dfs_for_purple(v,output):
	global longestStr
	flag = True
	for i in range(len(Tree[v])):
		if colorList[Tree[v][i][0]]=='purple':
			flag = False
			dfs_for_purple(Tree[v][i][0],output+Tree[v][i][1])
	if flag:
		if len(longestStr)<len(output):
			longestStr = output
		
		
	
if __name__ == '__main__':
	text = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	text = text[0]+'#'+text[1]+'$'
	#text = 'GTTCGTGGT$'
	#text = 'panama#bananas$'
	maxn = 2*len(text)+5
	[Tree,root] = SuffixTreeConstruct()
	'''
	# visualize the Built Tree
	output = []
	for i in range(len(Tree)):
		for j in range(len(Tree[i])):
			output.append(Tree[i][j][1])
	output.sort()
	for i in output:
		print(i)

	'''
	
	colorList = [0 for i in range(maxn)]
	colorEdge(0)
	output = ''
	longestStr = ''
	
	dfs_for_purple(root,output)
	print('#',longestStr)

	