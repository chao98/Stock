#!c:\Program Files (x86)\Python33\python.exe -tt

import sys

def take_num_name(line):
    num_name = ''
    int_sep = ', '
    ext_sep = '; '

    if '(' in line and ')' in line:
        pos = line.find(')')
        if pos != -1:
            line = line[(pos + 1):]
            l = line.split('\t')
            if len(l) >= 2:
                num_name = l[0] +int_sep + l[1] + ext_sep
    else:
        l = line.split('\t')
        if len(l) >= 2:
            num_name = l[0] + int_sep + l[1] + ext_sep

    return num_name

def pr_list(name, stock_list):
    if len(stock_list) > 0:
        print(name, ': ', len(stock_list))
        for item in stock_list:
                print(item, end = '')

    print('\n')
    return

def divide(fopen):
    (best, good, over, bad) = '(best)', '(good)', '(over)', '(bad)'
    (list_best, list_good, list_over, list_bad, list_nocomments) = [], [], [], [], []

    f = open(fopen, 'r')
    for line in f:
        if best in line:
            list_best.append(take_num_name(line))
        elif good in line:
            list_good.append(take_num_name(line))
        elif over in line:
            list_over.append(take_num_name(line))
        elif bad in line:
            list_bad.append(take_num_name(line))
        else:
            list_nocomments.append(take_num_name(line))

    f.close()

    pr_list(best, list_best)
    pr_list(good, list_good)
    pr_list(over, list_over)
    pr_list(bad, list_bad)
    pr_list('no comment', list_nocomments)

    return

def main():
    if len(sys.argv) != 2:
        print('usage: divide inputfile')
        sys.exit(1)

    if len(sys.argv) == 2:
        fopen = sys.argv[1]
        divide(fopen)

    return

if __name__ == '__main__':
    main()

