#!/usr/bin/python

from operator import itemgetter
import sys
from operator import itemgetter

file1 = open("tweets_for_uni_mapped.txt")
lines=file1.read()
li=lines.splitlines()
dictZ = {}
for line in li:
    x = line.split('\t')
    key  = x[0]
    value = x[1]
    if(key in dictZ):
        dictZ[key] = int(dictZ[key])+1
    else:
        dictZ[key] = 1
 
dictY = sorted(dictZ.items(), key=itemgetter(1),reverse = True)

f = open( 'tweets_for_uni_reduced.csv', 'a' )

for elem in dictY:
    f.write((' {} , {} '.format(elem[0],elem[1])+"\n"))
    #print(elem[1])
f.close