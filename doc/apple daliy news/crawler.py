#coding:utf-8
import requests as rq
import datetime
import time
import csv


def crawler(site_root,news_url,history_crawler):
    file_name = str(len(history_crawler)+1)
    Page = rq.get(site_root+news_url)#目標網佔
    content = Page.content
    content_start = Page.content.index('<div class="ndArticle_margin">')
    content_End = Page.content.index('<div id="fb-root"')
    content = content[content_start:content_End]
    content_tag_p = []
    content_text=""    
    while '<p' in content and '</p>' in content and len(content_tag_p)<=10:
        start = content.index('<p')
        end = content.index('</p>')
        #print start,end,content[:10]
        try:
            content_tag_p.append(content[start:end])
        except Exception as e:
            content_tag_p.append("none")
            print e
        
        content = content[end+3:]
    #for i in content_tag_p:print i

    for i in range(len(content_tag_p)):
        sub_content = str(content_tag_p[i])
        #print sub_content
        while '<' in sub_content and '>' in sub_content:
            start = sub_content.index('>')
            end = sub_content.index('<')
            try:
	            content_text+=str(sub_content[start+1:end]).rstrip()
            except Exception as e:
	            content_text+='break'
	            print e
            sub_content = sub_content[end+1:]
    #print content_text

    f = open("waitfortrain/"+str(file_name)+'.txt','wa')
    f.write(content_text)
    f.close()

    f = open("history.txt",'a')
    f.write(news_url+'\n')
    f.close()
    history_crawler.append(str(site_root+news_url+'\n'))

    content = Page.content
    content_start = content.index('ndArticle_pageNext')
    content = content[content_start:content_start+500]
    content_start = content.index('<a href="')
    content = content[content_start:content_start+50]
    content_start = content.index('/daily/')
    content_end = content.index('>')
    new_url = content[content_start:content_end-1]
    #print content[content_start:content_end]

   
    
    if site_root+new_url+'\n' not in history_crawler:
        try:
            print site_root+new_url
            crawler(site_root,new_url,history_crawler)
        except ValueError as e:
            print 'NODE END'
    else:
        print new_url+' the url is in history_crawler.txt'
f = open("history.txt",'r')
history_crawler=f.readlines()
#print history_crawler
f.close()
#crawler("https://tw.news.appledaily.com/headline",'/daily/20171203/37863184/',history_crawler)
#crawler("https://tw.entertainment.appledaily.com",'/daily/20171203/37862980/',history_crawler)
#crawler("https://tw.sports.appledaily.com",'/daily/20171203/37862844/',history_crawler)
#crawler("https://tw.finance.appledaily.com",'/daily/20171203/37863273/',history_crawler)
#crawler("https://tw.lifestyle.appledaily.com",'/daily/20171203/37862657/',history_crawler)
#crawler("https://tw.news.appledaily.com/international",'/daily/20171203/37862936/',history_crawler)
#crawler("https://tw.entertainment.appledaily.com",'/daily/20170511/37646443/',history_crawler)
#crawler("https://tw.news.appledaily.com/headline",'/daily/20170511/37646793/',history_crawler)
#crawler("https://tw.news.appledaily.com/international",'/daily/20170511/37646842/',history_crawler)
#crawler("https://tw.sports.appledaily.com",'/daily/20170511/37646710/',history_crawler)
#crawler("https://tw.finance.appledaily.com",'/daily/20170511/37646391/',history_crawler)
crawler("https://tw.lifestyle.appledaily.com",'/daily/20170511/37646262/',history_crawler)
