'''
Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.

Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
    
Output: All substrings of Text encoding Peptide (if any such substrings exist).
'''
reversedDict = {'A':'T','G':'C','T':'A','C':'G'}

def reversedSeq(text):
	revText = ''
	for i in text:
		revText += reversedDict[i]
	return revText[::-1]

def FindPosblSeq(AA,AAtoCondonDict):
	l = len(AA)
	current = 0
	Result = ['']
	while(l>current):
		#print(Result)
		tmp = []
		for i in AAtoCondonDict[AA[current]]:
			for preS in Result:
				tmp.append(preS+i)
		
		Result = tmp
		current+=1
		
	return Result


from os.path import dirname

dataset = open(dirname(__file__) + 'dataset.txt').read().strip().split()
condon = open(dirname(__file__) + 'RNA_codon_table_1.txt').read().strip().split('\n')

text = ''.join(dataset[0:-1])
AA = dataset[-1]
condon_table = []
for line in condon:
	condon_table.append(line.split())
#print(condon_table)
AAtoCondonDict = {}
for item in condon_table:
	if item[1] in AAtoCondonDict.keys():
		AAtoCondonDict[item[1]].append(item[0])
	else:
		AAtoCondonDict[item[1]]=[item[0]]
#print(AAtoCondonDict)

PossibleSequences = FindPosblSeq(AA,AAtoCondonDict)

for i in range(len(PossibleSequences)):
	PossibleSequences[i]=PossibleSequences[i].replace('U','T')

revPSq = []
for item in PossibleSequences:
	revPSq.append(reversedSeq(item))
PossibleSequences += revPSq
PossibleSequences = set(PossibleSequences)
#print(PossibleSequences)
#print('GTAAAACTATTTCCATGGTTTAACCAGTAC' in PossibleSequences)

for i in range(len(text)-3*len(AA)):
	if text[i:i+3*len(AA)] in PossibleSequences:
		print(text[i:i+3*len(AA)])
	