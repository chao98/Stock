#!c:\Python33\python.exe -tt

import sys
import os
import os.path


'''
1. Create a directory, naming 'data' under current directory
2. Store txt format stock data file into that directory
3. run this program as" ExtractSpecData data 2013/03/08
4. Output is to extract stock data of specified date 
'''

def main():
    if len(sys.argv) != 3:
        print('Missing directory name or date!')
        exit(1)

    dir = sys.argv[1]
    date = sys.argv[2]

    if not os.path.exists(dir):
        print('Wrong directory name!')
        exit(1)

    filenames = os.listdir(dir)
    print(len(filenames), ' files found: ',filenames)

    outlines = []
    outlines.append('ID\tOepn\tHigh\tLow\tClose\tVol\tAmount')

    for filename in filenames:
        fullfilename = os.path.join(dir, filename)

        f = open(fullfilename, 'r')

        lines = f.readlines()
        stockid = lines[0][:6]
        del lines[0]
        del lines[1]

        for l in lines:
            if l.find(date) != -1:
                newline = stockid + l[10:]
                outlines.append(newline)
                break

        f.close()

    print(outlines)
    for l in outlines:
        print(l)

    return

''' -------main----------'''
if __name__ == '__main__':
    main()


