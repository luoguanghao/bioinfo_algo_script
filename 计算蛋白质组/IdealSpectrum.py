from InPutTable import InPut_Integer_Mass_Table
from collections import defaultdict
from os.path import dirname


def IdealSpectrum(peptide = list('GPG'),tp='pre/suf'):
	l = len(peptide)
	IMTable = InPut_Integer_Mass_Table()[0]
	masssuf = 0
	masspre = 0
	ISpectrumPre = []
	ISpectrumSuf = []
	for i in range(l):
		masspre += IMTable[peptide[i]]
		masssuf += IMTable[peptide[l-1-i]]
		ISpectrumPre += [masspre]
		ISpectrumSuf += [masssuf]
	if(tp=='pre/suf'):
		ISpectrum=sorted(ISpectrumPre+ISpectrumSuf[:-1])	
		return ISpectrum
	elif(tp=='pre'):
		return ISpectrumPre
	elif(tp=='suf'):
		return ISpectrumSuf
	
	

if __name__ == '__main__':
	print(IdealSpectrum(tp='pre'))