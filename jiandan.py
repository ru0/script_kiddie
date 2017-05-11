#coding=utf-8
#python_demo 爬取煎蛋妹子图在本地文件夹
import requests
import threading
import time
import os
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Accept-Encoding': 'gzip',
    'Cookie': '1024679722=aada4mZxRMxqvInd7D6PSgq%2FIkpGFeGlZWAH1gqP8Q; __auc=57bffd35154a91de3cd5d3b1ddb; 1024679722=ebeaLZUFikSR1OE6lm5MJYJSV0V1DbcooxQr0CHu; jdna=596e6fb28c1bb47f949e65e1ae03f7f5#1467948344088; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1467001661,1467189261,1467685014,1467857178; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1467948345; _ga=GA1.2.1739476572.1438849462; _gat=1'}

def saveImgs(*allUrl):
    if len(allUrl) != 0:
        print '当前页面有', len(allUrl), '张图片即将下载'
        for l in allUrl:
            filename='d:/jiandanpic/'+parseName(l)
            saveImg(l,filename)
            time.sleep(1)
    else:
        print '当前页面无图片下载'
        
def saveImg(url,filename):
    print '当前图片url：',str(url)
    reponse = requests.get(str(url),headers=headers)
    image = reponse.content
    with open(filename,'wb') as f:
        f.write(image)
 
def parseName(url):
    u=str(url).split('.')
    filename=str(url)[30:55]+'.'+u[-1]
    return filename

def getAllImgUrl(url):
    allurl = []
    req=requests.get(url,headers=headers)
    # print req.status_code
    if req.status_code !=200:
        return allurl
    soup=BeautifulSoup(req.content,"lxml")
    links=soup.select('ol.commentlist img')
    print links
    for l in links:
        allurl.append('http:' + l.attrs.get('src'))
    return allurl

#多线程爬取
def crawler(n,m):
    for l in range(n,m):
        url = 'http://jandan.net/ooxx/page-' + str(l) + '#comments'
        u=getAllImgUrl(url)
        saveImgs(*u)
        
c1=threading.Thread(target=crawler,args=(1850,1900))
c2=threading.Thread(target=crawler,args=(1950,2000))
c3=threading.Thread(target=crawler,args=(2001,2064))
c1.start()
c2.start()
c3.start()
c1.join()
c2.join()
c3.join()
print 'success'