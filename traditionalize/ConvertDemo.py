#!/usr/bin/env python
#-*- coding: utf-8 -*-

#下載以下兩個文件
#zh_wiki.py:https://github.com/skydark/nstools/blob/master/zhtools/zh_wiki.py
#langconv.py:https://github.com/skydark/nstools/blob/master/zhtools/langconv.py

from langconv import Converter

line = u"籃球"
print 'source: ',line

line = Converter('zh-hans').convert(line)
print type(line), line



print '*'*20



line = u"篮球"
print 'source: ',line
line = Converter('zh-hant').convert(line)
print type(line), line


f = open('dict.txt','r')
w = open('dict_traditaion.txt','a+')
for i in f.readlines(): 
      
    i = i.split(' ')
    i2 = i[0]
    #print i2,len(i2)
    if len(i2)>3:
        i2 = unicode(i2,"utf-8")
        i2 = Converter('zh-hant').convert(i2)
        
        w.write(i2.encode('utf-8')+' '+i[1]+' '+i[2])
        print i2.encode('utf-8')+' '+i[1]+' '+i[2]+'\n'
    
f.close()
w.close()

