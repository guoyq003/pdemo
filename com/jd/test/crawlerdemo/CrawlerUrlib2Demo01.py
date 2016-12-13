#!/usr/bin/env python
#coding=utf-8
import urllib2
import re
import os

#一个简单的爬虫案例
if __name__=='__main__':
  #1.访问网页，获取网页源代码
    url="http://www.qiushibaike.com/textnew/page/2/?s=4935195"
    userAgent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    headers={"User-Agent":userAgent}
    request=urllib2.Request(url=url,headers=headers)
    response=urllib2.urlopen(request)
    content=response.read()
    # print content
  #2.从网页源代码重提取想要的数据
    pattern='<div class="content">.*?<span>(.*?)</span>.*?</div>'
    items=re.findall(pattern,content,re.S)
    # print items
    path="D:/javatest/qiueshibaike"
    count=1
    for item in items:
        item_new = item.replace('<br/>','\n').replace('\n','')
        if not os.path.exists(path):
            os.mkdir(path)
        file_path=path+'/'+str(count)+'.txt'
        f=open(file_path,'w')
        f.write(item)
        f.write(item_new)
        f.close()
        count=count+1
  #3.保存抓取数据
  #4.抓取其他剩下的页面