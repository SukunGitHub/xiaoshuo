#!usr/bin/env python3.6  
#-*- coding:utf-8 _*-  
""" 
@author:admin 
@file: article_info.py 
@time: 2018/01/27 
"""

from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import ssl

# url = 'https://www.88dushu.com/xiaoshuo/88/88234/29672181.html'




def article_info(url):
    header = {
        'Host': 'www.88dushu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    ssl._create_default_https_context = ssl._create_unverified_context()
    # url = urllib.request.Request(url,headers=header)
    # get = urllib.request.urlopen(url,timeout=20,context=content)
    # print(get)
    # return
    get = requests.get(url)
    soup = BeautifulSoup(get.content,'html.parser')
    title = soup.select('body > div > h1')
    # fenlei1 = soup.find('div',class_='read_t')
    classNameT = soup.select('body > div.read_t > a')
    reg = '<h1> (.*)</h1>'
    title = re.findall(reg,str(title), re.I | re.S | re.M)
    html = soup.find('div',class_='yd_text2')
    # print(title[0])       #文章标题
    # print(html.text)        #文章内容
    # 'body > div.read_t > a:nth-child(3)'
    # return
    return title[0],classNameT[1].text,classNameT[2].text,html.text     # 文章标题，分类名称，小说名称，文章内容

# print(article_info(url))
