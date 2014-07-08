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

	f.close()
	return stockLst

def checkIn(lineStr, stockLst):
	result = False

	if len(stockLst) != 0:
		for (stockID, stockName) in stockLst:
			if stockID in lineStr:
				result = True
				break

	return result

def getBookmark(file_to_get_same, baseStkLst):
	f = open(file_to_get_same, 'r')
	sepChar = '：'
	num = 0

	for line in f:
		parts = line.split(sepChar)

		if len(parts) != 0:
			if checkIn(parts[0], baseStkLst):
				print(line, end = '')
				num += 1

	print('\n\nTotal: ', num)
	f.close()
	return

def main():
	if len(sys.argv) < 2:
		print('Usage: getsame file-to-get-same(with comments) basefile(tdx format)')
		sys.exit(1)

	for parameter in sys.argv:
		print(parameter, ', ', end = '')

	file_to_get_same = sys.argv[1]
	basefile = sys.argv[2]

	getBookmark(file_to_get_same, getStockLst(basefile))

	return

if __name__ == '__main__':
	main()
