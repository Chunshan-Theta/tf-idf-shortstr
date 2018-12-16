# coding:utf-8
import numpy as np
import sys
sys.path.append('./jieba_zn/')
import jieba
import logging
jieba.setLogLevel(60)
from RKT_class import RKT
import wordfilter as sw

# 原始文本
SourceText = "對每一個決心學習寫程式的工程師來說，入坑之前，你也許只是一個「穿著正裝在辦公室裡上班」的人。你的學習歷程可能是這樣：如同一片樹葉，開始被各種建議拽著走，直到學完了每一個你能想像到的線上課程。最後，雖然你成功拿下了一份軟體開發的工作，但也對工程師有了新的認知：「那些看似正常的工程師們其實都是些『反社會』的怪人，鬼才知道他們經歷了什麼樣的精神創傷。」一份常見的程式學習過程：先從 Ruby 著手。很快，開始穿梭在 Scala, Clojure 和 Go 等其他語言中了。學習了Emacs，接著是 Vim，甚至還了解了 Dvorak 鍵盤佈局。接著又學習了 Linux，甚至還涉獵了 Lisp，以及用 Python 寫過程式，後來一直在命令行駐足半年多。一起來看一下學習寫程式要經歷哪幾個階段：剛開始學習時，你需要理解的東西很少。不論什麼目的、語言或背景，只需要明白一個「for」循環是什麼、如何用條件邏輯框架以及寫程式語言的基本語法。而且基礎知識終究沒有那麼多，所以知識體系在一開始並不複雜。但一旦掌握基礎，需要學習的知識面就一下變寬了，因為你需要了解更複雜的問題，例如了解程式錯誤以及什麼時候用哪些程式碼。這跟回答普通的問題截然不同，這個特殊的問題並沒有一個正確的答案，事情開始複雜起來。當進展到第三階段，知識面開始像氣球一樣膨脹。現在你開始知道需要什麼工具、用什麼程式語言、相關的計算機常識、如何寫模塊化的程式、面對對象寫程式、好的格式以及如何尋求幫助（這只是列舉了一些）。每次去谷歌搜尋或者駭客新聞，你就會發現更多你不知道但感覺要學習的知識。你產生了一個永遠不知道還有什麼不知道的念頭。"

seg_list = jieba.lcut(SourceText,cut_all=False)
seg_list = sw.filter(seg_list)
a = RKT(seg_list,20)
print SourceText
for i in seg_list:print i,'/',
print "\nTheta , keywords by textrank:"
#for i in a.Text_Array:print i
#for i in a.Text_Node_value:print i
#for i in a.TopText:print i,a.Text_Node[i],a.Text_Node_value[i]
for i in a.TopText_H2L:print (a.Text_Node[i]).encode('utf-8')+'/',


################################

from jieba import analyse
# 引入TextRank关键词抽取接口
textrank = analyse.textrank
print "\njieba , keywords by textrank:"
# 基于TextRank算法进行关键词抽取
keywords = textrank(','.join(seg_list))
# 输出抽取出的关键词
for keyword in keywords:
    print keyword + "/",

#################################
# 引入TF-IDF关键词抽取接口
tfidf = analyse.extract_tags

# 基于TF-IDF算法进行关键词抽取
keywords = tfidf(','.join(seg_list))
print "\njieba , keywords by tfidf:"
# 输出抽取出的关键词
for keyword in keywords:
    print keyword + "/",

