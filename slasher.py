import re
import sys
import os
import nltk

files = ['AlooParatha','PannerParatha','MuliParatha','MasalaEggParatha']

for f in files:
	outputText = ''
	fp = open(f,'r')
	lines = fp.readlines()
	if 'Method:\n' in lines:
		methodStart = lines.index('Method:\n')
		outputText += ''.join(lines[0:methodStart+1])
		for i in lines[methodStart+1:len(lines)]:
			outputText += i.replace('_','/')
		fn = open('slashed'+f,'w')
		fn.write(outputText)
		print 'PERFECT'
