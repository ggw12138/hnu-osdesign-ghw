#-*- encoding:UTF-8 -*-
#誉天暑期训练营
#引入bs4
from bs4 import BeautifulSoup
open_file=open('test.html','r',encoding='utf-8')
#将test.html的内容赋值给Html_Content
Html_Content=open_file.read()
open_file.close()
#使用html5lib解释器解析Html_Content的内容
soup=BeautifulSoup(Html_Content,'html5lib')
#将解析的内容全部输出
print('解析出来的标题内容是'+soup.title.getText())
#查找第一个标签P,并且输出标签
find_p=soup.find('p',id='python')
print('第一个p标签是'+find_p.getText())
#查找全部标签，并输出
find_all_p=soup.find_all('p')
for i ,k in enumerate(find_all_p):
    print('第'+str(i+1)+'p 是'+k.getText())