#-*- encoding:UTF-8 -*-
#誉天暑期训练营
"""
全局变量
局部变量
"""
def func1(x,y):
    x1=x
    y1=y
    z=100
    print("x1=",x1)
    print("y1=",y1)
    print("z=",z)
    func2()
    return

def func2():
    x1=10
    y1=20
    z=0
    print("x1=",x1)
    print("y1=",y1)
    print("z=", z)

# func1('a','b')
#定义全局变量
# basis=100
# def func1(x,y): #计算总分
#     sum=basis+x+y
#     return sum
#
# def func2(x,y):
#     avg=(basis+x*0.9+y*0.8)/3
#     return avg
#
# score1=func1(75,62)
# score2=func2(75,62)
# print(score1,score2)
# print(basis)

# def func3(x,y):
#     basis=90
#     sum=basis+x+y
#     return sum
# print(func3(10,20))
# print(basis)
basis=100
#在函数内部声明全局变量
def func4(x,y):
    global basis #声明basis是函数外的全局变量
    print(basis)
    basis=90
    sum=basis+x+y
    return sum

# print(func4(10,20))
# print(basis)

"""python里面的内置函数"""
# r1=range(10)
# print(list(r1))
# r2=range(0,10)
# print(list(r2))
# r3=range(0,10,3)
# print(list(r3))
"""map()函数是用于将指定序列中所有的元素作为参数,通过指定函数,将结果构成一个新的序列返回
map(function,iter1[iter2,....])
reduce(function,iter)
"""
m1=map(lambda x,y:x*y,(3,4,5),(4,5,6))
print(type(m1))
print(m1)
print(list(m1))

from functools import reduce
r1=reduce(lambda x,y:x+y,(1,2,3,4,5))
print(r1)
r2=reduce(lambda x,y:x+y,(1,2,3,4,5),10000)
print(r2)
r3=reduce(lambda x,y:x*10+y,[1,2,3,4,5])#基于整数列表生成整数数值
print(r3)
z1=zip([1,3,5])
print(list(z1))