#!c:\Program Files (x86)\Python33\python.exe -tt
# -*- coding=utf-8 -*-

import sys

def findStockList(lstr):
	stockSet = set()
	tmpStockid = ''
	count = 0
	lpos = 0

	for i in range(len(lstr)):
		if lstr[i].isdigit() == True:

			if (count == 0) and (lstr[i] == '0' or lstr[i] == '3' or lstr[i] == '6'):
				lpos = i
				tmpStockid = lstr[i]
				count = 1

			elif count >= 1 and count < 6:
				if (i - lpos) == 1:
					lpos = i
					tmpStockid = tmpStockid + lstr[i]
					count = count + 1
				else:
					tmpStockid = lstr[i]
					count = 1
					lpos = i
				
				if count == 6:
					if (i == len(lstr)) or (lstr[i+1].isdigit() == False):
						stockSet.add(tmpStockid)
						count = 0
					else:
						count = 0

	return stockSet

def filterStock(f, stockL):
	for l in f:
		stockL.extend(findStockList(l))

	return 

def main():
	if len(sys.argv) < 3:
		print('Usage: filterStock.py inputfile outputfile')
		sys.exit(1)

	inputfile = open(sys.argv[1], 'r', encoding = 'gb18030')

	stockL = []

	filterStock(inputfile, stockL)

	inputfile.close()

	outputfile = open(sys.argv[2], 'w')

	for i in range(len(stockL)):
		outputfile.write(str(stockL[i]))
		outputfile.write(';')

	outputfile.close()

	return

if __name__ == '__main__':
    main()
