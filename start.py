#!usr/bin/env python3.6  
#-*- coding:utf-8 _*-  
""" 
@author:admin 
@file: start.py 
@time: 2018/01/28 
"""
from 超级小农民.className import *
from 超级小农民.classBooksName import *
from 超级小农民.article_lists import *
from 超级小农民.article_info import *

url = 'https://www.88dushu.com/'
sqlClassList = "select id,name,url from className"
contentNum = 0
if __name__ == '__main__':
    print('获取小说分类地址开始!')
    cbool = (className(url))
    print('获取小说分类地址完成!')
    if cbool:
        for val in sqlhelper.queryAll(sqlClassList):
            # print(val['url'])
            print('获取小说分类名称开始!')
            startPages, endPages = classBooksNamePage(val['url'])
            page = startPages
            numbers = range(startPages, endPages + 1)
            for i in numbers:
                print('当前第[%s]页,共计[%s]页' % (i, len(numbers)))
                # url1 = 'https://www.88dushu.com/sort5/%s/' % (i)
                url1 = val['url'].format('1',i)
                for u in classBooksName(url1):
                    for infos in article_lists(u):#返回详细文章地址
                        try:
                            title,classNameT,xsname,contents = article_info(infos)
                        except ssl.SSLError as e:
                            break
                        datas = {
                            'title':title,
                            'class':classNameT,
                            'content':contents,
                            'xsname':xsname
                        }
                        sql = "select id from content WHERE title = '{}'".format(title)
                        result = sqlhelper.queryAll(sql)
                        if len(result) == 0:
                            sqlhelper.insert('content',datas)
                            contentNum += 1
                            print('第%s篇爬取成功 名称:[%s] 分类:[%s] 标题:[%s]' %(contentNum,xsname,classNameT,title))


