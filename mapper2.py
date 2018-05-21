#!/usr/bin/python

import sys

file1 = open("article.txt")
lines=file1.read()
line=lines.splitlines()
#print line
bigrams = [b for l in line for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
    
#print bigrams
f = open( 'article_bi_mapped.txt', 'a' )
for bigram in bigrams:
    f.write(('{} , {} , {} '.format(bigram[0],bigram[1],1))+"\n")
    print ('{} , {} , {} '.format(bigram[0],bigram[1],1))

f.close()