#!c:\Python33\python.exe -tt

import sys

def skip_header(f):
  skip_line_num = 5

  for i in range(skip_line_num):
    f.readline()

  return f

def gdict(dict, lines):
  '''
  Generate a dict like {'date string':[open, high, low, close],...}
  '''
  n = len(lines)

  for i in range(n - 1):
    l = lines[i]
    dts = l.split()
    data = dts[1:5]
    dict[dts[0]] = data

  return dict

def gdw(d):
  n = 10
  dw = {}
  op = 0.0
  cl = 0.0
  high = 0.0
  low = 10000.0 

  for key in sorted(d):
    if n == 0: break
    if n == 10: op = float(d[key][0])
    if n == 1: cl = float(d[key][3])
    if high < float(d[key][1]): high = float(d[key][1])
    if low > float(d[key][2]): low = float(d[key][2])
    n = n - 1

  l = [str(op), str(high), str(low), str(cl)]
  k = sorted(d)[9]
  dw[k] = l

  return dw

def pdict(fw, dict, n):

  for key in sorted(dict):
    s = key
    for str in dict[key]:
      s = s + '   ' + str
    fw.write(s)
    fw.write('\n')
    n = n - 1
    if n == 0:
      break

  return

def sfh(fopen, fwrite):
  fr = open(fopen, 'r')
  fr = skip_header(fr)
  d = {}
  fw = open(fwrite, 'w')

  lines = fr.readlines()
  d = gdict(d, lines)
  
  dw = {}
  dw = gdw(d)

  pdict(fw, dw, 10)

  fr.close()
  fw.close()
  return

def main():
  if len(sys.argv) != 3:
    print('usage: sfh.py inputstockfile outputfile')
    sys.exit(1)

  fopen = sys.argv[1]
  fwrite = sys.argv[2]
  sfh(fopen, fwrite)

if __name__ == '__main__':
  main()


