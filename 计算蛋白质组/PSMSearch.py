from os.path import dirname
from InPutTable import InPut_Integer_Mass_Table
from Peptide_Identification import PeptideIdentification

def PSMSearch(Spectrum_Vector,Proteome,threshold):
	PSMSet = []
	for sv in Spectrum_Vector:
		[peptide,score] = PeptideIdentification(sv, Proteome)
		if score >= threshold:
			PSMSet.append(peptide)
	return PSMSet

if __name__ == '__main__':
	
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
	Spectrum_Vector = [list(map(int,line.split())) for line in dataset[:-2]]
	#print(Spectrum_Vector)
	Proteome = dataset[-2]
	threshold = int(dataset[-1])
	
	print('\n'.join(PSMSearch(Spectrum_Vector, Proteome, threshold)))