#!c:\Program Files (x86)\Python33\python.exe -tt

import sys

def extract(fopen, compact):
    int_sep = ', '
    ext_sep = '; '
    sep = ': '
    count = 0

    f = open(fopen, 'r')
    for line in f:
        parameters = line.split('\t')
        id = parameters[0]
        if id.isdigit() and len(parameters) >= 2:
            name = parameters[1]

            if compact == '':
                print(id + int_sep + name + ext_sep, end = '')
            elif compact == 'c':
                print(id + int_sep + name + sep)
            count = count + 1

    f.close()
    print()
    print(count)

    return

def main():
    if len(sys.argv) < 2:
    	print('usage: extract [-c] inputfile')
    	sys.exit(1)

    if len(sys.argv) == 2:
        fopen = sys.argv[1]
        compact = ''
    elif len(sys.argv) == 3:
        fopen = sys.argv[2]
        compact = 'c'

    extract(fopen, compact)

if __name__ == '__main__':
    main()

