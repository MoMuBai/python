# coding:utf-8


from bs4 import BeautifulSoup
import urllib.request


def getHtml(url):
    header = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    req = urllib.request.Request(url=url, headers=header)
    return urllib.request.urlopen(req).read()


def getSoup(html):
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.title.string)
    print(soup.prettify())

def writeToFile(path,name,data):
    file = open(path+name,'wb')
    file.write(data)
    file.close()
    print('Succeed')



url = 'http://blog.csdn.net/marksinoberg/article/details/51379507'
html = getHtml(url)
getSoup(html)
