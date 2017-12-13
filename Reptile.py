# coding:utf8
import codecs
import cookielib
import json
import urllib
import urllib2

# # 第一种方法通过rullib2
import uuid

import requests
#
# urlText = "http://www.baidu.com"
# response1 = urllib2.urlopen(urlText)
# # print response2.read()
#
# # 第二种方法
# request = urllib2.Request(urlText)
# request.add_header("user-agent", "Mozilla/5.0")
# response2 = urllib2.urlopen(request)
# print response2.read().decode("utf-8")

# 通过requests方式爬虫
# resp = requests.get('http://www.baidu.com')
# print resp.status_code
# # 数据获取
# r = requests.get('http://115.159.78.127:8080/interranking/topten')
# # 获取内容
# print r.content
# # 获取内容2
# print r.text
# # 获取头部信息
# print r.headers
#
# # 爬虫代理
# proxies = {
#     "http": "http://192.168.31.1:3128",
#     "https": "http://10.10.1.10:1080"
# }
# requests.get("http://xlzd.me", proxies = proxies)

# request 会话对象其实就是session
# session = requests.Session()
# # 通过登录接口初始化session
# session.post('http://xlzd.me/login', data={'user': 'xlzd', 'pass': 'mypassword'})
# # 发送文章
# session.put('http://xlzd.me/new', data={'title': 'title of article', 'data': 'content'})


# 爬取豆瓣电影
from bs4 import BeautifulSoup

url = 'http://movie.douban.com/top250'


def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }

    return requests.get(url, headers=headers).content


def main():
    parsePage(download_page(url))


def parsePage(html):
    with codecs.open('xvhuichuang', 'wb', encoding='utf-8') as fp:
        soup = BeautifulSoup(html, "html.parser")
        movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'}, recursive=True)
        for movie_li in movie_list_soup.find_all('li'):
            detail = movie_li.find('div', attrs={'class': 'hd'})
            urllists = detail.find('a')
            fp.write(urllists.get('href') + '\n')

            print urllists.get('href')
            # for urllist_item in urllists:
            #     print urllist_item.getText()

            # movie_name = detail.find_all('span', attrs={'class': 'title'})
            # for movie_name_item in movie_name:
            #     print movie_name_item.getText()
            # print detail.find('span', attrs={'class': 'other'}).getText()
        nextLists = soup.find('div', attrs={'class': 'article'})
        atss = nextLists.find('div', attrs={'class': 'paginator'})
        # print nextLists
        hrefList = atss.find_all('a')
        for vv in hrefList:
            fp.write(vv.get('href') + '下一页'.decode('utf-8'))
            print(vv.get('href') + '下一页'.decode('utf-8'))

        # lists = soup.find('ol', attrs={'class': 'gird_view'})
        # for item in lists.find_all('li'):
        #     tag = item.find('div', attrs={'class': 'hd'})
        #     tag.find()

i = 10
def parseYellow():
    while True:
        j = 3
        setting = json.loads(requests.get('http://m.jilehezi.com/api/v1.2/?page='+ str(j)).text)
        j = j + 1
        lists = setting['data']['items']
        for item in lists:
            # http: // m.jilehezi.com / video /
            # urllib.urlretrieve('http://m.jilehezi.com/video/' + str(item['id']), str(item['id'])+'.mp4')
            maintext = requests.get('http://m.jilehezi.com/video/' + str(item['id']), "html.parser")
            soun = BeautifulSoup(maintext.text)
            # print soun
            sounson = soun.find('div', attrs={'class':'wraper'})
            # print sounson
            urlstr = sounson.find('video').get('src')
            print urlstr[2:]
            urllib.urlretrieve('http://' + urlstr[2:], str(uuid.uuid1())+'.mp4')

            # print item['id']

        # soup = BeautifulSoup(requests.get('http://m.jilehezi.com/video/').content, 'html.parser')
        # maindivs = soup.find('div', attrs={'class': 'waterfall'})
        # print maindivs
        # urllib.urlretrieve('url', 'path')



if __name__ == '__main__':
    # main()
    parseYellow()



# http://104.221.151.139:14442/480/44/4439adfe9a0efb4b538abfafb94919e488f6fa79.mp4