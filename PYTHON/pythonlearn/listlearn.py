list1 = []  #创建空列表
list1.append('dd')  #压入第一个元素
list1.append('pp')  #压入第二个元素
list1.append('mm')  #压入第三个元素
print(list1)

absent = 'dd'        #缺席名单
list1.remove(absent) #移除缺席者
list1.insert(0,'cc') #添加新加入者到开头
list1.insert(2,'ff') #添加新加入者到第3号位置
list1.append('gg')   #添加新加入者到末尾
print(list1)

while len(list1)>2: #当人数大于2的时候就弹出一个
    list1.pop()
print(list1)

del list1[1:2]      #删除第0个元素到第3个元素间的所有元素，不包括头尾
print(list1)

