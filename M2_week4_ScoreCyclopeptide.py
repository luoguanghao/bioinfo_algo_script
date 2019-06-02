def getMassSeq(text,mT):
	return [int(mT[i]) for i in text]

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
	

from os.path import dirname

massTable = open(dirname(__file__) + 'integer_mass_table.txt').read().strip().split('\n')
for i in range(len(massTable)):
	massTable[i] = massTable[i].split()
massTable = dict(massTable)

dataset = open(dirname(__file__) + 'dataset.txt').read().strip().split()
text = dataset[0]
Spectrum = [int(i) for i in dataset[1:]]

TheoreticalSpectrum = Cyclospectrum(getMassSeq(text, massTable))
bucketThSptm = [0]*6000
for item in TheoreticalSpectrum:
	bucketThSptm[item] += 1

bucketSptm = [0]*6000

for item in Spectrum:
	bucketSptm[item] += 1

cnt = 0
for i in range(len(bucketSptm)):
	if bucketSptm[i]<bucketThSptm[i]:
		cnt += bucketSptm[i]
	else:
		cnt += bucketThSptm[i]
print(cnt)	
