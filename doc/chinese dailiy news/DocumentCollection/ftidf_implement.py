# -*- coding:utf-8 -*-
import os,sys,io
sys.path.append('./jieba_zn/')

import jieba
import logging as log
jieba.setLogLevel(60)
log.basicConfig(format='\n%(levelname)s:%(message)s',level=log.INFO)


import json 

tfidf_ditc = {}

with io.open("./outpute.txt","r",encoding='utf-8') as f:
    tfidf_ditc = json.loads(f.read())
    log.info(tfidf_ditc)
a =tfidf_ditc[u'在']
print(a)