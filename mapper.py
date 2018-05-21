#!/usr/bin/python

import sys

file1 = open("article.txt")
lines=file1.read()
li=lines.splitlines()
f = open( 'article_uni_mapped.txt', 'a' )
for line in li:
    line=line.strip()
    words=line.split()
    for word in words:
         f.write('%s\t%s' % (word,1)+"\n")
         print '%s\t%s' % (word,1)
f.close()