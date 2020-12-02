#-*- encoding:UTF-8 -*-
#誉天暑期训练营
# import re
# pattern = re.compile(r'\d')#定义匹配的字符串
# m = pattern.search('aaee45one12twothree34four')
# """match()从头开始匹配，如果一旦匹配成功就返回match对象，后面的不会继续再匹配，如果没有匹配成功就结束程序
#    findall()匹配所有的数据
#    search()从头开始匹配，如果第一个没有找到，就继续往后面搜索，一旦匹配到程序就结束，后面不会继续匹配
# """
# print(m)
# text="This is the last one"
# res=re.match('(.*) is (.*?).*',text,re.M|re.I)
# if res:
#     print('res.group():',res.group())
#     print('res.group(1):', res.group(1))
#     print('res.group(2):', res.group(2))
#     print('res.groups():', res.groups())
# else:
#     print('No match!')
import re
# # 将正则表达式编译成 Pattern 对象
# pattern = re.compile(r'\d+')
# # 使用 search() 查找匹配的子串，不存在匹配的子串时将返回 None
# # 这里使用 match() 无法成功匹配
# m = pattern.search('hello 123456 789')
# if m:
#     # 使用 Match 获得分组信息
#     print ('matching string:',m.group())
#     # 起始位置和结束位置
#     print ('position:',m.span())
# import re
# pattern = re.compile(r'\d+')
#
# result_iter1 = pattern.finditer('hello 123456 789')
# result_iter2 = pattern.finditer('one1two2three3four4', 0, 10)
# print (result_iter1)
# print (result_iter2)
#
# print ('result1...')
# for m1 in result_iter1:   # m1 是 Match 对象
#     print ('matching string: {}, position: {}'.format(m1.group(), m1.span()))
#
# print ('result2...')
# for m2 in result_iter2:
#     print ('matching string: {}, position: {}'.format(m2.group(), m2.span()))
import re
# p = re.compile(r'(\w+) (\w+)')
# s = 'hello 123, hello 456'
#
# print (p.sub(r'hello world', s))
# print (p.sub(r'\2 \1', s))
#
# def func(m):
#     print(m)
#     return 'hi' + ' ' + m.group(2)
#
# print (p.sub(func, s))
# print (p.sub(func, s, 2))

title = '你好，hello，世界'
pattern = re.compile(r'[\u4e00-\u9fa5]+')
result = pattern.findall(title)

print (result)