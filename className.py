#!usr/bin/env python3.6  
#-*- coding:utf-8 _*-  
""" 
@author:admin 
@file: class.py 
@time: 2018/01/27 
"""

from bs4 import BeautifulSoup
import requests
import ssl
from 超级小农民.mysql.MySQLHelper import *

sqlhelper = MySQLHelper('localhost','root','')
sqlhelper.setDB('xiaoshuo')
# url = 'https://www.88dushu.com/sort1/1/'
# url = 'https://www.88dushu.com/'

def className(url):
    content = ssl._create_default_https_context
    header = {
        'Host': 'www.88dushu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    get = requests.get(url)
    soup = BeautifulSoup(get.content, 'html.parser')
    className = soup.select('body > div > div > ul > li > a')

    for title in className[1:10]:
        cUrl = 'https://www.88dushu.com%s' % (title.get('href'))
        datas = {
            'name':title.text, #小说分类
            'url':cUrl,     #分类url地址
        }
        sql = "select id from className where name='{}'".format(title.text)
        req = sqlhelper.queryAll(sql)
        if len(req) == 0:
            sqlhelper.insert('className',datas)
            continue
    return True