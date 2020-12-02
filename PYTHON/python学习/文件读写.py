#-*- encoding:UTF-8 -*-
#誉天暑期训练营
f=open("test.txt","a+",encoding='utf-8')
# str1=f.read(4)
# print(str1)
# str2=f.readlines()
# print(str2)
# for line in f:
#     print(line,end=" ")
f.write("hello\n")
f.write("继续写入")
f.close()
"""
f=open("文件名称","模式")
w:写文件,如果文件不存在就创建新的文件，如果文件存在，就会把原来的文件内容清空，重新创建文件
r:读文件,一定要保证文件是存在的，如果不存在就会保存
read()读取文件里面的所有的内容
readline()读取文件里面的第一行内容
readlines()读取文件里面的所有行内容
"""
