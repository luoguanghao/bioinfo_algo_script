from os.path import dirname
from useful import InputData

def PatternCount(Text,Pattern):
	pl = len(Pattern)
	l = len(Text)
	cnt = 0
	for i in range(0,l-pl+1):
		if Text[i:i+pl]==Pattern:
			cnt += 1
	return cnt
		
if __name__ == '__main__':
	data = InputData()
	data = data.split('\n')
	Text = data[0]
	Pattern = data[1]
	print(PatternCount(Text, Pattern))