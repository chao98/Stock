
import sys

def getStockID(linestr):
	items = linestr.split()

	if items[0] != '' and items[0].isdigit():
		return items[0]
	else:
		return ''

def pl(lstlines):
	for i, lines in enumerate(lstlines):
		print('>>> %d >>>' % i)
		for l in lines:
			print(l)

	return

def rmsame(filelist):
	if len(filelist) < 2:
		print('Not enough file to compare and remove the same')
		sys.exit(1)

	filecontent = []
	for filename in filelist:
		with open(filename) as f:
			lines = f.readlines()
		filecontent.append(lines)

	for i in range(len(filecontent)):
		for l1 in filecontent[i]:
			stockID = getStockID(l1)
			
			if stockID != '':
				for j in range(i+1, len(filecontent)):
					lines = filecontent[j]
					for n, l2 in enumerate(filecontent[j]):
						if stockID in l2:
							lines.pop(n)
					filecontent[j] = lines

	#pl(filecontent)
	for filename, lines in zip(filelist, filecontent):
		nfilename = 'n' + filename
		with open(nfilename, 'w') as f:
			for l in lines:
				f.write(l)

	return

def main():
	if len(sys.argv) < 3:
		print('Usage: rmsame file1 file2 [...filen]')
		sys.exit(1)

	rmsame(sys.argv[1:])

	return

if __name__ == '__main__':
	main()
