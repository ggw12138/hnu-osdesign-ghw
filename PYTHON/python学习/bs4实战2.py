#-*- encoding:UTF-8 -*-
#誉天暑期训练营
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    r=requests.get(url,timeout=15)
    r.raise_for_status()
    r.encoding='utf-8'
    return r.text

def getSoup(url):
    txt=getHTMLText(url)
    soup=BeautifulSoup(txt,"html.parser")
    return soup

def getContent(soup):
    contents=soup.find('div',{'class':'usoft-listview-basic'})
    articles=[]
    for item in contents.find_all('li'):
        date1=item.find('span',{'class':'usoft-listview-item-date'})
        datestr=date1.string
        title=item.find('a')['title']
        articles.append([title,"---",datestr])
    return articles

if __name__ == '__main__':
    url='http://www.upln.cn/html/Channel_01/Column_0103/2.html'
    soup=getSoup(url)
    articleslist=getContent(soup)
    #显示爬取的信息
    for item in articleslist:
        for i in item:
            print(i,end='')
        print()
        print('-----------------------')

