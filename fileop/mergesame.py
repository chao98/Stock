#!c:\Program Files (x86)\Python33\python.exe -tt

import sys

def fillmergelist(mergelist, line):

    parameters = line.split('\t')
    if len(parameters) != 0 and parameters[0].isdigit():
        mergelist.append(parameters[0])

    return mergelist

def mergesame(filenames):
    mergelist = []
    count = 0
    
    for file in filenames:
        f = open(file, 'r')
        count = count + 1
        
        if count < len(filenames):
            if len(mergelist) == 0:
                for line in f:
                    mergelist = fillmergelist(mergelist, line)
 #                   parameters = line.split('\t')
 #                   if len(parameters) != 0 and parameters[0].isdigit():
 #                       mergelist.append(parameters[0])
            else:
                templist1 = []
                for line in f:
                    templist1 = (templist1, line)
#                    parameters = line.split('\t')
#                    if len(parameters) != 0 and parameters[0].isdigit():
#                        templist1.append(parameters[0])
                
                templist2 = [x for x in mergelist for y in templist1 if x == y]
                mergelist = templist2
            
        else:
            tempdict1 = {}
            templist1 = []
            for line in f:
                parameters = line.split('\t')
                if len(parameters) >= 2 and parameters[0].isdigit():
                    tempdict1[parameters[0]] = parameters[1]
                    
            for e in sorted(tempdict1.keys()):
                if e in mergelist:
                    stockseq = e + ', ' + tempdict1[e]
                    templist1.append(stockseq)
                    
            mergelist = templist1
            
        f.close()

    return mergelist

def outputlist(mergelist):
    print("Total num is: ", len(mergelist))
    
    for elem in mergelist:
        print(elem, "; ", end = '')

    return

def main():
    if len(sys.argv) < 3:
        print('usage: mergesame inputfile1 inputfile2 ...[inputfileX]')
        sys.exit(1)

    filenames = sys.argv[1:]
    
    mergelist = mergesame(filenames)
    outputlist(mergelist)
    
    return

if __name__ == '__main__':
    main()
