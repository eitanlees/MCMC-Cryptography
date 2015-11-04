# Boring preliminaries
import re
import math
import string
import random
from collections import Counter
import numpy as np
#from __future__ import division

def sanitizeText(s):
	"""Sanitize the text. Retain only letters - make them all upper-case"""
	return re.sub('[^A-Z\s]+', '', s.upper())
	
def readSourceText(fname):
	"""Read, sanitize reference text, and return association map of letter pairs"""
	
#	TEXT = file('test.txt').read()
	TEXT = file(fname).read()
	print "Number of lines in reference text", len(TEXT)

	TEXT = sanitizeText(TEXT)
	
	# Make the association map of letter pairs
	c = Counter(zip(TEXT, TEXT[1:]))

	# increment counter by 1 because later going to take log of this qty
	for i in c:
		c[i] += 1


	return c

def printFirstOrderTransitionMatrix(pairFreqSource):

	M = np.zeros((27,27),dtype=int)


	yset = sorted(set(pairFreqSource.elements()))
	for x in yset:
		
		i = j = -1
		
		if ord(x[0]) == 32:
			i = 26
		elif 65 <= ord(x[0]) <= 90:
			i = ord(x[0]) - 65

		if ord(x[1]) == 32:
			j = 26
		elif 65 <= ord(x[1]) <= 90:
			j = ord(x[1]) - 65
		
		if i >= 0 and j >= 0:
			M[i,j] = pairFreqSource[x[0],x[1]]

	np.savetxt('M.dat', M, fmt='%8d') 
  
	return
		
#
# Main Program
#

LETTERS  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
invTemp  = 1.0
thinning = 10000

pairFreqSource = readSourceText('WarAndPeace.txt')
pairFreqSource += readSourceText('OliverTwist.txt') 
pairFreqSource += readSourceText('KJBible.txt') 

printFirstOrderTransitionMatrix(pairFreqSource)
