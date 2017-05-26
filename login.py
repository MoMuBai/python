# coding:utf-8
import urllib.request, urllib
import http.cookiejar

# 封装cookie信息
cookie = http.cookiejar.MozillaCookieJar()
cookieProc = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookieProc)
urllib.request.install_opener(opener)

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

postData = {
    'username': 'quickly520@126.com',
    'password': 'quicklymost'
}


def GetUrlRequest(iUrl, iStrPostData, header):
    postdata = urllib.parse.urlencode(iStrPostData)
    postdata = postdata.encode(encoding='UTF8')
    req = urllib.request.Request(
        url=iUrl,
        data=postdata,
        headers=header)
    result = urllib.request.urlopen(req).read()
    return result


otherurl = 'http://my.csdn.net/my/score'
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'

# respose = opener.open(url,postData)

GetUrlRequest(url, postData, headers).decode('utf-8')

req = urllib.request.Request(url=otherurl, headers=headers)
result = opener.open(req).read().decode('utf-8')
print(result)

#
# response = opener.open(url, postData)
#
# for item in cookie:
#     print(item.name + '=' + item.value)
