#!usr/bin/env python3.6  
#-*- coding:utf-8 _*-  
""" 
@author:admin 
@file: article_lists.py 
@time: 2018/01/27 
"""

import requests
from bs4 import BeautifulSoup
import urllib.request
import ssl



# url = 'https://www.88dushu.com/xiaoshuo/88/88234/'


def article_lists(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    context = ssl._create_unverified_context()
    reponse = urllib.request.Request(url,headers=headers)
    html = urllib.request.urlopen(reponse,timeout=30,context=context)
    soup = BeautifulSoup(html,'html.parser')
    list = soup.select('body > div > ul > li > a')
    urls = []
    for val in list:
        urls.append(url+val.get('href'))
        # print(val.text,url+val.get('href'))     #标题与url
    return urls

# for i in article_lists(url):
#     print(i)