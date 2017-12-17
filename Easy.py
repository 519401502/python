# coding:utf8
import uuid
import time
from uuid import uuid1

import MySQLdb
import requests
from bs4 import BeautifulSoup

import sys
reload(sys)
# 解决编码问题
sys.setdefaultencoding('utf8')

type = ''

connect = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='123456', db='rookie', charset='utf8')
cursor = connect.cursor()

def urlhandler():
    requ = requests.get('http://www.yiibai.com/v3.php?app=all')
    soup = BeautifulSoup(requ.content, 'html.parser')
    # 获取主要的整体内容
    content = soup.find('article', attrs={'class': 'article-content'})
    itemall = content.find_all('div', attrs={'class':'item item-0'})
    for item in itemall:
        type = item.find('h2').get_text()
        parseritem(item.find_all('li'), type)

def savedata(title, content, type, subtype, page):
    # 创建时间
    time_ = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # id
    id_ = str(uuid.uuid1())
    title_ = title.strip()
    content_ = content.strip()
    type_ = type.strip()
    subtype_ = subtype.strip()
    page_ = page.strip()

    number = cursor.execute("select * from yibai_src WHERE title='" + title_ + "'" + "and type='" + type_ + "'" + " and subtype='" + subtype_ + "'")
    if number > 0:
        print '提示: 内容重复，数据未重复存储'
        return
    sql1 = "insert into yibai_src VALUES(%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql1, (id_, type_, subtype_, title_, content_, time_, page_))
    print '已爬取: ' + title_


def parseritem(items, type):
    for item in items:
        src = item.find('a')
        href = src['href']
        subtype = src.get_text()
        describe = item.get_text()[len(subtype):]
        # 解析一套内容的章节
        requ = requests.get(href)
        soup = BeautifulSoup(requ.content, 'html.parser')
        titlelist = soup.find('ul', attrs={'class': 'pagemenu'})

        # 计算总数
        sum = 0
        for number,item in enumerate(titlelist):
            sum = number
        page = 0
        for number,item in enumerate(titlelist):
            # print item
            if(number < 3 or number > sum - 2) :
                continue
            ainfo = item.find('a')
            # print ainfo['href']
            # print ainfo.get_text()
            if ainfo == -1 or ainfo == None:
                continue
            try:
                if ainfo['href'] == None:
                    continue
            except Exception as e:
                continue
            # 得到标题
            # print ainfo.get_text()
            page = page + 1
            title, content = parsercontent(ainfo['href'])
            if title == None or content == None:
                continue
            savedata(title, content, type, subtype, str(page))






# 解析内容网页
def parsercontent(url):
    try:
        requ = requests.get(url)
        soup = BeautifulSoup(requ.content, 'html.parser')
        contentsrc = soup.find('div', attrs={'class': 'content'}).find('div', attrs={'class': 'article-content'})
        i = 0
        # 内容
        content = ''
        for number, item in enumerate(contentsrc):
            i = number
        for number, item in enumerate(contentsrc):
            if number >= i - 3:
                continue
            content = content + str(item).decode('utf-8')
        # 标题
        title = soup.find('h1', attrs={'class': 'article-title'}).get_text()
        return title, content;
    except Exception as e:
        return None, None

if __name__ == '__main__':
    urlhandler()


