#!/c/Python33/python tt

# Define a main() function
def main():
  StockfileName = 'SH600031.TXT'
  Stockfile = open(StockfileName, 'r')

  Stockfile.readline()

  for i in range(10):
    line = Stockfile.readline()
    item_list = line.split()

    str_comma = ', '
    new_line = str_comma.join(item_list)
    print(new_line)

  Stockfile.close()

# This is the standard boilerplate that calls the main() function. 
if __name__ == '__main__':
  main()

