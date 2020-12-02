import urllib.request
url = 'https://github.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Referer': 'https://github.com',
    'Connection': 'keep-alive'
}
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')
f = open('test.txt', 'w', encoding='utf8')
f.write(html)
f.close()
