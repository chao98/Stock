#!c:\Program Files (x86)\Python33\python.exe -tt
# -*- coding=utf-8 -*-

import sys
import time
import re

preNameSet = set(['中国', '上海', '广东', '西藏', '北京', '天津', '重庆', '中航', '浙江'])
sufNameSet = set(['股份', '集团', '科技', '光电', '光伏', '实业', '能源', '技术', '机械', '通讯', '国际'])

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
	if (n <= 0) or (n > len(d)):
		n = len(d)

	for k in d:
		print(k, ' ---> \n')

		for e in d[k]:
			print(e)
			print('\n')

		print('#' * 20)

		n = n -1
		if n == 0:
			break
	
	return

def specSplit(specStr, splitStrL, contL):

	tmpL = specStr.split('\n')
	tmpStr = ''

	for e in tmpL:
		if (splitStrL[0] in e) or (splitStrL[1] in e):
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
	splitStrL = ['<---分割线', '<---段分割线']

	specSplit(inputfile.read(), splitStrL, contL)

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

def checkName(stockName):
	stockName = stockName.strip()
	tmpStr = ''

	for i in range(len(stockName)):
		if stockName[i].isspace != True:
			tmpStr = tmpStr + stockName[i]

	if len(tmpStr) == 4:
		h2Str = tmpStr[0:2]
		t2Str = tmpStr[2:4]

		if (h2Str in preNameSet) and (t2Str in sufNameSet):
			stockName = tmpStr
		elif (h2Str in preNameSet) and not (t2Str in sufNameSet):
			stockName = t2Str
		elif not (h2Str in preNameSet) and (t2Str in sufNameSet):
			stockName = h2Str
		else:
			stockName = tmpStr
	else:
		stockName = tmpStr

	return stockName

def getSpecComments(contL, reffile, commentDic):
	stockL = reffile.read().split(';')
	tmpL = []

#	print('>>> Debug info: in getSpecComments, to find sth in stockL')
#	tempPrintList(stockL, 0)

	for e in stockL:
		if e != '':
			(stockID, stockName) = e.split(',')
			
			if stockID != '':
				stockID = stockID.strip()

			if stockName != '':
				stockName = checkName(stockName)

			for lstr in contL:
				if (stockID in lstr) or (stockName in lstr):
					tmpL.append(lstr)

			e = e.strip()
			commentDic[e] = tmpL
			tmpL = []

	return

def outputComments(reffile, commentDic, outputfile):
	reffile.seek(0, 0)
	stockL = reffile.read().split(';')

#	print('>>> Debug info: in outputComments, to find sth in stockL')
#	tempPrintList(stockL, 0)

#	print(' >>> Debug info: comment in Dic')
#	tempPrintDic(commentDic, 2)

	for e in stockL:
		outputfile.write('\n')
		outputfile.write('>>>')
		outputfile.write(e)
		outputfile.write('\n')
		outputfile.write('-' * 20)
		outputfile.write('\n')

		e = e.strip()
		if e in commentDic:
			lstr = commentDic[e]
			
			if len(lstr) != 0:
				for aStr in lstr:
					outputfile.write(aStr)
					outputfile.write('\n')
			else:
				outputfile.write('( None )')
				outputfile.write('\n')

			outputfile.write('\n')
			outputfile.write('#' * 20)
			outputfile.write('\n')

		else:
			outputfile.write('None')
			outputfile.write('\n')

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
#	tempPrintList(contL, 0)

	commentDic ={}
	getSpecComments(contL, reffile, commentDic)

	outputComments(reffile, commentDic, outputfile)

	inputfile.close()
	reffile.close()
	outputfile.close()

	markTime('Ending: ', received)

	return

if __name__ == '__main__':
    main()
