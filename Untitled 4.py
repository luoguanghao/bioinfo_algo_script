

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

def linearSpectrum(Peptide):
	linearSpectrum = []
	for k in range(1,len(Peptide)):
		for i in range(len(Peptide)):
			element = Peptide[i:i+k]
			linearSpectrum.append(sum(element))
	linearSpectrum += [sum(Peptide),0]
	return linearSpectrum
	
def getMassSeq(text,mT):
	return [int(mT[i]) for i in text]


from os.path import dirname

massTable = open(dirname(__file__) + 'integer_mass_table.txt').read().strip().split('\n')
for i in range(len(massTable)):
	massTable[i] = massTable[i].split()
massTable = dict(massTable)	
print(linearSpectrum(getMassSeq('NQEL', massTable)))
print(Cyclospectrum(getMassSeq('NQEL', massTable)))