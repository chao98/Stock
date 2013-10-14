#!c:\Program Files (x86)\Python33\python.exe -tt
# -*- coding=utf-8 -*-

import sys
import time

def markTime(timeStampStr, preTimeStamp):
	currentTime = time.time()
	durTime = currentTime - preTimeStamp

	print(timeStampStr, 'Curent = ', currentTime, ',', 'Duration = ', durTime)

	return currentTime

def tempPrintList(l, n):
	print('Debug info: length = ', len(l))

	if (n == 0) or (n > len(l)):
		for e in l:
			if e != '':
				print(e)
	else:
		for i in range(n):
			if l[i] != '':
				print(l[i])
	
	return

def tempPrintDic(d, n):
	if (n == 0) or (n > len(d)):
		for e in d.keys():
			print(e, ' -> ', d[e], ';')
	else:
		kl = d.keys()
		for i in range(n):
			print(kl, ' -> ', d[kl[i]], ';')

def specSplit(specStr, splitStr, contL):

	tmpL = specStr.split('\n')
	tmpStr = ''

	for e in tmpL:
		if splitStr in e:
			if tmpStr != '':
				contL.append(tmpStr)
				tmpStr = ''
		else:
			if e != '':
				tmpStr = tmpStr + e + '\n'

	if tmpStr != '':
		contL.append(tmpStr)

	return

def getContent(inputfile, contL):
	splitStr = '<---分割线'

	specSplit(inputfile.read(), splitStr, contL)

	return

def getSpecPeriod(contL, sDate, eDate):


	return

def getSpecComments(contL, reffile, commentDic):

	return

def outputComments(reffile, commentDic):

	return

def main():
	if len(sys.argv) < 5:
		print('Usage: getComments.py sdate edate inputfile reffile outputfile')
		sys.exit(1)

	received = markTime('Beginning: ', 0)

	inputfile = open(sys.argv[3], 'r', encoding = 'gb18030')
	reffile = open(sys.argv[4], 'r', encoding = 'gb18030')
	outputfile = open(sys.argv[5], 'w')

	contL = []
	getContent(inputfile, contL)

#	tempPrintList(contL, 2)

	sDate = sys.argv[1]
	eDate = sys.argv[2]

	getSpecPeriod(contL, sDate, eDate)

	commentDic ={}
	getSpecComments(contL, reffile, commentDic)

	outputComments(reffile, commentDic)

	inputfile.close()
	reffile.close()
	outputfile.close()

	markTime('Ending: ', received)

	return

if __name__ == '__main__':
    main()
