#!c:\Program Files (x86)\Python33\python.exe -tt
# -*- coding=utf-8 -*-

import sys
import time

def markTime(timeStampStr, preTimeStamp):
	currentTime = time.time()
	durTime = currentTime - preTimeStamp

	print(timeStampStr, 'Curent = ', currentTime, ',', 'Duration = ', durTime)

	return currentTime

def genRefDic(reffile, refdic):
	
	l = reffile.read().split(';')

	for e in l:
		subElem = e.split(',')

		if len(subElem) != 0:
			id = subElem[0].strip()

			if (id != '') and (id not in refdic):
				refdic[id] = e

	return 

def genCompleteList(inputfile, refdic, compList):

	l = inputfile.read().split(';')

	for e in l:
		e = e.strip()

		if e in refdic:
			compList.append(refdic[e])

	return

def genOutfile(outputfile, compList):

	for e in compList:
		outputfile.write(str(e))
		outputfile.write(';')

	return

def main():
	if len(sys.argv) < 4:
		print('Usage: filterStock.py inputfile reffile outputfile')
		sys.exit(1)

	received = markTime('Beginning: ', 0)

	inputfile = open(sys.argv[1], 'r', encoding = 'gb18030')
	reffile = open(sys.argv[2], 'r', encoding = 'gb18030')
	outputfile = open(sys.argv[3], 'w')

	refdic = {}
	genRefDic(reffile, refdic)

	compList = []
	genCompleteList(inputfile, refdic, compList)

	genOutfile(outputfile, compList)

	inputfile.close()
	reffile.close()
	outputfile.close()

	markTime('Ending: ', received)

	return

if __name__ == '__main__':
    main()

