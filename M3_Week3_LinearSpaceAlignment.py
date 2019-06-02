'''
Code Challenge: Implement LinearSpaceAlignment to solve the Global Alignment Problem for a large dataset.
>>>Input: Two long (10000 amino acid) protein strings written in the single-letter amino acid alphabet.
>>>Output: The maximum alignment score of these strings, followed by an alignment achieving this maximum score. Use the

BLOSUM62 scoring matrix and indel penalty σ = 5.
------------
Sample Input:
PLEASANTLY
MEANLY
------------
Sample Output:
8
PLEASANTLY
-MEA--N-LY
------------
coder: Lo Kwongho in 2018.9
'''
from os.path import dirname
import numpy
#
indel = -5
negINF = -9999
#
#
def Grade(Symb1,Symb2):
	Indx1 = symbolList[Symb1]
	Indx2 = symbolList[Symb2]
	return matrix[Indx1][Indx2]

def ImportScoreMatrix():
	dataset = open(dirname(__file__)+'BLOSUM62.txt').read().strip().split('\n')
	symbolList = dataset[0].split()
	for i in range(len(symbolList)):
		symbolList[i]=[symbolList[i],i]
	symbolList = dict(symbolList)
	matrix = []
	for i in range(1,len(dataset)):
		matrix.append(dataset[i].split()[1:])
	for l in range(len(matrix)):
		for i in range(len(matrix[l])):
			matrix[l][i]=int(matrix[l][i])
	return [matrix,symbolList]
#
def half_Alignment(v,w):
	nv = len(v)
	mw = len(w)
	s = numpy.zeros(shape=(nv+1,2),dtype=int)
	for i in range(nv+1):
		s[i,0] = indel*i
	if mw==0:
		return s[:,0] #
	for j in range(mw):
		s[0,1]=s[0,0]+indel
		for i in range(nv):
			s[i+1,1]=max(s[i,1]+indel,s[i+1,0]+indel,s[i,0]+Grade(w[j],v[i]))
		s[:,0]=s[:,1]
	return s[:,1]

def midEdge(v,w):
	nv = len(v)
	mw = len(w)
	mid = int((mw-1)/2)
	wl = w[:mid]
	wr = w[mid+1:]
	pre = half_Alignment(v,wl)
	suf = half_Alignment(v[::-1],wr[::-1])[::-1]
	hs = [pre[i]+suf[i]+indel  for i in range(nv+1)]
	ds = [pre[i]+suf[i+1]+Grade(w[mid],v[i])  for i in range(nv)]
	maxhs = max(hs)
	maxds = max(ds)
	if maxhs>maxds:
		return ( (hs.index(maxhs),mid) ,(hs.index(maxhs),mid+1) )
	else:
		return ( (ds.index(maxds),mid) ,(ds.index(maxds)+1,mid+1) )

def build_Alignment_track(v,w):
	vn = len(v)
	wm = len(w)
	if vn==0 and wm==0:
		return []
	elif vn==0:
		return ['-']*wm
	elif wm==0:
		return ['|']*vn
	((x1,y1),(x2,y2)) = midEdge(v,w)
	if x1==x2:
		edge = ['-']
	else:
		edge = ['\\']
	wleft = w[:y1]
	wright = w[y2:]
	vupper = v[:x1]
	vbotm = v[x2:]

	upper_left_track = build_Alignment_track(vupper,wleft)
	bottom_right_track = build_Alignment_track(vbotm,wright)
	return upper_left_track+edge+bottom_right_track

def trackToString(v,w,track):
	vi = 0
	wj = 0
	outv = ''
	outw = ''
	score = 0
	for i in track:
		if i == '|':
			outv += v[vi]
			outw += '-'
			score += indel
			vi += 1	
		elif i == '-':
			outv += '-'
			outw += w[wj]
			score += indel
			wj += 1			
		else:
			outv += v[vi]
			outw += w[wj]
			score += Grade(v[vi], w[wj])
			vi += 1
			wj += 1
			
	return [score,outv,outw]

def LinearSpaceAlignment(v,w):
	track = build_Alignment_track(v,w)
	[score,outv, outw] = trackToString(v,w,track)
	print(score)
	print(outv)
	print(outw)

if __name__ == '__main__':
	dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
	[matrix,symbolList] = ImportScoreMatrix()
	v = dataset[0]
	w = dataset[1]
	LinearSpaceAlignment(v,w)