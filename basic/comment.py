#!c:\Program Files (x86)\Python33\python.exe -tt

import sys

def main():
	filename = sys.argv[1]
	desireddate = '2010-11-23'
	desiredstr = '<---分割线'

	linecount = 0
	desiredstrfound = False
	desireddatefound = False
	elem = []
	tempstr = ''

	f = open(filename, 'r')

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

			if linecount == 1:
				desireddatefound = True

			if desireddatefound == True:
				tempstr = tempstr + line

	print(elem)

	f.close()

	return

if __name__ == '__main__':
    main()
