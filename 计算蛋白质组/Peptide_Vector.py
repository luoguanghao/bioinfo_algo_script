from InPutTable import InPut_Integer_Mass_Table
from IdealSpectrum import IdealSpectrum
from os.path import dirname

def get_Peptide_Vector(peptide):
	ISpectrum = IdealSpectrum(peptide=peptide,tp='pre')
	#print(ISpectrum)	
	vector = [0]*ISpectrum[-1]
	for i in ISpectrum:
		vector[i-1]=1
	return vector

def get_Peptide(vector):
	traIMTable = InPut_Integer_Mass_Table()[1]
	ISpectrum = []
	peptide = ''
	for i in range(len(vector)):
		if(vector[i]==1):
			ISpectrum.append(i+1)
	last = 0
	for i in ISpectrum:
		peptide += traIMTable[i-last]
		last=i
	print(peptide)

if __name__ == '__main__':
	
	vector = list(map(int,open(dirname(__file__)+'dataset.txt').read().strip().split()))
	get_Peptide(vector)