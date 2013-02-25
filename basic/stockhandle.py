#!c:\Python33\python.exe -tt

import sys
import time
import datetime

def verCmdline(sysl):

  if len(sysl) != 3:
    print('>>>Usage: stockhandle.py inputfilename outputfilename')
    sys.exit(1)

  return (sysl[1], sysl[2])

def readInTdx(ifilename):
  l = []
  f = open(ifilename, 'r')

  l = f.readlines()

  # skip first 5 lines, in tdx file
  if len(l) > 5:
    l = l[5:]
  else:
    print('Input file with wrong format')
    sys.exit(1)

  # skil last line, in tdx file
  if len(l) > 1:
    l = l[:-1]
  else:
    print('Input file with wrong format')
    sys.exit(1)

  f.close()

  return l

def strpOrigStockData(linesOfStr):
  # Only keep daily stock origin data
  # e.g. date, open, high, low, close, volume
  nlStr = []
  
  for s in linesOfStr:
    l = (s.split())[:6]
    nlStr.append(l)

  return nlStr

def getStrDate(lStr):
  tformat = '%Y/%m/%d'
  datestr = lStr[0]
  # print(datestr, end = '        ')
  date_tp = time.strptime(datestr, tformat)
  
  that_date = datetime.date(date_tp[0], date_tp[1], date_tp[2])
  
  return that_date

def getDataList(ll, n):
  datalist = []

  for l in ll:
    datalist.append(l[n])

  return datalist

def sumf(dl):
  sumd = 0.0
  for i in dl:
    sumd = sumd + float(i)

  return sumd 

def createWeekData(ll):
  p_date = 0
  p_open = 1
  p_high = 2
  p_low = 3
  p_close = 4
  p_vol = 5

  opv = ll[0][p_open]
  clv = ll[-1][p_close]
  dt = ll[-1][p_date]
  hiv = str(max(getDataList(ll, p_high), key = float))
  lov = str(min(getDataList(ll, p_low), key = float))
  vol = str(sumf(getDataList(ll, p_vol)))

  return ('       ').join([dt, opv, hiv, lov, clv, vol])

def toWeekData(linesOfStr):
  l = []
  ltmp = []
  i = 0

  while i < len(linesOfStr):
    ltmp.append(linesOfStr[i])
    dtOfline = getStrDate(linesOfStr[i])
    j = 4 - dtOfline.weekday()
    FriDt = dtOfline + datetime.timedelta(j)

    k = 1
    while k <= j and getStrDate(linesOfStr[i + k]) <= FriDt: 
      ltmp.append(linesOfStr[i + k])
      k = k + 1

    l.append(createWeekData(ltmp))
    i = i + k
    # print()
    # print('i = %d,  j = %d,   k= %d' % (i, j, k))

  return l

def toWeek(linesOfStr):
  '''
  Turn the daily stock data into weekly stock data
  '''
  nlStr = []
  
  nlStr = strpOrigStockData(linesOfStr)
  nlStr = toWeekData(nlStr)

  return nlStr

def writeOut(ofilename, lStr):
  f = open(ofilename, 'w')

  for l in lStr:
    f.write(l)
    f.write('\n')

  f.close()
  return

def main():
  '''Tasks to do:
  1. Collect & verify arguments of the file
  2. Pass the input/output file for handling
  3. exit
  '''
  t1 = time.clock()

  ifilename = ''
  ofilename = ''
  (ifilename, ofilename) = verCmdline(sys.argv)

  if ifilename and ofilename:
    print('input file is: %s,\toutput file is: %s' % (ifilename, ofilename))
  else:
    print('Something wrong in the cmdline, please follow the guide')
    print('>>>Usage: stockhandle.py inputfilename outputfilename')
    sys.exit(1)
  
  linesOfStr = readInTdx(ifilename)
  if len(linesOfStr) == 0:
    print('Nothing in input file, please check')
    sys.exit(1)
  else:
    newLinesOfStr = toWeek(linesOfStr)
    writeOut(ofilename, newLinesOfStr)
    print('Successfully finished!')

  t2 = time.clock()
  print('Time used = %f (s)' % (t2))

''' execution of main program'''
if __name__ == '__main__':
  main()
