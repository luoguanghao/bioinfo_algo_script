from os.path import dirname

def InputCodon():
	dataset=open(dirname(__file__)+'/Codon.txt').read().strip().split()
	dict=[]
	for i in range(0,len(dataset),2):
		dict.append([dataset[i],dataset[i+1]])
	return dict

def InputRNABasePair():
	return {'A':'U', 'T':'A', 'C':'G', 'G':'C'}

def InputDNABasePair():
	return {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def InputData(file_name = '/dataset.txt'):
	dataset = open(dirname(__file__)+file_name).read().strip()
	return dataset

if __name__ == "__main__":
	for i in InputCodon():
		print(i)
	