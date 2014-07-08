#!c:\Program Files (x86)\Python33\python.exe -tt

import sys, datetime

def extract(fopen, compact):
    int_sep = '，'
    ext_sep = '；'
    sep = '：'
    count = 0

    today = datetime.date.today()
    thisweek = today.isocalendar()[1]
    todaystr = str(today)
    thisweekstr = str(thisweek)

    msg = 'Unknown source'
    if 'dSKDJ' in fopen:
        msg = '日线SKDJ金叉'
    elif 'wSKDJ' in fopen:
        msg = '周线SKDJ金叉'
    elif 'dMACD' in fopen:
        msg = '日线MACD金叉'
    elif 'wMACD' in fopen:
        msg = '周线MACD金叉'
    elif 'nz' in fopen:
        msg = '本周逆势上涨'
    elif 'tianya' in fopen:
        msg = '天涯提示'

    f = open(fopen, 'r')
    for line in f:
        parameters = line.split('\t')
        id = parameters[0]
        if id.isdigit() and len(parameters) >= 2:
            name = parameters[1]

            if compact == '':
                print(id + int_sep + name + ext_sep, end = '')
            elif compact == 'c':
                print('[新WK%s]，%s，%s，%s' % (thisweekstr, msg, todaystr, str(id + int_sep + name + sep)))
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

