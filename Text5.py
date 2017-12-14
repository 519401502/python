# coding:utf-8
import uuid

import MySQLdb
import requests
import time

import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

connect = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='123456', db='rookie', charset='utf8')
cursor = connect.cursor()

def start(url):
    maincontent = requests.get(url)
    divs = BeautifulSoup(maincontent.content, 'html.parser')

    # 类型
    type = ''
    typediv = divs.find('div', attrs={'class': 'container main'})
    typedivson = typediv.find('div', attrs={'class': 'tab'})
    type = typedivson.text

    # 内容
    tags = divs.find('div', attrs={'class': 'article'})
    tagss = tags.find('div', attrs={'class': 'article-intro'})
    content = ''
    for v in tagss.contents:
        content = content + str(v)
        # print v


    # 标题
    print divs.find('meta', attrs={'name':'keywords'})['content']
    title = divs.find('meta', attrs={'name':'keywords'})['content']
    connectionMySql(type, title, content)



def connectionMySql(type, title, content):

    # cursor.execute('insert into src VALUES('
    #                + str(uuid.uuid1())
    #                + type +  title + content + time.strftime('%Y-%m-%d', time.localtime(time.time())) +')')
    # cursor.execute("insert into src VALUES('123', '123', '123','123', '132')")
    id1 = str(uuid.uuid1())
    title1 = title.strip()
    type1 = type.strip()
    content1= content.strip()
    time1 = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # sql = "insert into src VALUES(" \
    #       + "'"+ id1 + "'"+ "," \
    #       + "'"+type1 + "'"+ "," \
    #       + "'"+title1 + "'"+ "," \
    #       + "'"+content1 + "'"+ "," \
    #       + "'"+time1 + "'"+ ")"
    # print sql
    # cursor.execute(sql)

    # number = cursor.execute("select * from src WHERE title='" + title1 + "'" + "and type='" + type1 + "'")
    # if number > 0:
    #     print '内容重复，数据未重复存储'
    #     return
    sql1 = "insert into src VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(sql1, (id1, type1, title1, content1, time1))
    print '已爬取'+ title1


def getURL():
    urls = requests.get('http://www.runoob.com')
    soup = BeautifulSoup(urls.content, "html.parser")
    divs = soup.find('div', attrs={'class': 'container main'})
    lists = divs.find('div', attrs={'class': 'col middle-column-home'})
    listsas = lists.find_all('a', attrs={'class':'item-top item-1'})

    for item in listsas:
        getSonURL('http://' + item['href'][2:])
        print item.text + ' - - - - - ' + item['href'][2:]
        # print item['href'][2:]

def getSonURL(url):
    urls = requests.get(url)

    tag = url[22:].split('/')[0]

    soup = BeautifulSoup(urls.content, "html.parser")
    lists = soup.find('div', attrs={'class': 'col left-column'})
    sons = lists.find('div', attrs={'class': 'design'})
    sonsas = sons.find_all('a')
    for item in sonsas:
        # print '开始爬取'+ item['href']
        # urlstr = item['href']
        if len(item['href'].split('/')) == 3:
            # print 'http://www.runoob.com' + item['href']
            start('http://www.runoob.com' + item['href'])
        elif len(item['href'].split('/')) == 1:
            # print 'http://www.runoob.com/' + tag + '/' +item['href']
            start('http://www.runoob.com/' + tag + '/' +item['href'])

if __name__ == '__main__':
    # getURL()
    # start('http://www.runoob.com/html/html-attributes.html')
    # getSonURL('http://www.runoob.com/php/php-tutorial.html')
    # url = 'htmlhtml5-browsers.html'
    # print len(url.split('/'))
    # number = cursor.execute("select * from src WHERE title='" + "2" + "'" + "and type='" + "1" + "'")
    # print number
    # print cursor.execute("select * from src WHERE type='SQLite 教程'")
    print '  dsfsa  '
