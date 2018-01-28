#!usr/bin/env python3.6  
#-*- coding:utf-8 _*-  
""" 
@author:admin 
@file: classBooksName.py 
@time: 2018/01/27 
"""
from bs4 import BeautifulSoup
import requests
import urllib.request
import ssl
import re
import time

contexts = ssl._create_unverified_context()

# url = 'https://www.88dushu.com/sort6/44/'
# url = 'https://www.88dushu.com/sort4/1/'
def classBooksNamePage(url):
    header = {
        'Host':'www.88dushu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    # url = urllib.request.Request(url,headers=header)
    # get = urllib.request.urlopen(url,context=contexts,timeout=10)
    get = requests.get(url)
    # soup = BeautifulSoup(get.read().decode('gbk'), 'html.parser')
    soup = BeautifulSoup(get.content, 'html.parser')

    # bookNames = soup.find_all('span', class_='sm')
    bookPages = soup.find('em', id='pagestats').text
    # for title in bookNames:
    #     res = r'<span class="sm"><a href="(.*)"><b>(.*)</b></a></span>'
    #     urls = re.findall(res, str(title), re.I | re.S | re.M)
    #     for k, v in urls:
    #         print('URL地址是:%s 书名称是:%s' % (k, v))
    #     print('当前第[%s]页,共计[%s]页' % (bookPages.split('/')[0], bookPages.split('/')[1]))
    #     page += int(bookPages.split('/')[0])
    return int(bookPages.split('/')[0]),int(bookPages.split('/')[1])


def classBooksName(url):
    header = {
        'Host': 'www.88dushu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    # url = urllib.request.Request(url,headers=header)
    # get = urllib.request.urlopen(url,context=contexts,timeout=10)
    # soup = BeautifulSoup(get.read().decode('gbk'), 'html.parser')
    get = requests.get(url)
    soup = BeautifulSoup(get.content, 'html.parser')
    bookNames = soup.find_all('span', class_='sm')
    # bookNames = soup.find_all('div', class_='booklist')
    # bookNames = soup.select('body > div > ul > li > span > a')
    CBKurls = []
    for title in bookNames:
        res = r'<span class="sm"><a href="(.*)"><b>(.*)</b></a></span>'
        urls = re.findall(res, str(title), re.I | re.S | re.M)
        for k, v in urls:
            u = 'https://www.88dushu.com%s' % (k)
            # print('URL地址是:https://www.88dushu.com%s 书名称是:%s' % (k, v))
            CBKurls.append(u)
    return CBKurls

# startPages,endPages = classBooksNamePage(url)
# page = startPages
# numbers = range(startPages,endPages+1)
# for i in numbers:
#     print('当前第[%s]页,共计[%s]页' % (i, len(numbers)))
#     url1 = 'https://www.88dushu.com/sort5/%s/' % (i)
#     classBooksName(url1)


# classBooksNamePage(url)






