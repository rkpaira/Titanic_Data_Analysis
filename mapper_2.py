#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(",") 	
    if len(data) > 6:
          survived = data[1]
	  sex = data[4]
	  age = data[5]
	  s = survived+" "+sex+" "+age
	  print("{0}\t{1}".format(s,1))



