#!c:\Program Files (x86)\Python33\python.exe -tt
# -*- coding=utf-8 -*-

import sys
import time
import re

def markTime(timeStampStr, preTimeStamp):
	currentTime = time.time()
	durTime = currentTime - preTimeStamp

	print(timeStampStr, 'Curent = ', currentTime, ',', 'Duration = ', durTime)

	return currentTime

def tempPrintList(l, n):
#	print('Debug info: length = ', len(l))
	if len(l) == 0:
		print('Empty list!')

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

def getDate(aStr):
	dateStr = ''
	mStr = '\d\d\d\d-\d\d-\d\d'

	l = aStr.split('\n')
	match = re.search(mStr, l[0])

#	print(' >>> Debug info: l[0] = ', l[0])
	if match:
		dateStr = match.group()

#	print('Debug info: dateStr = ', dateStr)
	return dateStr

def checkDate(aStr, head):
	dateStr = ''
	dateL = aStr.split('-')

	if len(dateL) == 1:
		if head == True:
			dateStr = '-'.join([dateL[0], '01', '01'])
		else:
			dateStr = '-'.join([dateL[0], '12', '31'])

	elif len(dateL) == 2:
		if head == True:
			dateStr = '-'.join([dateL[0], dateL[1], '01'])
		else:
			dateStr = '-'.join([dateL[0], dateL[1], '31'])

	elif len(dateL) == 3:
		dateStr = aStr

	return dateStr

def getSpecPeriod(contL, sDate, eDate):
	markStart = 0
	markEnd = len(contL)
	sDate = checkDate(sDate, True)
	eDate = checkDate(eDate, False)

	if sDate > eDate:
		print('Error! Start Date is later than End Date, please have a check! Start Date = ', sDate, '; End Date = ', eDate)
		exit(1)

#	tempPrintList(contL, 0)
#	print(' >>> Debug info: sDate = ', sDate, '; eDate = ', eDate)
	
	for i in range(len(contL)):
		curDate = getDate(contL[i])
#		print(' >>> Debug info: current line = ', i, 'Current Date = ', curDate, '; Start Date = ', sDate)
		if curDate >= sDate:
			markStart = i
			break
	else:
		markStart = len(contL)

#	print(' >>> Debug info: found markStart = ', markStart)

	for i in range(markStart, len(contL)):
		curDate = getDate(contL[i])
#		print(' >>> Debug info: current line = ', i, '; Current Date = ', curDate, '; End Date = ', eDate)
		if curDate > eDate:
			markEnd = i
			break

	print('>>> Debug info: markStart = ', markStart, '; markEnd = ', markEnd)

	contL[:] = contL[markStart:markEnd]
#	tempPrintList(contL, 0)

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

	sDate = sys.argv[1]
	eDate = sys.argv[2]

	getSpecPeriod(contL, sDate, eDate)
	tempPrintList(contL, 0)

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
