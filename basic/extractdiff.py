#!c:\Program Files (x86)\Python33\python.exe -tt

import sys

def getstockstr(line):
	stockName = ''

	parameters = line.split('\t')
	id = parameters[0]
	if id.isdigit() and len(parameters) >= 2:
		name = parameters[1]
		stockName = id + ', ' + name

	return stockName

def getstocklst(fName):
	f = open(fName, 'r')
	stockNameLst = []

	for line in f:
		stockName = getstockstr(line)

		if stockName != '':
			stockNameLst.append(stockName)

	f.close()
	return stockNameLst

def getstockset(fNameLst):
	stockNameSet = set()

	for fName in fNameLst:
		f = open(fName)
		for line in f:
			stockName = getstockstr(line)

			if stockName != '':
				stockNameSet.add(stockName)

		f.close()

	return stockNameSet

def diffstocklst(stockNameLst, stockNameSet):
	diffStockNameLst = []

	if len(stockNameLst) == 0 or len(stockNameSet) == 0:
		print('Something must be wrong, please check!')
		sys.exit(1)

	for stockName in stockNameLst:
		if (stockName in stockNameSet) == False:
			diffStockNameLst.append(stockName)

	return diffStockNameLst

def extractdiff(fNameLst):

	if len(fNameLst) <= 1:
		print('usage: extract file-for-compare file1-to-compare [file2-to-compare ...]')
		print('more parameters needed')
		sys.exit(1)

	newStockNameLst = getstocklst(fNameLst[0])

#	print('debug in extractdiff: ')
#	stocknamelstprint(newStockNameLst)

	oldStockNameSet = getstockset(fNameLst[1:])
#	stocknamesetprint(oldStockNameSet)

	diffStockNameLst = diffstocklst(newStockNameLst, oldStockNameSet)

	return diffStockNameLst

def stocknamelstprint(stockNameLst):

	if len(stockNameLst) == 0:
		print('No differeence at all!')
		sys.exit(1)

	for stockName in stockNameLst:
		print('2014-01-12' + ', ' + stockName)

	print('Total num is: ', len(stockNameLst))

	return

def stocknamesetprint(stockNameSet):

	if len(stockNameSet) == 0:
		print('Someting must be wrong with old files, please check!')
		sys.exit(1)

	for stockName in stockNameSet:
		print('2014-01-12' + ', ' + stockName)

	print('Total num is: ', len(stockNameSet))

	return

def main():
    if len(sys.argv) < 3:
    	print('usage: extract file-for-compare file1-to-compare [file2-to-compare ...]')
    	sys.exit(1)

    if len(sys.argv) >= 3:
    	fNameLst = sys.argv[1:]

    stockNameLst = extractdiff(fNameLst)
    stocknamelstprint(stockNameLst)

    return

if __name__ == '__main__':
    main()
