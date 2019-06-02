'''

Code Challenge: Implement BWMatching.
     Input: A string BWT(Text), followed by a collection of Patterns.
     Output: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns
     in Text.
-------------------
Sample Input:
TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC
CCT CAC GAG CAG ATC
-------------------
Sample Output:
2 1 1 0 1
-------------------
Lo Kwongho 2018.9
'''

def BWMatching(text,pattern):
	text = list(text)
	lexOrder = sorted(text)
	rearOrder = [0 for i in range(len(text))]
	d_num = {'$':-1,'A':-1,'T':-1,'G':-1,'C':-1}
	#d_num = {'p':-1,'a':-1,'n':-1,'m':-1,'b':-1,'s':-1,'$':-1}
	for i in range(len(text)):
		d_num[text[i]] += 1
		rearOrder[i] = d_num[text[i]]
	d = {'$':[],'A':[],'T':[],'G':[],'C':[]}
	#d = {'p':[],'a':[],'n':[],'m':[],'b':[],'s':[],'$':[]}
	for i in range(len(lexOrder)):
		d[lexOrder[i]].append(i)
	
	top = -1
	bottom = -1
	while(len(pattern)):
		flag = False
		symbol = pattern[-1]
		pattern = pattern[:-1]
		if top==-1:
			cnt = 0
			for i in range(len(text)):
				if text[i]==symbol and top==-1:
					flag = True
					top = i
					bottom = i
				elif text[i]==symbol:
					bottom = i
			if not flag:
				return 0
			top = d[text[top]][rearOrder[top]]
			bottom = d[text[bottom]][rearOrder[bottom]]
			#print(symbol,top,bottom)
			#input()
			continue
		newtop = -1
		newbottom = -1
		for i in range(top,bottom+1):
			if text[i]==symbol and newtop==-1:
				flag = True
				newtop = i
				newbottom = i
			elif text[i]==symbol:
				newbottom = i
		if not flag:
			return 0
		top = d[text[newtop]][rearOrder[newtop]]
		bottom = d[text[newbottom]][rearOrder[newbottom]]
		#print(symbol,top,bottom)
		#input()
	return bottom-top+1
		
if __name__ == '__main__':
	from os.path import dirname
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
	text = dataset[0]
	patterns = dataset[1:]
	for pattern in patterns:
		print(BWMatching(text,pattern),end=' ')