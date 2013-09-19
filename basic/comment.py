#!c:\Program Files (x86)\Python33\python.exe -tt
# -*- coding=utf-8 -*-

import sys
#import codecs

def main():
	filename = sys.argv[1]
	desireddate = sys.argv[2]
	desiredstr = '<---分割线'

	linecount = 0
	desiredstrfound = False
	desireddatefound = False
	elem = []
	tempstr = ''

	f = open(filename, 'r', encoding = 'gb18030')

	for line in f:
		if desiredstr in line:
			if tempstr != '':
				elem.append(tempstr)
				tempstr = ''
				
			linecount = 0
			desireddatefound = False

			if desiredstrfound == False:
				desiredstrfound = True

		elif desiredstrfound == True:
			linecount = linecount + 1

			if linecount == 1 and desireddate in line:
				desireddatefound = True

			if desireddatefound == True:
				tempstr = tempstr + line

	print(elem)
	f.close()

	return

if __name__ == '__main__':
    main()
