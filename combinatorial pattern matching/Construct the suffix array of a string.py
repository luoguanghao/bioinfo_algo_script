'''
Suffix Array Construction Problem: Construct the suffix array of a string.
     Input: A string Text.
     Output: SuffixArray(Text).

Code Challenge: Solve the Suffix Array Construction Problem.
-----
Sample Input:
AACGATAGCGGTAGA$
----
Sample Output:
15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5
'''

text = "AACGATAGCGGTAGA$"
suffixList = []

for i in range(len(text)):
	suffixList.append([i,text[i:]])
suffixList=sorted(suffixList,key=lambda x: x[1])
for i in suffixList:
	print(i[0],end=', ')