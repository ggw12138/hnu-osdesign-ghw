#-*- encoding:UTF-8-*-
"""
分支结构
单分支
if 条件语句:
   执行语句
多分支
if 条件语句:
elif(条件语句)：
else:
嵌套分支结构
if 条件语句1:
    if 条件语句2:
        执行语句
    else:
        执行语句
else:
    if 条件语句1:
       执行语句
    else:
       执行语句
"""
# a=int(input('请输入您的年龄:'))
# if a<18:
#     print('未成年，网吧不能去，不能到处浪...')
# else:
#     print('可以出去浪，但是要注意安全...')


"""根据月份来计算天数"""
#定义月份
# month=eval(input("请输入您的月份: "))
# days=0;
# if(month==1 or month==3 or month==5 or month==7 or month==8or month==10or month==12):
#     days=31
# elif(month==4 or month==6 or month==9 or month==11 ):
#     days=30
# else:
#     days=28
#
# print("{}月份的天数为{}天".format(month,days))
"""
做一个简易计算购书款程序。如果有会员卡，购买5本书以上，书款按照7.5折计算，5本以下按照8.5折计算；如果没有会员卡，购买5本书以上
，书款按照8.5折结算，5本以下，按照9.5折结算
"""
# #定义一个初始变量，目的就是为了区分会员和非会员的区别
# flag=1 #flag=1表示有会员卡
# books=8 #购书数量
# price=234#单价
# if flag==1:
#     if books>=5:
#         actuaplay=price*0.75*books
#     else:
#         actuaplay=price* 0.85*books
# else:
#     if books>=5:
#         actuaplay=price*0.85*books
#     else:
#         actuaplay=price* 0.95*books
#
# print("您实际付款金额是:",actuaplay)

"""循环语句结构
for i in range(n):
  <statements>
计算1-100中能被3整除的数之和

 while 判断条件:
     执行语句
 现在有一组如下的数据numbers=[12,37,5,42,8,3]，请你从这个数据中同时找出，奇数和偶数
 even=[]
 odd=[]
    
"""
# print(range(10))
# s=0
# for i in range(100):
#     if i %3==0:
#         s+=i
#         print(i)
# print(s)
# a=1
# while a<10:
#     print(a)
#     a+=2
# stra='12a3456'
# print(len(stra))
# # print(stra[0],stra[1])
# print(stra[0:3])
# print(stra[::-1])
numbers=[12,37,5,42,8,3]
even=[] #定义偶数列表
odd=[] #定义奇数列表
while len(numbers)>0:
    number=numbers.pop()
    if(number % 2==0): #如果为偶数
        even.append(number) #把对应的数据添加到even里面
    else:
        odd.append(number)

print(even,odd)

