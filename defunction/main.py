# def mufunc(name,times):
#     for i in range(times):
#         print(f'i love {name}')
# mufunc('kk',5)

# def myfunc(x,y):
#     return x/y
# print(myfunc(3,6))
# def div(x,y):
#     if y==0:
#         return 'y不能为0'
#     return x/y
# print(div(2,0))

# def myfunc(o,sv,t='3'):#默认参数在最后
#     return':'.join((t,sv,o))
# print(myfunc('1','2','3'))
# print(myfunc(o='1',sv='2',t='3'))
# print(myfunc('1','2',t='3'))
# print(myfunc('1','2'))
# help(abs)
# help(sum)#/前的参数必须是位置参数 ，即abs（x=1.5）不被允许

# def myfunc(a ,*,b,c):#*右侧b，c只能是b=''.c=''.
#     return(a,b,c)
# print('123','2',sep=' ')#收集参数
# def myfunc(*arg):
#     print('有{}个参数'.format(len(arg)))
#     print('第二个参数是:{}'.format(arg[1]))
# myfunc(1,2,3)
# def myfunc1(*arg):#收集参数后，只能使用关键字参数,单一的*是匿名的收集参数
#     return arg
# print(myfunc1(2,3,4)) #返回值被元组打了个包
# x,y,z=myfunc1(2,3,4)#解包

# def myfunc(**kwargs):
#     print(kwargs)
# myfunc(a=1,b=2,c=3)#生成一个列表键值对

# def myfunc(a,*b,**c):
#     print(a,b,c)
# myfunc(1,2,3,4,x=1,y=2,z=3)
# def myfunc(a,b,c,d):
#        print(a,b,c,d)
# arg=(1,2,3,4)
# myfunc(*arg)#在定义函数中*代表着使用元组的方式打包参数，在调用函数的时候即为解包
# kwarg={'a':1,'b':2,'c':3,'d':4}
# myfunc(**kwarg)
# def myfunc(x,**y):
#     print(x,y)
# myfunc(x=1,y=2,z=3)

# def myfunc():
#     x=500
#     print(x)
# x=900
# myfunc()
# x=880
# def myfunc():
#     global x
#     x=550
#     print(x)
# myfunc()
# def funa():
#     x=800
#     def funb():
#         x=500
#         print('is funb x=',x)
#     funb()
#     print('is funa x=',x)
# funa()
# def funa():
#     x=800
#     def funb():
#         nonlocal x
#         x=500
#         print('is funb x=',x)
#     funb()
#     print('is funa x=',x)
# funa()
# str='123'
# str(1)#根据LEGB原则 全局变量global 高于 Bulid in  ，local 为局部作用域 就是在函数内定义的变量 enclosed 为嵌套函数的外层作用域
# def funa():
#     x=800
#     def funb():
#         print(x)
#     return funb
# funa()()
# funny=funa()
# funny()#暗藏玄机， 我们认为将funa（）的返回值给予funny后，funny应当是funb并与funa再无瓜葛，但事实上内部保存了funa的外层作用域，
# def power(exp):
#     def exp_of(base):
#         return base**exp
#     return exp_of
# square=power(2)
# cube=power(3)#可以通过一个函数制造不同函数
# print(square(3),cube(2),sep=' and ')#即为闭包

# origin = (0, 0)        # 这个是原点
# legal_x = [-100, 100]  # 限定x轴的移动范围
# legal_y = [-100, 100]  # 限定y轴的移动范围
# # 好，接着我们定义一个create()函数
# # 初始化位置是原点
# def create(pos_x=0, pos_y=0):
#     # 然后我们定义一个实现角色移动的函数moving()
#     def moving(direction, step):
#     # direction参数设置方向，1为向右或向上，-1为向左或向下，如果是0则不移动
#     # step参数是设置移动的距离
#         # 为了修改外层作用域的变量
#         nonlocal pos_x, pos_y
#         # 然后我们真的就去修改它们
#         new_x = pos_x + direction[0] * step
#         new_y = pos_y + direction[1] * step
#         # 检查移动后是否超出x轴的边界
#         if new_x < legal_x[0]:
#             # 制造一个撞墙反弹的效果
#             pos_x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             pos_x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             pos_x = new_x
#         # 检查移动后是否超出y轴边界
#         if new_y < legal_y[0]:
#             pos_y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             pos_y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             pos_y = new_y
#         # 将最终修改后的位置作为结果返回
#         return pos_x, pos_y
#     # 外层函数返回内层函数的引用
#     return moving

# import numpy as np
# def predict(X,w,b):
#     return X*w+b
# def loss(X,Y,w,b):
#     return np.average((predict(X,w,b)-Y)**2)
# def gradient(X,Y,w,b):
#     w_gradient=2*np.average(X*(predict(X,w,b)-Y))
#     b_gradient=2*np.average(predict(X,w,b)-Y)
#     return w_gradient,b_gradient
# def train(X,Y,iteration,lr):
#     w=b=0
#     for i in range(iteration):
#         print('iteration:{a},loss:{b}'.format(a=i,b=loss(X,Y,w,b)))
#         w_gradient,b_gradient=gradient(X,Y,w,b)
#         w-=w_gradient*lr
#         b-=b_gradient*lr
#     return(w,b)
# X,Y=
# w,b=train(X,Y,iteration=2000,lr=0.01)
# print('w={a},b={b}'.foramt(a=w,b=b))
# print('prediction:X={a},Y={b}'.format(20,predict(20,w,b)))

# import time
# def time_master(func):
#     def call_back():
#         print('程序开始运行')
#         start=time.time()
#         func()
#         over=time.time()
#         print(f'耗费{(over-start):.2f}秒.')
#     return call_back
# @time_master#语法糖，功能相等于 myfunc=time_master(myfunc)
# def myfunc():
#     print('正在运行')
#     time.sleep(2)
# myfunc()
#
# import time
# def add(func):
#     print('1')
#     def inner():
#         print('11')
#         return func()+'111'
#     return inner
# def cube(func):
#     print('2')
#     def inner():
#         print('22')
#         return func()+'222'
#     return inner
# @add
# @cube
# def test():
#     return 'test'
# print(test())


# import time
#
# def delay(func):
#     def call_func():
#         time.sleep(1)
#         func()
#     return call_func
#
# def fib():
#     back1, back2 = 0, 1
#     @delay
#     def func():
#         nonlocal back1, back2
#         back1, back2 = back2, back1 + back2
#         print(back1, end=' ')
#     return func
#
# def get_fib(n):
#     f = fib()
#     for i in range(n):
#         f()
# n = int(input("请输入需要获取的斐波那契数："))
# get_fib(n)

# import time
# def longer(msg):
#     def time_master(func):
#         def call_back():
#             start=time.time()
#             func()
#             over=time.time()
#             print(f'{msg}耗费了{(over-start):.2f}秒')
#         return call_back
#     return time_master
# @longer(msg='A')
# def funcA():
#     print('程序A运行中')
#     time.sleep(1)
# funcA()

# mapped=map(lambda x:ord(x),'abcd')
# print(list(mapped))

# print(list(filter(lambda x:x%2==0,range(10))))

# def counter(): # 生成一个实时的可迭代对象 ，不能进行索引， 每一次调用生成一个元素。
#     i=0
#     while i<=5:
#         yield i
#         i+=1
# c=counter()
# for i in c:
#     print(i)
# print(c)#<generator object counter at 0x000001FA5EBDDF90>

# def fib():
#     back1,back2=0,1
#     while True:
#       yield back1
#       back1,back2=back2,back1+back2
# f=fib()
# for i in range(10):
#     print(next(f))

# print((i**2 for i in range(10)))#类似于列表，返回一个生成器对象，因此内容为一个一个生成，区别于列表.<generator object <genexpr> at 0x000001600B78DF90>
# for i in (i**2 for i in range(10)):
#     print(i)

# def factiter(n):#递归与迭代对比
#     result=n
#     for i in range(1,n):#result 初始result就是5
#         result*=i
#     return result
#
# print(factiter(5))
#
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))

# def fibIter(n):
#     a=1
#     b=1
#     c=1
#     while n>2:
#         c=a+b
#         a=b
#         b=c
#         n-=1
#     return c
# print(fibIter(12))
#
# def fibRecur(n):#
#     if n<=2:
#         return 1
#     else:
#         return fibRecur(n-1)+fibRecur(n-2)
#
# print(fibRecur(9))

# def time(n:dict[str,int],s:int=3)->list:#建议n为字典，键值对为str和int，s为int，按照要求返回值应为list
#     return list(n.keys())*s
# print(time({'a':1}))
#
# print(time.__annotations__)#函数自省  #.doc 则为阅读函数文档

# import functools #高级函数模块
# a=functools.reduce(lambda x,y:x*y,range(1,11))#functools内置高级函数模块，reduce第一参数为函数，第二参数为可迭代对象，返回将可迭代对象依次代入函数的数值。
# print(a)
#
# cube=functools.partial(pow,exp=3)#本质类似于闭包 参数里pow为一个函数
# print(cube(3))

# import functools #内省对于闭包函数不返回其本身 而是return值
# def time_master(func):
#     def call_turn():
#         print("start")
#         func()
#         print('ending')
#     return call_turn
# @time_master
# def myfunc():
#     print('lodarding')
# myfunc()
# print(myfunc.__name__)#返回值是call——turn 而不是myfunc 因此可以增加修饰器给装饰器
#
# def time_master(func):
#     @functools.wraps(func)#参数为即将调用的函数
#     def call_turn():
#         print("start")
#         func()
#         print('ending')
#     return call_turn
# @time_master
# def myfunc():
#     print('lodarding')
# myfunc()
# print(myfunc.__name__)#此时name返回值为myfunc

# f=open('fishfish.txt','w')#会对以存在的内容覆盖,即以存在内容消失 慎用!!!!!!!!
# f.writelines(['this is a tentative document.\n ','i wish it is not the last time.'])
# f.close()

# f=open('fishfish.txt','r+')#即读取又写入
# for back in f:
#     print(back)
# #此时文档指针在最后一个文档内容里的字符上
# print(f.read())#由于指针位置读取内容为空，读取从指针开始
#
# f.seek(0)#指针返回最开始
# print(f.read())
# f.write('ok')
# f.flush()#在不关闭文件的同时保存

# f=open('fishfish.txt','r+')
# f.truncate(10)#从第十个字符截取
# f.flush()


# from pathlib import Path
# print(Path.cwd())
# p=Path('G:\py\PyCharm Community Edition 2022.3.3\defunction')
# q=p/'fishfish.txt'
# print(q.cwd())
# print(p.name)
# print(q.name)
#
# import pickle
# x,y,z=1,2,3
# s='123'
# d=[1,2,3]
# g={x:1,y:2,z:3}
# with open('conversion of number systems.plk','wb') as f:
#     pickle.dump((x,y,z,s,d,g),f)
# with open('conversion of number systems.plk','rb') as h:
#     x,y,z,s,d,g=pickle.load(h)
# print(x,y,z,s,d,g,sep='\n')
# x=1
# y={x:1}
# print(y)






# try:
#     1/0
# except:
#     print('error')

# try :
#     a=1/1
#     print(a)
# except:
#     print('error')
# else:
#     print('ok')

# try:
#     a=1/0# f=open('fish.txt','w')
#     print(a)#f.write('ok')
# except:
#     print('error')
# else:
#     print('ok')
# finally:
#     print('test closure')#f.close()

# try:
#     while True:
#         pass
# finally:
#     print('test closure')
# try:
#     try:
#         1/0
#     except:
#         print('内部')
#     1/0
# except:
#     print('外部')

# raise ValueError('数值错误')
# c='fish'
# assert c != 'fish'

# class C:
#     def hello(self):
#         print('ok')
# c=C()
# c.hello()

# class A:
#     x=300
#     def hello(self):
#         print('A')
#
# class B:
#     x=500
#     y=100
#     def hello(self):
#         print('B')
# # b=B()
# # b.hello()
# # print(isinstance(b,B))
# # print(issubclass(B,A))
# class C(A,B):
#     pass
# c=C()
# print(c.x)
# print(c.y)
# c.hello()

# class A:
#     def say(self):
#         print('A')
# class B:
#     def say(self):
#         print('B')
# class C:
#     def say(self):
#         print('C')
# class D:
#     a=A()
#     b=B()
#     c=C()
#     def say(self):
#         self.a.say()#self为实例对象本身，该例子就是d
#         self.b.say()
#         self.c.say()
# d=D()
# d.say()

# class C:
#     x=100
#     def _self(self,v):
#         x=v
#     def a_self(self):
#         print(self)
#     def set_x(self,v):
#         self.x=v
#
# c=C()
# print(c.x)
# print(C.x)
# print(c._self(200))
# print(c.__dict__)
# print(C.__dict__)
# c.a_self()
# C.a_self(c)
# c.set_x(300)
# print(c.__dict__)

# class C:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def add(self):
#         return self.x+self.y
#     def mul(self):
#         return self.x * self.y
# class D(C):
#     def __init__(self,x,y,z):#如果子类不写构造函数即__init__则自动继承父类函数
#         C.__init__(self,x,y)
#         self.z=z
#     def add(self):
#         return C.add(self)+self.z
#     def mul(self):
#         return C.mul(self)*self.z
# d=D(2,2,3)
# print(d.add())
# print(d.mul())
# print(d.__dict__)

# c=C(1,2)
# print(c.add())
# print(c.__dict__)
# print(c.mul())

# class E(C):
#     def div(self):
#         return C.add(self)/2
# e=E(2,3)
# print(e.div())

# class A:
#     def __init__(self):
#         print('A')
# class B1(A):
#     def __init__(self):
#         A.__init__(self)
#         print('B1')
# class B2(A):
#     def __init__(self):
#         A.__init__(self)
#         print('B2')
# class C(B1,B2):#引起钻石继承问题，即A父类的内容被执行两遍
#     def __init__(self):
#         B1.__init__(self)
#         B2.__init__(self)
#         print('C')
# c=C()#c=C()本身是执行init构造函数命令

# class B1(A):#super解决钻石继承问题
#     def __init__(self):
#         super().__init__()
#         print('B1')
# class B2(A):
#     def __init__(self):
#         super().__init__()
#         print('B2')
#
# class C(B1,B2):
#     def __init__(self):
#         super().__init__()
#         print('C')
# c=C()# 此例子可看出 super 的查询范围是从B1，B2 再到父级A 最后以倒叙的形式打印 类似递归 即为MRO顺序
# print(C.mro())
# print(B2.mro())
# print(C.__mro__)

# class polygon:
#     def __init__(self,name):
#         self.name=name
#     def area(self):
#         pass
# class square(polygon):
#     def __init__(self,side):
#         super().__init__('square')
#         self.side=side
#     def area(self):
#         print(self.side*self.side)
# class circle(polygon):
#     def __init__(self,radius):
#         super().__init__('circle')
#         self.radius=radius
#     def area(self):
#         print(3.14*self.radius*self.radius)
# class triangle(polygon):
#     def __init__(self,bottom,side):
#         super().__init__('triangle')
#         self.bottom=bottom
#         self.side=side
#     def area(self):
#         print(0.5*self.bottom*self.side)
#
# class artificial_intelligence:
#     def __init__(self,name):
#         self.name=name
#     def intro(self):
#         print(f'i am {self.name} ')
# class quark:
#     def __init__(self,name):
#         self.name=name
#     def intro(self):
#         print(f'{self.name},glad to see you')
# s=square(3)
# c=circle(4)
# t=triangle(3,4)
# s.area()
# c.area()
# t.area()
# def name(x):
#     x.intro()
# a=artificial_intelligence('ai')
# q=quark('quark')
# name(a)
# name(q)

# class C:
#     def __init__(self,x):
#         self.__x=x
#     def set_x(self,x):
#         self.__x=x
#     def get_x(self):
#         print(self.__x)
# c=C(200)
# c.get_x()
# print(c._C__x)
# C.get_x(c)
# print(c.__dict__)

# class D:
#     def __init__(self,x):#单个下滑线为约定俗称的内部变量 单个下划线结尾以区别内置函数
#         self.x=x
#     def __fun(self):
#         print(self.x)
# d=D(2)
# d._D__fun()
# #d._D__init__() 这个运行不了

# class C:
#     def __init__(self,x):
#         self.x=x
# c=C(200)
# print(c.__dict__)
# c.__dict__['y']=100
# print(c.__dict__)
# c.z=50
# print(c.__dict__)#可以看出类属性通过字典存放，但字典占用内存，如果类属性不再更改，可使用其他方法创造类

# class D:
#     __slots__=['x','y']
#     def __init__(self,x):
#         self.x=x
# d=D(100)
# d.y=50
# #d.z=10#该语句无法执行
# #print(d.__dict__)#此时就没有字典里哦 空间被节省了

# class E(D):
#     pass
# e=E(100)
# e.y=150
# e.z=200
# print(e.y,e.z)
# print(e.__slots__)
# print(e.__dict__)

# class C:
#     def __init__(self,name,func):
#         self.name=name
#         self.func=func
#     def __del__(self):
#         self.func(self)
# def outter():
#     x=0
#     def inner(y=None):
#         nonlocal x  #在第二次调用inner函数 即g=f（）时 x默认为上一次调用时的数值 即为 self
#         if y:
#             x=y
#         else :
#
#           return x
#     return inner
# f=outter()
# c=C('test',f)
# print(c.name)
# del c
# g=f()
# print(g.name)


# def outter():
#     x=0
#     def inner(y=None):
#         nonlocal x  #在第二次调用inner函数 即g=f（）时 x默认为上一次调用时的数值 即为 self
#         if y:
#             x=y
#             print(x,1)
#         else:
#             print(x)
#
#     return inner
# class C:
#     def __init__(self,f):
#         self.f=f
#     def kk(self):
#         self.f(self)


# class C:
#    def __init__(self, x):
#            self.x = x
#            print(self.x)
#    def get(self):
#        print('3')
# c=C()
# c=C.__init__(c,1)

# import time
# import hashlib
#
# class Member:
#     def __init__(self,cardid,name,passwd,scores,regdate):
#         self.cardid=cardid
#         self.name=name
#         self.passwd=passwd
#         self.scores=scores
#         self.regdate=regdate
# class PasswdMixin:
#     def is_tooshort(self,passwd,require=6):
#         while len(passwd)<require:
#             passwd=input('会员密码不能小于6位请重新输入：')
#
#         return passwd
#
#     def to_md5(self,passwd):
#
#         bstr=bytes(passwd,'utf-8')#bstr=hashlib.md5()
#         passwd=hashlib.md5(bstr).hexdigest()#bstr.updata(passwd.encode('utf-8'))
#
#         return passwd                        #return bstr.hexdigest()
#
# class LoggerMixin:
#     def log(self,message,file_name='Supermarket member user information.txt'):
#         with open(file_name,'a') as f:
#             f.write(message)
# class Manage( PasswdMixin,LoggerMixin):
#     def __init__(self):
#         self.members = {}
#         self.cardid = 10000
#     def welcome(self):
#         ins=0
#         print('欢迎使用超市会员管理系统')
#         while ins!=5:
#          ins=input("\n1.创建新卡;2.修改密码;3.商品支付;4.积分查询;5.退出程序：")
#
#          if ins=='1':
#              self.ceate_member()
#          if ins=='2':
#              self.modify_passwd()
#          if ins=='3':
#              self.pay_money()
#          if ins=='4':
#              self.view_scores()
#          if ins=='5':
#              print('感谢使用超市会员管理系统')
#              break
#
#     def confirm_passwd(self):
#         cardid=int(input('请输入卡号：'))
#         while not self.members.get(cardid):
#             cardid=input('卡号不存在，请重新输入：')
#         passwd=input('请输入密码：')
#         passwd=self.to_md5(passwd)
#         while not self.members.get(cardid).passwd==passwd:
#             passwd=input('密码错误，请重新输入密码：')
#
#         return cardid
#     def ceate_member(self):
#         name=input('请输入姓名：')
#         passwd=input('请输入密码:')
#         passwd=self.is_tooshort(passwd)
#         passwd=self.to_md5(passwd)
#         scores=0
#         regdate=time.localtime()
#         member=Member(self.cardid,name,passwd,scores,regdate)
#         self.members[self.cardid]=member
#         print(f'创建成功，卡号->{self.cardid},关联用户->{name}')
#         self.log(f"开卡成功：{self.cardid} -> {name}，时间：{time.strftime('%Y-%m-%d %H:%M:%S', regdate)}\n")
#         self.cardid+=1
#     def modify_passwd(self):
#        cardid= self.confirm_passwd()
#        newpasswd=input('请输入新的密码：')
#        newpasswd=self.is_tooshort(newpasswd)
#        newpasswd =self.to_md5(newpasswd)
#        self.members[cardid].passwd=newpasswd
#        self.log( f"修改密码:卡号->{cardid},时间: {time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())}\n")
#        print('密码修改成功')
#     def pay_money(self):
#        cardid=self.confirm_passwd()
#        money=int(input('请输入支付金额:'))
#        self.members[cardid].scores+=money
#        self.log(f"积分累计:卡号->{cardid},+{money}分,时间:{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())}\n")
#        print('支付完毕')
#     def view_scores(self):
#         cardid = self.confirm_passwd()
#         print(f"卡号{cardid},当前消费积分:{self.members[cardid].scores}")
#         self.log(f"积分查询:卡号->{cardid},{self.members[cardid].scores}分,时间:{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")
# def main():
#     m=Manage()
#     m.welcome()

# a={}
# a[1]=100

# class S1(str):
#     def __add__(self,other):#add函数的魔法方法，寓意为在执行str的add方法前打断 并输出新的函数。
#         return len(self)+len(other)
# s=S('ok')
# s2=S('y')
# print(s+s2)#s.__add__(s2)
#
# # class S(str):
# #     def __add__(self,other):
# #         return NotImplemented
# class S2(str):
#     def __radd__(self,other):#调用条件为两者基于不同的类
#         return len(self)+len(other)
# #
# # s=S('ok')
# # s2=S2('yy')
# # print('python'+s2)
# # print(s+s2)
#
# class S3(str):
#     def __iadd__(self,other):
#         return len(self)+len(other)
# s1=S3('pk')
# s2=S1('ok')
# s1+=s2
# print(s1)

# print(2&3,3&4,5|6,7|8,~2,~3,2^3,4^5,sep='  ')
# if 8>>2==8//pow(2,2):#移位会使数字丢失 所以是地板除
#     print('1')
# import math
# print(3.1+0.2)
# if 0.1+0.2==0.3:
#     print('y')
# else:
#     print('n')
# print(math.ulp(0.3))
# print(math.ulp(1.3))
# print(math.ulp(2.3))
# print(math.ulp(3.3))
# print(math.ulp(4.3))
# print(math.ulp(5.3))
# print(math.ulp(6.3),end='\n')
# for i in range(10):
#     print(i,math.ulp(i+0.3))

# class C:
#     def __index__(self):#有某变量所有该对象触发
#         print('n')
#         return 4
# c=C()
# s='abcde'
# print(s[c])

# class C:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
# c=C('test',20)
# print(getattr(c,'name'))#_attr()命令也具备魔法方法
# print(setattr(c,'name','test1'))#无返回值
# print(delattr(c,'name'))
# print(hasattr(c,'name'))
# print(getattr(c,'_C__age'))
# print(setattr(c,'_C__age',21))
# print(getattr(c,'_C__age'))
# print(delattr(c,'_C__age'))
# print(hasattr(c,'_C__age'))


# class C:#其父类为object
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def __getattribute__(self,attrname):#getattr()的魔法命令
#         print('get1')
#         return super().__getattribute__(attrname)
#     def test(self):
#         print('ok')
#     def __getattr__(self,attrname):
#         if attrname=='none':
#             print('yes')
#         else :
#             raise AttributeError(x)
#
# c=C('test',10)
# #c.__getattribute__('name') /C.__getattribute__(c,'name')/getattr(c,'name')
# c.none#只要访问属性 就会被拦截 但不存在的属性才会被__getattr__拦截

# class D:
#     def __setattr__(self,name,value):#一旦发现赋值操作就拦截
#         self.name=value#错误写法，由于该操作也是个赋值操作，会导致赋值时无限递归
# class D:
#     def __setattr__(self,name,value):
#         self.__dict__[name]=value
#     def __delattr__(self,name):
#         del self.__dict__[name]
# d=D()
# d.name='test'
# print(d.name)
# del d.name
# print(d.__dict__)




# import hashlib
# class Member:
#     def __init__(self,cardid,name,passwd,money,):
#         self.cardid=cardid
#         self.name=name
#         self.passwd=passwd
#         self.money=money
# class PasswdMixin:
#     def is_valid(self,passwd):
#         while len(passwd)!=6:
#             passwd=input('密码必须是六位。请重新输入：')
#         return passwd
#     def to_md5(self,passwd):
#         bstr=hashlib.md5()
#         bstr.update(passwd.encode('utf-8'))
#
#         return bstr.hexdigest()
# class MoneyMixin:
#     def is_positive(self,money):
#          while float(money)<0:
#
#             money=input('金额必须为正数：')
#
#          return money
# class UserManager(PasswdMixin,MoneyMixin):
#     def __init__(self):
#         self.members={}
#         self.cardid=88888888
#     def check_account(self):
#         cardid=input("请输入卡号：")
#         cardid=self.is_integer(cardid)
#         while not self.members.get(int(cardid)):
#             cardid=input('卡号不存在请重新输入')
#         passwd = input('请输入密码：')
#         passwd = self.is_valid(passwd)
#         passwd = self.to_md5(passwd)
#         while not self.members.get(int(cardid)).passwd==passwd:
#             passwd = input('密码错误请重新输入')
#         return cardid
#     def is_integer(self,cardid):
#         while not cardid.isdecimal():
#             cardid=input('卡号必须为正整数：')
#         return cardid
#     def create_account(self):
#         name=input('请输入姓名：')
#         passwd=input('请输入密码：')
#         passwd=self.is_valid(passwd)
#         passwd=self.to_md5(passwd)
#         money=input('请输入预存金额：')
#         money=self.is_positive(money)
#         member=Member(self.cardid,name,passwd,money)
#         self.members[self.cardid]=member
#         print(f'创建成功，卡号为{self.cardid}')
#         self.cardid+=1
#     def delete_account(self):
#         cardid=self.check_account()
#         a=input('确认删除该账号吗Y/N: ')
#         if a=='Y':
#             self.members.pop(int(cardid))
#         else:
#               main()
#     def get_account(self,cardid):
#         return self.members[cardid]
#
# class welcome(UserManager):
#     def welcome1(self):
#         ins=0
#         while ins!=5:
#          ins=input("\n1.创建新卡;2.修改密码;3.商品支付;4.积分查询;5.退出程序：")
#          if ins=='1':
#              self.create_account()
#          if ins=='2':
#              self.delete_account()
#          if ins=='3':
#              break
#          if ins=='4':
#              break
#          if ins=='5':
#              break
#
# def main():
#         w = welcome()
#         w.welcome1()
#
# main()
# class Account(PasswdMixin):






# class Iterator:#创建一个迭代器对象
#     def __init__(self):
#         self.counter=0
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.counter+=1
#         if self.counter==3:
#             raise StopIteration()#此为抛出一个错误
#         return self.counter
# class Iterable:#创建一个可迭代对象
#
#     def __iter__(self):
#         return Iterator()
# i=Iterable()#可迭代对象,for循环促使可迭代对象内含__iter__方法并返回一个迭代器对象 此迭代器对象实施next方法。
# for a in i:
#     print('test')

# class C(object):
#    def __init__(self,test):
#        print(1)
#        self.test=test
#    def __new__(cls, *args, **kwargs):
#        print(2)
#        v1=super().__new__(cls)
#        print(v1)
#        return v1
# c=C(1)
# print(c)

# class C:
#     list_display=[]#定义了一个类变量，类变量只属于类，在实例化对象时对象内不包含类变量。
#     def get_list_display(self):
#         self.list_display.insert(0,10)
#         return self.list_display
# c=C()#此时对象内部为空
# a=c.get_list_display()#由于对象内啥也没有 ，所以寻找类中的方法，方法内有一个。而list_display 对象中也没有此变量，
# # 故仍然在类中寻找，最后完成插入，
# # 插入操作不会更改原来变量存储的地址，赋值会改变。
# print(a)
# print(C.list_display)


# class MyDecriptor:#描述符号类的制作，需要两个类，下面的类需要调用上面类并作为自己的一个变量
#     def __get__(self, instance, owner):
#         print(self,instance,owner)
#     def __set__(self, instance, value):
#         print(self,instance,value)
#     def __delete__(self, instance):
#         print(self,instance)
# class Test:#描述器的拥有者
#     x=MyDecriptor()
#
# test=Test()
# test.x
# test.x=1
# del test.x#<__main__.MyDecriptor object at 0x000001FE3FCF3FD0> <__main__.Test object at 0x000001FE3FCF3FA0> <class '__main__.Test'>
# # <__main__.MyDecriptor object at 0x000001FE3FCF3FD0> <__main__.Test object at 0x000001FE3FCF3FA0> 1
# # <__main__.MyDecriptor object at 0x000001FE3FCF3FD0> <__main__.Test object at 0x000001FE3FCF3FA0>

# class Myproperty:
#     def __init__(self,fget=None,fset=None,fdel=None):
#         self.fget=fget#注意此例子中的fget是一个函数作为了属性
#         self.fset=fset
#         self.fdel=fdel
#     def __get__(self, instance, owner):
#         return self.fget(instance)
#     def __set__(self, instance, value):
#         self.fset(instance,value)
#     def __delete__(self, instance):
#         self.fdel(instance)
# class C:
#     def __init__(self):
#         self._x=None
#     def getX(self):
#         return self._x
#     def setX(self,value):
#         self._x=value
#     def delX(self):
#         del self._x
#     a=Myproperty(getX,setX,delX)# 此处可以看出将三个函数传给了 property类作为对象的三个初始化属性
# c=C()
# c.a=1#此处调用a属性 相当于调用property类 赋值操作被类的__set__方法拦截 其中instance参数就是c本身，value为1 （get set delete 出现则类为描述符类，且在其他类对象调用时拦截）
# # __set__函数中 的fset方法相当于  setX（）方法 故就是在运行 setX（instance，value）这个函数
# print(c._x)

# class E:
#     def __init__(self):
#         self._x=250
#     @property# x=property(x)
#     def x(self):
#         return self._x
#     @x.setter
#     def x(self,value):
#         self._x=value
#     @x.deleter
#     def x(self):
#         del self._x
# e=E()
# print(e.x)
# e.x=520
# print(e.__dict__)
# del e.x
# print(e.__dict__)

 # class property:
#
#  def __init__(self, fget=None, fset=None, fdel=None, doc=None):
#          self.fget=fget# self.fget=getx
#  def __get__ (self,instance,owner):
#      return self.fget(instance) #self.fget = getx  get(instance)
#  def __call__(self,)

#
#
#
#
# class C(object):
#     def getx(self): return self._x
#
#     def setx(self, value): self._x = value
#
#     def delx(self): del self._x
#
#     x= property(getx, setx, delx, "I'm the 'x' property.")
#
# c=C()
# c.x
#
#
#
# class C(object):
#     @property #  x=property(x)
#     def x(self):
#         "I am the 'x' property."
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         self._x = value
#
#     @x.deleter
#     def x(self):
#         del self._x
# # (copied from class doc)

# class C:
#     def __init__(self,fget):
#         self.fget=fget
#     def __get__(self, instance, owner):
#         return self.fget(instance)
#
# class D:
#     x=1
#     def __init__(self):
#         self.x=1
#     def getx(self):
#         return self.x
#     c=C(getx)
#
# d=D()
# d.c

#
# def outer(openation):
#     def inner():
#         x()
#
#     return inner
#
# @outer   #x=outer(x)  x= inner
# def x():
#     print('1')
#
# x()



#1.闭包和装饰器//////////////////////////////////////////////////////////////////////////////////
# def func():
#     print('正在执行func功能')
#     value=(1,2,3,4)
#     return value
# def outer(orgain):
#     def inner():#在闭包时 每一次调用 都会形成一个包空间，内含一个变量 orgain 可以是函数。
#         # 返回 inner 给一个变量，使其变成inner函数 在inner函数中，orgain参数则为保留在包空间的那个变量.
#         # 直到下一次outer函数调用形成一个新的包。
#         print('before')
#         res=orgain()
#         print('after')
#         return res
#     return inner
# func=outer(func)
# result=func()
# print(result)

#2.装饰器改写//////////////////////////////////////////////////////////////////////////////////
# def outer(orgain):
#     def inner():
#         print('before')
#         res=orgain()
#         print('after')
#         return res
#     return inner
# @outer# 此语句相当于 outer（func）执行后并将返回值给func 装饰器，
# 其本质意义在于并不更改func函数的同时 在其中添加剂一些功能，使其不至于失去函数本身的命名意义，方便且优雅，维护也更加方便
# def func():
#     print('正在执行func功能')
#     value=(1,2,3,4)
#     return value
# result=func()#此语句相当于在执行inner
# print(result)

#3.带参函数的装饰器//////////////////////////////////////////////////////////////////////////////////
# def outer(orgain):
#      def inner(*args,**kwargs):#针对带参数的func，最后执行的func1（） 实际上是在执行inner 所以要在inner上加全类型的参数设置
#          #该参数同时适用于 闭包内含的已经保存的参数或函数，此例子为orgain。
#          print('before')
#          res=orgain(*args,**kwargs)
#          return res
#      return inner
# @outer
# def func1(a1):
#     print(f'程序执行中{a1}')
#     value = (1, 2, 3, 4)
#     return value
# @outer
# def func2(a1,a2):
#     print(f"程序执行中{a1},{a2}")
#     value = (1, 2, 3, 5)
#     return value
# func1(1)
# func2(2,a2=10)

#4.如何创造一个类装饰器//////////////////////////////////////////////////////////////////////////////////
# class C:
#     def __init__(self,char):
#         self.char=char
#     def __call__(self,func):
#         def inner():#一个普通的装饰器内函数 ，call 魔法方法充当 外函数
#             print(self.char)
#             res=func()
#             return res
#
#         return inner

# @C('before') #C（）=c ，相当于c即为一个可执行的对象，(一般放在@符号后都是可执行的函数，而这会放的时可执行的一个对象，这个对象加(),才开始是执行了，C()()=c())
# # 对象加()会被call方法拦截。call方法的拦截出发条件 即为小c（），其中小c=C（）
# def func():
#     print("hello,world")
# func()# 及完成inner方法调用


#5.迭代器对象与可迭代对象//////////////////////////////////////////////////////////////////////////////////
# class Iterator:#创建一个迭代器对象
#     def __init__(self):
#         self.counter=0
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.counter+=1
#         if self.counter==3:
#             raise StopIteration()#此为抛出一个错误
#         return self.counter
# class Iterable:#创建一个可迭代对象
#
#     def __iter__(self):
#         return Iterator()
# i=Iterable()#可迭代对象,for循环促使可迭代对象内含__iter__方法并返回一个迭代器对象 此迭代器对象实施next方法。
# for a in i:
#     print('test')


#6.函数参数传递默认为转递内存地址//////////////////////////////////////////////////////////////////////////////
# import copy
# def func(data):#要求函数内部 不应该出现重新赋予内存地址的操作 如data=[5,6,7]
#     data.append(4)#data[1]=3
# data_list=[1,2,3]
# func(data_list)#data_list  的内存地址作为参数传递给了func 在func内对参数的操作会影响data_list
# print(data_list)#要求data_list 是可变类型 list dict set 等
# new_list=copy.deepcopy(data_list)#如果不想更改data_list的内容 需要深拷贝一份 内存地址不一样的数据
# func(new_list)
# print(data_list)
#
# def func1():
#     data=[1,2,3]
#     return data
# v=func1()#函数返回值也是内存地址，先生成， 给v后 函数内data就会被释放，指向生成的内存地址的变量就只剩下v了 ，
# # 如果data 是字符串或int等类型 则在内容相同时，任何变量都指向同一内存地址。
# v1=func1()

#7.类变量////////////////////////////////////////////////////////////////////////////////////////////
# class C:#本例子如果有继承自C的子类 子类pass
#     list_display=[]#定义了一个类变量，类变量只属于类，在实例化对象时对象内不包含类变量。
#     def get_list_display(self):
#         self.list_display.insert(0,10)
#         return self.list_display
# c=C()#此时对象内部为空
# a=c.get_list_display()#由于对象内啥也没有 ，所以寻找类中的方法，方法内有一个。而list_display 对象中也没有此变量，
# # 故仍然在类中寻找，最后完成插入，
# # 插入操作不会更改原来变量存储的地址，赋值会改变。
# print(a)
# print(C.list_display)
#class D(C):
   #pass
# D.list_display=10 #该操作类似于c的对象赋值操作，不会影响父类的类变量，只会在子类新创建一个同名的

#8.静态方法/////////////////////////////////////////////////////////////////////////////////////////////
# class Foo:
#     def __init__(self):
#         self.name='test'
#     def  tes(self):
#         print(self)
#     @staticmethod#静态方法定义装饰器，作为静态方法f（）可以传入任何参数或不传入，适用于函数执行过程中不需要 实例变量参与的情况。
#     def f():
#         print('1')
# Foo.f()#同时静态方法支持无对象，类执行 比较便捷 也可以通过对象调用但不建议
#这里有个小彩蛋 如果实例化对象f 使用Foo.tes(f)方法也可以调用 绑定方法  有点类似于需要传入对象作为参数的静态方法

#9.类方法//////////////////////////////////////////////////////////////////////////////////////////
# class Foo:
#     def __init__(self):
#         self.name='test'
#     def  tes(self):
#         print(self)
#     @staticmethod#将静态方法的参数设置为f（x）
#     def f(x,a):
#         print(x,a)
#     @classmethod#类方法调用类似于静态方法，其函数有一个cls参数 就是 类本身，并且不需要在调用时输入
#     def f1(cls,a):#在函数内部就可以将cls作一系列操作
#         print(cls,a)
# Foo.f1(1)#同样支持对象调用 ，并并不推荐
# Foo.f(Foo,1)#在调用静态方法时 选择参数为Foo即类本事 也可以完成类方法相同的操作

#10.

# ip='192.168.12.79'
# ip_list=ip.split('.')
# res=[]
# count=0
# for i in ip_list:
#     res.append(bin(int(i)))
# l=max(res,key=len)
# for i in res:
#     i=i[2:]
#     if len(i)<len(l)-2:
#         i=i.rjust(len(l)-2,'0')
#     res[count]=i
#     count+=1
# a=''
# for i in res:
#     a=a+i
# print(int(a,base=2))
# class C(object):
#    def __init__(self,test):
#        print(1)
#        self.test=test
#    def __new__(cls, *args, **kwargs):
#        print(2)
#        v1=super().__new__(cls)
#        print(v1)
#        return super().__new__(cls)
# c=C(1)
# print(c)

# class Parent():
#     x=1
# class children1(Parent):
#     pass
# class children2(Parent):
#     pass
#
# class children3(children1,children2):
#     pass
# print(children3.x)
# children2.x=2
# print(children3.x)
# children1.x=3
# children2.x=4
# print(children3.x) # 左至右原则 优先第一层父类查询
# print(children3.mro())
# class C:
#     def login(self):
#
#         return "ok"
#     def __call__(self, *args, **kwargs):
#
#        res= getattr(self,"login")()
#
#        print(res)
# c=C()
# c()
# res=getattr(c,"login")
# print(res)







# import matplotlib as mpl
# # import matplotlib.pyplot as plt
# import numpy as np
# import scipy
# t=np.linspace(0,1,1000)
# f=10
# y=np.sin(2*np.pi*t*f)
# y_fft=np.fft.fft(y)
# y_fft_abs=np.abs(y_fft)
# freqs=np.fft.fftfreq(len(y),t[1]-t[0])
# plt.subplot(121),plt.plot(t,y)
# plt.subplot(122),plt.plot(freqs,y_fft_abs)
# plt.show()
#
# import scipy.io.wavfile as wav    #读取信号模块
# import matplotlib.pyplot as plt    #画图模块
#
# rt, wavsignal = wav.read(r"D:\Documents\录音\录音1.wav")  # 读取信号
# print("sampling rate = {} Hz, length = {} samples, channels = {}, dtype = {}".format(rt, *wavsignal.shape, wavsignal.dtype))  #输出信号
# # fg=plt.figure(1)  #画图
# # plt.plot(wavsignal)  #画图
# # plt.show()  #显示图形

# # print(wavsignal.shape)
# a=[("1","2"),("3","4")]
#
# a["1"]
class Z():
    def __init__(self):
        self.a=1
class X(Z):
    def __init__(self):
        self.b=2
        super().__init__(self.b)
x=X()
print(x.__dict__)