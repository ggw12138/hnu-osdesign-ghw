import re
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
response = requests.get(
    'http://daohang.qq.com/?fr=hmpage', headers=headers)
print(response.url)
response.encoding = 'utf-8'
# print(response.text)
# 匹配不受限制 re.M:多行模式，改变'^'和'$'行为 re.L字符集的本地化
title = re.findall('_blank">(.*?)</a>', response.text, re.S)
for each in title:
    print(each)

#china = re.findall('color: #039;">(.*?)</span>', response.text, re.S)
#for each in china:
#    print(each)

