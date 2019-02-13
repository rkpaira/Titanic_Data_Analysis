#!/usr/bin/python

import sys

Total = 0
oldkey = None

# Loop around the data
# It will be in the format key \t val
# Where key is the store name, val is the sale amount
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) == 2:
    	
    	thiskey,thistotal = data_mapped
	#thiskey = s+" "+sex+" "+age

    	if oldkey and oldkey != thiskey:
        	print oldkey, "\t", Total
        	oldkey = thiskey;
        	Total = 0

    	oldkey = thiskey
    	Total += int(thistotal)

if oldkey != None:
    print oldkey, "\t", Total
