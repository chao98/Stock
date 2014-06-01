#!c:\Program Files (x86)\Python34\python.exe

import sys
from datetime import *

def getStockID(strLine):
	stockParameters = strLine.split('\t')
	stockID, stockName = '', ''

	if stockParameters[0].isdigit() and len(stockParameters) >= 2:
		stockID = stockParameters[0]
		stockName = stockParameters[1]

	return (stockID, stockName)

def getStockLst(stockFile):
	stockLst = []

	f = open(stockFile, 'r')

	for line in f:
		(stockID, stockName) = getStockID(line)
		if stockID != '':
			stockLst.append((stockID, stockName))

	return stockLst

def getStockDic(stockFile):
	stockDic = {}

	f = open(stockFile, 'r')

	for line in f:
		(stockID, stockName) = getStockID(line)
		if stockID != '': stockDic[stockID] = stockName

	f.close()
	return stockDic

def getDiff(newList, baseList):
	diffList = []

	for elem in newList:
		if not elem[0] in baseList:
			diffList.append(elem)

	return diffList

def formatPrint(nameList):
	today = str(date.today())
	head = '[新]，'
	strComment = '本周变化，'

	for elem in nameList:
		print(head, end = '')
		print(today, end = ', ')
		print(strComment, end = '')
		print(elem[0], '，', elem[1], '：')

	return

def main():
	if len(sys.argv) < 2:
		print('Usage: getdiff file-to-compare basefile')
		sys.exit(1)

	for parameter in sys.argv:
		print(parameter, ', ', end = '')

	file_to_compare = sys.argv[1]
	basefile = sys.argv[2]

	#print('\n>>> Base Stock Dic >>>')
	#print(sorted(list(getStockDic(basefile))))
	#print('\n>>> File to Compare >>>')
	#print(sorted(list(getStockDic(file_to_compare))))

	#print('\n>>> Diff Stock List >>>')
	#print(getDiff(getStockLst(file_to_compare), list(getStockDic(basefile))))

	#print('\n>>> format print Diff Stock List >>>')
	formatPrint(getDiff(getStockLst(file_to_compare), list(getStockDic(basefile))))

	return

if __name__ == '__main__':
	main()

