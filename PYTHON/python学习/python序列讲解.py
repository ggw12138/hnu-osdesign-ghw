#-*- encoding:UTF-8 -*-
#誉天暑期训练营
#创建列表
lst1=[]
lst2=["python",12,2.71828,[0,0],12]
lst3=[21,10,55,100,2]
print("python" in lst2)
lst2+=lst3 #合并列表
# print(lst2)
lst3.append('a')
# print(lst3)
# lst4=lst2.copy()
# print(lst4)
# lst3.remove(10) #删除指定的内容
# lst3.pop()#如果没有指定索引，那么就默认移除最后一个元素，如果有指定那么就是根据指定的索引位置移除元素
# print(lst3)
# for item in lst2:
#     print(item,end=",")

# i=0
# while i<len(lst2):
#     print(lst2[i],end='')
#     i+=1
"""元组"""
# tup1=('physics','en',1997,2000)
# tup2=(1,2,3,4,5,6)
# tup3=('hello',)
# print(type(tup3))
# tup4="a","b","c","d"
# print(type(tup4))
"""元祖和列表的区别,元祖和列表都是有序的，但是元祖是不可变，列表就像铅笔，写错了还可以改，元祖就像钢笔，一旦
定义了之后是不可变的"""
# #将元祖转换为列表
# lst1=list(tup1)
# lst1.append(999)
# print(lst1)
# tup1=tuple(lst1)
# print(tup1)
"""字典 dict={key:value} dict={键:值},在字典里面key值是唯一的"""
dict1={'001':'钟浩','002':'钟浩','003':'小钟'}
# print(dict1)
#修改字典元素，必须保证key值是存在的
# dict1["002"]='小白'
# print(dict1)
# print(dict1.keys()) #获取所有的key值
# print(dict1.values())#获取所有的value的值
# print(dict1.items())#同时获取key和value的值
# for key,value in dict1.items():
#     print(key,value)
# dict1.popitem()
# print(dict1)
# dict2={"name":"John","email":"ul@u2"}
# dict1.update(dict2)
# print("更新之后的结果为:",dict1)
# dict3=dict1.copy()
# print(dict3)
# dict3.clear()#清空字典里面的元素，但是不删除元素
# print(dict3)
"""python里面的集合"""
# aset=set("python")
# print(aset)
# test1={'python'}
# print(type(test1))
# bset=set([1,2,5,5,2])#集合是不能重复的
# print(bset)
a=set([10,20,30])
b=set([20,30,40])
set1=a&b
print(set1)  # 交集，返回一个新的集合，包括同时在集合a和b中的元素
set2=a|b
print(set2) #并集,返回一个新的集合,包含集合a和b中的所有元素
set3=a-b
print(set3) #差集，返回一个新的集合，包含集合a中但是不在集合b中
set4=a^b
print(set4)#补集,返回一个新的集合，包含集合a和b中的元素但不包括同时在其中的元素


