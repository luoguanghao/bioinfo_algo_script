'''
CODE CHALLENGE: Solve the Peptide Identification Problem.
     Given: A space-delimited spectral vector Spectrum' and an amino acid string Proteome.
     Return: A substring of Proteome with maximum score against Spectrum'.

Lo Kwongho 2018.12
'''

from os.path import dirname
from InPutTable import InPut_Integer_Mass_Table

def PeptideIdentification(Spectrum_Vector,Proteome):
	l = len(Spectrum_Vector)
	IMTable = InPut_Integer_Mass_Table()[0]
	
	def Product(peptide,sv):
		ans = 0
		mass = 0
		for aa in peptide:
			mass += IMTable[aa]
			ans += sv[mass-1]
		return ans
	
	max_score = 0
	max_peptide = ''
	for i in range(len(Proteome)):
		mass = 0
		j=0
		while(i+j<len(Proteome) and mass<l):
			mass += IMTable[Proteome[i+j]]
			j += 1
		if mass == l:
			score = Product(Proteome[i:i+j],Spectrum_Vector)
			if score>max_score:
				max_score = score
				max_peptide = Proteome[i:i+j]
	return [max_peptide,max_score]

if __name__ == '__main__':
	
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	Spectrum_Vector = list(map(int,dataset[0].split()))
	Proteome = dataset[1]
	
	print(PeptideIdentification(Spectrum_Vector, Proteome))