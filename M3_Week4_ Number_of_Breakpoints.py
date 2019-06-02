'''
Code Challenge: Solve the Number of Breakpoints Problem.
 >>Input: A permutation.
 >>Output: The number of breakpoints in this permutation.
Sample Input:---------
(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)
Sample Output:--------
8
----------------------
coder : Lo Kwongho 2018.9
'''
from os.path import dirname

def CountBreakpoints():
	cnt = 0
	for i in range(1,len(P)):
		if P[i-1]+1!=P[i]:
			cnt += 1
	return cnt

if __name__ == '__main__':
	
	dataset = open(dirname(__file__)+'dataset.txt').read().strip()
	P = [0]+dataset[1:-1].split()
	P += [len(P)]
	P = list(map(int,P))
	
	print(P)
	print(CountBreakpoints())