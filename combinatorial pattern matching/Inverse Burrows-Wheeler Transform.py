'''
Inverse Burrows-Wheeler Transform Problem: Reconstruct a string from its Burrows-Wheeler transform.
     Input: A string Transform (with a single "$
" symbol).
     Output: The string Text such that BWT(Text) = Transform.

Code Challenge: Solve the Inverse Burrows-Wheeler Transform Problem.
-------------------
Sample Input:
TTCCTAACG$A
-------------------
Sample Output:
TACATCACGT$
'''

def InverseBurrowsWheelerTransform():
	d = {'$':[],'A':[],'T':[],'G':[],'C':[]}
	for i in range(len(text)):
		d[text[i]].append(i)
		
	LexOrder = sorted(text)
	frontOrder = [0 for i in range(len(text))]
	for i in range(1,len(text)):
		if LexOrder[i-1]==LexOrder[i]:
			frontOrder[i] = frontOrder[i-1]+1
	#print(frontOrder)
	#print(LexOrder)
	firstOrder = -1
	firstSymb = ''
	output = '$'
	for i in range(len(text)):
		#print(output)
		if i==0:
			output += LexOrder[d['$'][0]]
			firstOrder = frontOrder[d['$'][0]]
			firstSymb = LexOrder[d['$'][0]]
			continue
		#print('#',firstOrder,firstSymb)
		output += LexOrder[d[firstSymb][firstOrder]]
		firstOrder = frontOrder[d[firstSymb][firstOrder]]
		firstSymb = output[-1]
	output = output[1:]
	return output

if __name__ == '__main__':
	text = list('TTCCTAACG$A')
	output = InverseBurrowsWheelerTransform()
	print(output)