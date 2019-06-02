AminoAcids = [[57], [71], [87], [97], [99], [101], [103], [113], [114], [115], [128], [129], [131], [137], [147], [156], [163], [186]]

def Print(pep):
	for i in range(len(pep)):
		if i!=0:
			print('-',end='')
		print(pep[i],end='')
	print(' ',end='')

def Expand(Peptides):
	output = []
	if len(Peptides)==0:
		return [i for i in AminoAcids]
	for aa in AminoAcids:
		for item in Peptides:
			output.append(item+aa)
	return output
	
def getMass(Peptide):
	return sum(Peptide)
	
def Cyclospectrum(Peptide):
	spectrum = []
	for k in range(1,len(Peptide)):
		for i in range(len(Peptide)):
			element = Peptide[i:i+k]
			if k-len(Peptide)+i>0:
				element += Peptide[:k-len(Peptide)+i]
			spectrum.append(sum(element))
	spectrum += [0,sum(Peptide)]
	spectrum.sort()
	return spectrum
	
def Consistent(Peptide,Spectrum):
	linerSpectrum = []
	for k in range(1,len(Peptide)):
		for i in range(len(Peptide)):
			element = Peptide[i:i+k]
			linerSpectrum.append(sum(element))
	linerSpectrum += [sum(Peptide)]
	for item in linerSpectrum:
		if not(item in Spectrum):
			return False
	return True

from os.path import dirname

dataset = open(dirname(__file__) + 'dataset.txt').read().strip().split()
for i in range(len(dataset)):
	dataset[i] = int(dataset[i])
Spectrum = dataset
Spectrum.sort()
parentMass = dataset[-1]

Peptides = []
flag = True
time = 1
while(len(Peptides)>0 or flag):
	flag = False
	Peptides = Expand(Peptides)
	tmpPeptides = Peptides[:]
	
	for pep in tmpPeptides:
		if getMass(pep) == parentMass:
			if Cyclospectrum(pep)==Spectrum:
				Print(pep)
			Peptides.remove(pep)
		elif not(Consistent(pep,Spectrum)):
			Peptides.remove(pep)
			