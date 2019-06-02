'''
Burrows-Wheeler Transform Construction Problem: Construct the Burrows-Wheeler transform of a string.
     Input: A string Text.
     Output: BWT(Text).
---Sample Input:
GCGTGCCTGGTCA$
---Sample Output:
ACTGGCT$TGCGGC
'''
from os.path import dirname

def M(text):
	RotateMatrix = []
	for i in range(len(text)):
		RotateMatrix.append([i,i-1])
		print()
	sorted(RotateMatrix, key=lambda x:text[0])
	
	output = ''
	for i in range(len(RotateMatrix)):
		output += text[RotateMatrix[i][1]]
	return output

text = 'GCGTGCCTGGTCA$'
#text = open(dirname(__file__)+'dataset.txt').read().strip()
threshold = 2
BWStr = M(text)
print(BWStr)
'''
cnt = 0
tmpl = 0
currentSymbol = ''
for i in range(len(BWStr)):
	if currentSymbol!=BWStr[i]:
		if tmpl>=threshold:
			cnt += 1
		tmpl = 1
		currentSymbol = BWStr[i]
	else:
		tmpl += 1
print(cnt)
'''