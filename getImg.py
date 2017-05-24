# coding:UTF-8

import urllib.request
import re


def getHtml(url):
    return urllib.request.urlopen(url).read().decode("UTF-8")


def get_Html(url):
    return urllib.request.urlopen(url).read()


def writeToFile(path, name, data):
    file = open(path + name, 'wb')
    file.write(data)
    file.close()
    print('save img succeed')


url = 'http://www.u148.net/article/55557.html'
page = getHtml(url)
reg = r'src="(.+?\.jpg)"'
imgre = re.compile(reg)
img_list = re.findall(imgre, page)

path = "/Users/lzw/Desktop/mubai/workspace/python/weather/img/"
for i, img in enumerate(img_list):
    if i == 0:
        continue
    else:
        writeToFile(path, str(i) + ".jpg", get_Html(img))
