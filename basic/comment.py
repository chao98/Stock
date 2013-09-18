#!c:\Program Files (x86)\Python33\python.exe -tt

import sys

def main():
	filename = sys.argv[1]
	desiredstr = '<---分割线'
	count = 0
	found = False
	elem = []
	tempstr = ''

	f = open(filename, 'r')

	for line in f:
		if count == 2:
			break
		elif desiredstr in line:

			if tempstr != '':
				elem.append(tempstr)
				tempstr = ''
				count = count + 1

			if found == False:
				found = True

		elif found == True:
			tempstr = tempstr + line


	print(elem)

	f.close()

	return

if __name__ == '__main__':
    main()
