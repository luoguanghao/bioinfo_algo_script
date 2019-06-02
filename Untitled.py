import random
from os.path import dirname
from numpy.random import choice
from collections import Counter
import numpy as np

def Score(Motifs,k):
	size = len(Motifs)
	cnt = k*len(Motifs)
	for i in zip(*Motifs):
		cnt -= int(Counter(i).most_common(1)[0][1])	
	return cnt

from os.path import dirname

dataset = open(dirname(__file__)+'dataset.txt').read().strip().split('\n')
#dataset = [i.split()[-1] for i in dataset]
print(dataset)
print(Score(dataset, 20))

'''
 Rv1733c   1|14  :   1/187   TTCGTGACCGACGTCCCCAG
	 Rv1737c   2|5   :   2/141   TTGGGGACTTCCGGCCCTAA
		Rv1738   3|1   :   3/117   GCCGGGACTTCAGGCCCTAT
		Rv0079   4|7   :   4/162   CATGGGACTTTCGGCCCTGT
		Rv0569   5|10  :   6/156   GAGGGGACTTTTGGCCACCG
	 Rv0571c   6|4   :   8/199   CCAGGGACCTAATTCCATAT
	 Rv0574c   7|9   :  10/139   TTGAGGACCTTCGGCCCCAC
	 Rv1734c   8|19  :  11/202   CTGGGGACCGAAGTCCCCGG
		Rv1996   9|16  :  14/175   TTAGGGACCATCGCCTCCTG
		Rv1997  10|6   :  15/161   TGGATGACTTACGGCCCTGA
	 Rv2005c  11|15  :  17/180   TTGGGGACTAAAGCCTCATG
	 Rv2031c  12|2   :  20/169   TCGGGGACTTCTGTCCCTAG
		Rv2032  13|11  :  21/174   TTGGGGACCATTGACCCTGT
		Rv2623  14|13  :  22/120   TTGAGGACCTAAGCCCGTTG
	 Rv2626c  15|18  :  24/161   CACGGGTCAAACGACCCTAG
	 Rv2627c  16|3   :  25/198   GGCGGGACGTAAGTCCCTAA
		Rv2628  17|17  :  26/214   GAAGTGACGAAAGACCCCAG
	 Rv3130c  18|8   :  31/157   CGGAGGACCTTTGGCCCTGC
	 Rv3134c  19|12  :  34/159   GTGGGGACCAACGCCCCTGG
'''