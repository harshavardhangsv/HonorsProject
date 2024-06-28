import re
import sys
import os
import nltk
from nltk.corpus import verbnet
from stemming.porter2 import stem

for r,d,f in os.walk('./'):
	for each in f:
		if 'slashed' in each:
			print '##########################################################'
			counter = 0
			null=0
			fp = open(r+each,'r')
			lines = fp.readlines()
			start = lines.index('Method:\n') + 2
			end = len(lines)
			for i in lines[start:end]:
				parts = i.replace("\n","").split(" ")
				for part in parts:
					token = part.split("/")[0]
					pos_tag = part.split("/")[1]
					if pos_tag[0] == 'V':
						counter += 1
						apprx_classid = verbnet.classids(token.lower())
						if apprx_classid == []:
							root = stem(token.lower())
							apprx_classid = verbnet.classids(root)
						if apprx_classid == []:
							null += 1	
						print "-------------------------------------"
						print ''.join(i),
						print token,apprx_classid
						print "--------------------------------------\n"
			print counter,null
