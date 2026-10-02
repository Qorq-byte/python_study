# num=int(input())
# num1=int(input())
# sum=num+num1
# print(sum)
# name=input()
# num2=float(input())
# num3=float(input())
# sum1=num2+num3
#type(sum)
#print(sum1)
# sting=('nihao')
# print(type(sting))
# word='hello'*3
# print(word)
#word='chen shu hang'
#name='chen shu han'
# print(name[0])
# print(name[:5])
# print(name[-5:])
# word='friends'
# find_the_evil_in_your_friends=word[0]+word[2:4]+word[-3:-1]
# print(find_the_evil_in_your_friends)
# word='asdfghjklkldsaf'
# print(word[:-5])

# word='你好'
# print(type(word))

# weight=input('请输入树涵的体重')
# height=input('请输入树涵的身高')
# weight=float(weight)
# height=float(height)
# BIM=weight/height**2
# print(BIM)

# phone_number='12345678'
# hiding_number = phone_number.replace(phone_number[:4],'*'*4)
# print(hiding_number)

# num=12
# num1=12
# sum=num+num1
# print(sum)
# print('1+1+1')
# search = '168'
# num_a = '1386-168-0006'
# num_b = '1681-222-0006'
# print(search + ' is at ' + str(num_a.find(search)) + ' to '+ str(num_a.find(search) + len(search)) + ' of num_a')
# print(search + ' is at ' + str(num_b.find(search)) + ' to '+ str(num_b.find(search) + len(search)) + ' of num_b')

# print('%s,%f,%d'%(123,12345,324525))
#print('%.2f'%(123.2222222))

# num=(input('请输入树涵的大小'))

# num=11                                 #占位符
# n1=('%s%s'%(num,num))
# n2=('%s'%(num))
# print(num,n1,n2)
# print(int(num) + int(n1) + int(n2))

# number='chenshuhan'
# print('树涵的名字是:'+number
# number='陈树涵'
# age='18'
# print(f'树涵的名字{number}，树涵的年龄{age}')
# num=123456789
# print(f'num={num:.3f}')
# print(99%3)
# print(23//2)
# print(14/2)
# a,b,c=11,'niii','树涵'
# print(a)
# print(b)
# print(c)
# age=11
# age+=1111
# print(age)
# age*=3
# print(age)
# a=11
# b=122
# print('a'>'b')
# print(12<11 and 13>12)
# print(11==11 and 13.>11)
#print(not('11'=='12'))
# name='chenshuhan'
# name1="shuhan"
# print(name=='chenshuhan' or name1=='shuhan')
# print('{} a word she can get what she {} for.'.format('With', 'came'))
# print('{preposition} a word she can get what she {verb} for'.format(preposition='With', verb='came'))
# print('{0} a word she can get what she {1} for.'.format('With', 'came'))
# print('{} is chenhshuhan.'.format('who'))
# name=input('请输入树涵的名字')
# print('{} is my son.'.format(name))
# def fahrenheit_converter(C):
#     fahrenheit = C * 9/5 + 32
#     return str(fahrenheit) + '˚F'
# a=fahrenheit_converter(33)
# print(a)


# def fahrenheit_converter(c):
#     fahrenheit = c * 9 / 5 + 32
#     print(str(fahrenheit) + '˚F')
# C2F = fahrenheit_converter(35)
# print(C2F)
#
# def g_converter(c):              #定义
#      g=c*1000
#      print(str(g)+'g')
# weight=g_converter(5)
# print(weight)

# list=('a', 'b', 'c')                 #列表
# print(list[1])
# dict1 = {'a':1, 'b':2, 'c':3}
# print(dict1['a'])
# print('a' in dict1)
# print('a'in list)

# import random                             #随机模块
# guess_num=random.randint(0,122)
# print(guess_num)

# import random
# guess_num=random.randint(1,45)
# user_num=input('请输入树涵的大小')
# if user_num == guess_num:
#     print('恭喜你猜对啦，摸摸你的头')
# else:
#     print('www你猜错啦，给你一巴掌')

# name=input('请输入树涵的名字')               #if
# age=input('请输入树涵的年龄大小')
# if name=="树涵" and age=='18':
#     print('恭喜进入页面')
# else:
#     print('输入错误，你无法进入')

# word='陈树涵是我亲爱的孩子'                #列表
# print(word[1:3])
# print(word[:-1])

# def area(base_up,base_down,height):                     #定义赋值
#     return 2/3*base_up*32*base_down*height
# area(11,23,22)
# print(area(11,23,22))

# base_up=1
# base_down=2
# height=3
# area=(base_up,base_down,height,height)
# print()

# user_size=int(input('请输入树涵的大小'))               #多分支
# if user_size<1:
#     print('树涵你不乘哦')
# elif user_size>77:
#     print('树涵你太棒了')
# elif 1<user_size<5:
#     print('不愧是树涵')
# else:
#     print('hhhh')

# num=int(input('请输入树涵的大小'))                      #if嵌套
# if 0<num<100:
#     print(f'你输入的{num}不符合树涵的大小')
#     if num%2==0:
#         print(f'你输入的{num}仍不符合树涵的大小')
#     if num//2!=0:
#         print(f"你输入的{num}已经很接近树涵的大小了，请加油")
#     else:
#         print(f'你输入的{num}依旧不符合树涵的大小')
# else:
#     print(f'孩子，连{num}都猜不到，回去洗洗睡吧')

# num1=int(input('请输入一个数字'))                             #也是if嵌套，建议看这个
# num2=int(input('请再输入一个数字，可以与num1相同也可以不同'))
# a=input('请输入1234任意一个数字')
# if a=='1':
#     print(num1+num2)
# elif a=='2':
#     print(num1/num2)
# elif a=='3':
#     if num1<num2:
#         print(num1-num2)
#     else:
#         print(num2%num1)
# else:
#     print(num1//num2)

# a=int(input('请输入一个数字'))                            #三目运算符的两种方法
# b=int(input('请输入一个数字'))
# max_num= a if a > b else b
# print(max_num)
# print(a if a > b else b)

# n=1                                   #循环
# while n<=5:
#     print('树涵是巴嘎')
#     n+=1

# result=0
# n=1                                             #起始值
# while n<=10:                                     #输出的最后结尾
#     result+=n
#     n+=1                                        #变化的程度
#     print('输出的结果',result)                    #不断计算，并连续输出结果      （与下一列是不同的输出方法）
# print('输出的计算结果',result)                     #一次性计算完所有值，并一次输出所有值的结果
#（此处与上处的结果的笔记相同）
#（当想对循环设置条件时可以利用if函数）

# n=0
# while n<3:
#     username=input('请输入树涵的名字')
#     password=input('请输入树涵原神的密码')
#     if username=='原批' and password=='123456':
#         print('欢迎登入原神')
#         n=4                                           #通过加入超出变量的值从而停止循环
#     else:
#         print('请重新输入')
#     n+=1
#     print('已循环一次')

# n=0                                                   #通过加入break结束循环
# while n<5:
#     if n==4:
#         break
#     print(f'{n=}')
#     n+=1

# list=[1,2,3,4,4,5]                            #for循环
# for a in list:
#     print(a)

# dict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
# for key in dict:
#     print(key)

# for a in range(0,10,2):        #for循环生成数字，其中（）第一个数字为起始值，第二个数字为结束值，但不包括，第三个数字为变化的程度
#     print(a)

# a=0                             #数字相加的总值
# for b in range(0,20,2):
#     a+=b
# print(f'{a=}')

# for a in range(4):
#     if a==2:
#         print('树涵完蛋了')
#         break
#
#     print('好耶，树涵没完蛋')

# num=10                          #倒序循环
# while num>0:
#     print(num)
#     num-=1
#     if num==5:
#         break
# print('你好，该程序已经结束')

# for a in range(1,12):                           #可以用end将循环写于一行
#     if a==3 and 5 and 6:   /a in list[    ]                      #continue函数            两种方法
#         continue
#     print(a,end=',')

# while True:                                                    #循环与嵌套
#     name=input('请输入树涵的名字')
#     if name==('陈树涵'):
#         print('你好，name正确，请输入密码')
#         password=input('请输入树涵的原神密码')
#         if password==('123456'):
#             print('你好，欢迎登入原神')
#             break
#         else:
#             print('你好，请重新开始登入')
#     else:
#         print('你好，name错误，请重新输入')

# while True:                                          #相对于上面那个部分，这个部分更方便
#     name=input('请树涵输入你的名字')
#     if name !=('陈树涵'):
#         print('你好，请重新输入正确的名字')
#         continue
#     a=input('请输入树涵的原神账号')
#     if a==('1234'):
#         print('欢迎进入原神')
#         break
#     else:
#         print('你好，请重新开始输入')

# a=1                                         #while的内嵌循环
# while a<=5:
#     print(f'今天是星期{a}')
#     a+=1
#     b=1
#     while b<=2:
#         print(f'今天吃的第{b}顿饭')
#         b+=1

# for row in range(5):                       #for的内嵌循环
#     for num in range(row):
#         print('ai',end=" ")
#     print()

# for row in range(1,10):                      #99乘法表
#     for col in range(1,row+1):
#         print(f'{row}*{col}={row*col}',end=" ")
#     print()

# list=['a','s','d','f']
# for i in  list:
#     print(i)
#
# num=0
# while num<4:
#     print(list[num])
#     num+=1

# def func():                                              #定义函数
#     while True:
#         name=input('请输入你的名字')
#         if name!=('陈树涵'):
#             continue
#         password=input('请输入你的密码111')
#         if password==('1234'):
#             print('欢迎登入')
#             break
#         else:
#             print('请重新输入')
# func()

# def func(x,y):                          #x,y是形参
#     print(x,y)
# a=10                                    #a,b,'ni''hao'为实参
# b=12
# func(a,b)
# func('ni','hao')

# def func(x,y):                                    #调用函数的灵活应用
#     rey=x+y
#     print(rey)
# func(23,2)
# func(222222222,222222222222222222)

# def welcome(name,age):                            #位置参数，数目必须一致
#     print(f'{name},{age}')
# welcome('陈树涵','13')
#/  welcome(nama='',age='')                           #关键字参数。与上一行是差不多的，只是多了指示。

# def welcome(name,age='17'):                           #默认参数。。。默认参数必须在非默认参数之后，否则会报错
#     print(f'{name},{age}')
# welcome('john')
# //welcome('john','18')               #若你输出自己的一个值，则按你输出的值输出，即不输出默认参数值

# def func(*args):                     #可变位置参数的应用，进行数字总和计算
#     total=0
#     for i in args:
#         total+=i
#     print(total)
# func(1,2,3,4,5)
# func(11,23,44)
#
# def func1(x,y,**kwargs):               #可变关键字参数
#     print(x,y)
#     print(kwargs)
#     print(kwargs['c'])                    #此处是对可变关键字参数的选取
# func1(x=1,y=2,c=3)

# def func():
#     print('陈树涵是my son')
#     return 22222        #若返回多个值则会已元组的形式输出。return之后的代码不会执行。若有多个return则会执行第一个return,后面不会执行
# print(func())                        #此处会将返回值一块输出
# func()                                  #此处只会输出print（）里面的值
#
# def func():                                                 #近期内容的大致应用
#     username=input('请输入树涵的名字')
#     password=input('请输入树涵的密码')
#     if username == '陈树涵' and password == '1234':
#         return True
#     else:
#         return False
# def check():
#     print('欢迎查看树涵的小秘密')
# print('请输入正确的名字和密码')
# while True:
#     result = func()
#     if result:
#         check()
#         break
#     else:
#         print('请重新登入')

#变量查找优先级：局部名称空间--全局名称空间---内置名称空间                 全局是不能调用内嵌的函数
# x=12
# def func():
#     x=111
#     print(x)               #此处优先输出111，因为为局部
# func()
# print(x)                   #此处优先输出12，因为为全局

# def func():
#     x=111
#     print(x)
#     def func2():
#         x=222
#         print(x)
#     func2()
# func()

# a=12
# def func():
#     global a                     #利用global告诉python  a为全局变量
#     a=1111
#     print(a)
# func()
# print(a)               #此时，该处输出结果为1111，但必须先调用函数，否则书橱结果为12

# def outer():
#     a=12
#     def inner():
#         nonlocal a         #nolocal 声明a不是局部变量，只能在嵌套中使用
#         a+=12
#         print("inner",a)
#     inner()
#     print("outer",a)
# outer()

# a="hello"
# print(a,type(a))          以字符串str进行输出
# a1=a.encode()             进行编码    （）内可以选择编码方式
# print(a1,type(a1))        以字节bytes进行输出
# a2=a1.decode()            进行解码
# print(a2,type(a2))        以字符str进行输出

# name='chenshuhan'
# print('x'in name)         输出false
# print('c'in name)         输出true
# print('c'not in name)     输出false
# print('x' not in name)    输出true
#字符串的话是作为一个整体去找的

# 切片
# 含义：指对操作对象截取其中一部分的操作
# 语法：[开始的位置：结束的位置：步长]
# 包前不包后：即从起始的位置开始，到结束位置的前一位(不包括结束位置本身)
# 步长：表示选取间隔，不写步长，则默认间隔为1；步长的绝对值大小决定切取的间隔，正负号决定切取方向。正号表示从左往右取值，负数表示从右向左取值

