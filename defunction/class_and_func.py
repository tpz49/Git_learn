#1.闭包和装饰器///////////////////////////////////////////////////////////////////////////////////////////////////////////
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
import os

#2.装饰器改写/////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

#3.带参函数的装饰器/////////////////////////////////////////////////////////////////////////////////////////////////////////
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

#4.如何创造一个类装饰器/////////////////////////////////////////////////////////////////////////////////////////////////////
# class C:
#     def __init__(self,char):
#         self.char=char
#     def __call__(self,f):
#         def inner():#一个普通的装饰器内函数 ，call 魔法方法充当 外函数
#             print(self.char)
#             res=f()
#             return res
#         return inner
#
# @C('before') #C（）相当于c即为一个可执行的对象 而call方法的拦截出发条件 即为 c=C（） 后 c（）
# def func():
#     print("hello,world")
# func()# 及完成inner方法调用

#4.1 call的应用\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# from wsgiref.simple_server import make_server
#
#
# class Foo:
#     def login(self):#根据用户输入不同url显示不同模块
#         return "测试用的登录"
#
#     def __call__(self,environ,start_response):
#         start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
#
#         method_name=environ.get("PATH_INFO").strip("/")#environ字典中的"PATH_INFO“根据用户输入的url
#         # 返回最后一项并加一个/，这里的strip方法是为了去除/,得到一个字符串
#         if not hasattr(self,method_name):#如果用户随便输入，或者method_name包含的第二个参数，favicon.ico被接收
#             return ["输入的网址不存在，请重新输入".encode("utf-8")]
#
#         respose=getattr(self,method_name)()#这里注意要执行，当用户在url最后一项输入login时 method_name接受这个字符串，并给getattr参数
#
#         return [respose.encode("utf-8")]
# serve=make_server(" 192.168.0.3",8000,Foo())#可以自动执行第三个参数 即给第三个参数加()
# serve.serve_forever()




#5.迭代器对象与可迭代对象////////////////////////////////////////////////////////////////////////////////////////////////////
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


#6.函数参数传递默认为转递内存地址/////////////////////////////////////////////////////////////////////////////////////////////
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

#7.类变量////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

#8.静态方法///////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

#9.类方法////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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


#10.property的另一种解释-->属性////////////////////////////////////////////////////////////////////////////////////////////
# class page_split:#以一个分页应用举例，当321个产品展示在页面中，每页显示10个商品，当顾客需要第几页时，显示对应的十个商品
#     def __init__(self,total_page,current_page,per_page=10):
#         self.total_page=total_page
#         self.current_page=current_page
#         self.per_page=per_page
#     @property
#     def start_index(self):
#         return (self.current_page-1)*self.per_page
#     @property#end_index=property(end_index)
#     def end_index(self):
#         return self.current_page*self.per_page
#     # end_index=property(end_index) 运用该行代码也可以运行，但是只能有一个参数，因为第二个参数是在赋值时拦截，即 p.end_index=1 这种命令时
#另外一个注意的事情描述符只能在类属性上，把他放在某个绑定方法里做实例属性是不行的
# current_page=int(input("请输入当前页："))
# p=page_split(321,current_page)
# list=[]
# for i in range(321):
#     list.append("alex-%s"%(i,))
# data_list=list[p.start_index:p.end_index]#由于@property p.start_index相当于在调用属性（在原本的property例子中即为调用类变量）故不用加（）
# print(data_list)

#11.成员修饰符\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class C:
#     __a=2
#     def __init__(self):
#         self.__x=1
#     def get_xand_a(self):
#         print(self.__x,C.__a)
# class D(C):
#      def get_xand_a(self):
#          print(self.__x,C.__a)
#
# c=C()
# # print(c.__x,C.__a)#私有类与实例变量 无法从外部访问
# c.get_xand_a()#但是可以调用函数，函数即是在类的内部访问
# d=D()
# # d.get_xand_a()#同时也可以在子类的内部访问
# print(c._C__x)#外部强制访问

#12.sys模块 解释器相关数据获取\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# import os
# import  sys
# a=[1,2,3]
# b=a
# print(sys.getrefcount(a))#同一个地址有多少变量指向 ，函数调用时 会有变量赋值操作 类似于 b=a 所以也是一次指向

# c=sys.getrecursionlimit()#得到python允许的最大递归次数 1000


# sys.stdout.write('你好')#print的底层代码 但打印第二个字符的时候不会自动换行
# sys.stdout.write('hello')
# sys.stdout.write(1,2,3)#同时无法打印int list dict 只能打印字符串

#sys.argv 参见 脚本 Module deletion.py

# for i in sys.path:
#    print(i)
# print(sys.path)#查询可以import的模块的位置被允许存放的目录 ////
# # sys.path.append(r"G:\\")#强硬添加一个模块查找位置
# # #当需要添加一个模块查找位置时
# # BISE_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#逐步解析，最内层为查询目前.py文件的绝对路径，下一层为找到放他的文件夹bin，
# # #实际情况时没有这个文件夹的，本例子是用来 当.py文件在一个文件夹内，调用的模块在另一个文件夹的情况，最后一层为 defunction文件夹目录。
# # sys.path.append(BISE_dir)#将该目录强硬的加入，就可以from test import text.py



#13.os模块应用 操作系统相关数据获取，对比pathlib中的path模块\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import os
# import time
#在print中\n表示换行，\r表示回到（）内初始位置，\t表示制表符tab
# print("你好\r",end="")
# print("123",end="")

# os.path.exists()#判断路径是否存在
# os.stat("a.mp4").st_size#获取我呢见大小，字节数
# path=os.path.abspath("a.mp4")#G:\pycharm\PyCharm Community Edition 2022.3.3\defunction\a.mp4 获取绝对路径
# print(path)#可以在不同的包中调用绝对路径命令 来获取任意文件的绝对路径 ，更方便挎包使用。
# path=r"a.mp4"
# os.path.dirname(path)#获取对象上级目录

#windows默认使用\为路径分隔符 在python中\为转义符，所以应当 \\ 取消转义 以防止 路径为 \n.1mp4 而\n被当成换行
#当然也可以 r“\n,\t,\n”字符串前加r就可以自动转义

# path1="a.mp4"
# path2="G:\pycharm\PyCharm Community Edition 2022.3.3\defunction"
# res=os.path.join(path2,path1)#根据目前操作系统的路径表达方式拼接多个路径
# print(res)

# res=os.listdir(path2)#该路径下所有子文件
# print(res)

#直接在该目录下创建文件夹
# file_path=r"test\test1.txt"
# file_dir=os.path.dirname(file_path)
# if not os.path.exists(file_dir):
#     os.makedirs(file_dir)
# with open(file_path,'w',encoding='utf-8') as f:
#     f.write("这是os模块测试创建文件夹用")

# os.rename("test","test_rename")#重命名文件夹

#os模块查看一个文件夹大小
# sum_size=0
# res=os.walk(r"G:\pycharm\PyCharm Community Edition 2022.3.3\defunction")#walk返回一个生成器对象 只能通过 迭代来 输出，输出结果为元组，元组第一项
# #为[文件夹路径]，以及[子文件夹]和单独.txt文件等
# for path_name,dir_name,file_list in res:
#     for file in file_list:
#         size=os.path.getsize(os.path.join(path_name,file))
#         sum_size+=size
# print(sum_size)







#该种操作可以用来制作进度条
# for i in range(1,101):
#     print("\r%s%%"%i,end="")#在pycharm 中记得把\r放在最前面
#     time.sleep(0.1)

# file_size=os.stat("1-01 day01 计算机基础简介-1-480P 清晰-AVC.mp4").st_size#看该文件有多少字节
# print(file_size)
#
# read_size=0
# with open("1-01 day01 计算机基础简介-1-480P 清晰-AVC.mp4","rb") as f1,open("a.mp4",'wb') as f2:#with as 自动关闭 执行 f。close()
#     while read_size<file_size:
#         chunk=f1.read(1024)#每一次循环读出1024字节
#         f2.write(chunk)
#         read_size+=len(chunk)
#         print("\r%s%%"%int(read_size/file_size*100),end="")#end很重要 end为空意味着不换行，这样\r才能定位


#
# os.makedirs("data")
# data_files=os.path.join("data","hourse_tiny.cvs")
# with open(data_files,"w") as f:
#     f.write("Numroom,Alley,Price\n")
#     f.write("NA,Prive,12750\n")
#     f.write("2,Prive,106000\n")
#     f.write("4,NA,178100\n")
#     f.write("NA,NA,140000\n")

#14.描述符拦截顺序\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#数据描述符（set delete ）>实例对象属性（self.）>非数据描述符(get)>类属性(cls.)
# class C:#由于实例对象属性属于对象内部空间，而非数据描述符创建于类内，所以访问后 先显示实例对象同名属性
#     def __get__(self,instance,owenr):
#         print("get")
# class D:
#     x=C()
# d=D()
# # d.x#d.x 被拦截
# d.x=1#给对象属性
# d.x#此时不会被拦截

# class C:
#     def __get__(self, instance, owenr):
#         print("get")
#     def __set__(self, instance, value):
#         print("set")
# class D:
#     x=C()
# d=D()
# d.x
# d.x=1#该赋值被拦截 d 的dict里无x属性
# d.x
# d.__dict__['x']=1#强制添加属性
# d.x#即便时dict里已经有了也不能访问

# class D:
#     x=C()
#     def __getattribute__(self, item):
#         print("attr")
# d=D()
# d.x#在一个类中内置的getattribute 定义了四种属性的顺序，所以在索引方面其顺序最高。


# class C:
#     # def __init__(self,name):
#     #     self.name=name
#     def __set_name__(self, owner, name):#可以拦截，在get和set之前命名
#         self.name=name
#     # def __get__(self, instance, owenr):
#     #     print("get")
#     #     return instance.__dict__.get(self.name) #拦截后 在d对象的字典里直接操作
#     def __set__(self, instance, value):
#         print("set")
#         instance.__dict__[self.name]=value
# class D:
#     x=C()#将x作为属性名给 x这个C类的对象 instance代表的时D类的对象
#
#
# d=D()
#
# d.x=1# 由于在类的括号里填写 不是很美观， __set_name__魔法方法可以拦截，在get和set之前将对象d.后的名字 给对象c
# print(d.__dict__)
# print(D.x.__dict__)#隐去__get__ 可以输入此行代码 不隐去 会被拦截，可以看到，对象x是C的对象 有一个“name”：“x”键值对

#15.可变类型参数作为函数参数\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# def func(data,e=[]):
#     e.append(data)
#     return e
# v1=func(1)#v1指的是e的内存地址
# print(v1)#可以和下面对比 v1会变
# v2=func(2,[11,2])
# v3=func(3)
# v4=func(3,[11,2])
# print(v1,v2,v3,v4) # [1, 3] [11, 2, 2] [1, 3] [11, 2, 3]
# #类似于类 在func执行之前 func函数空间内包含e变量 当不赋值e时 其内存地址就相当于一个类变量,append不改变内存地址,所以e中数据会随着append增加
# #但赋值给e就会在v2 func中创建一个新内存 进而使其改变


#16.json模块 json是一个特殊字符串，python语言转成json 再由其他语言翻译 以形成交互。 在前端比较常见\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# import json
# v=[1,2,3,"c",True,{'k':1}]#未序列化的列表内的   元组将会被变成列表,集合不能序列化
# v1=json.dumps(v)#将v序列化 生成json字符串，注意 此时json是字符串
# print(v1,type(v),type(v1))
# v2='[1,2,"12"]'#json本身为一个字符串，字符串中外层为列表或字典 列表内的字符串只能是双引号
# v3=json.loads(v2)#反序列化 将其变成python格式
# print(v3,type(v2),type(v3))
# #序列化在爬虫中获取网页内容后反序列化时使用

# v=[1,{1:"该文档用于理解json的dump方法"}]
# # v1=json.dumps(v)#得到unicode编码的中文
# # print(v1)
# # v1=json.dumps(v,ensure_ascii=False)
# # print(v1)
# f=open("x.txt","w",encoding="utf-8")
# v1=json.dump(v,fp=f,ensure_ascii=False)#fp参数是一个文件对象，与dumps不同，dump可将json写入一个文件夹
# print(v1)#返回none
# f.close()

#17.反射 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class C:
#     def get(self):
#         pass
# c=C()
# c_method=getattr(c,"get")
# c_method()#实例变量与绑定方法的另类实现，内置函数getattr方法 其对应魔法方法拦截优先很高。
# a=input(":")
# getattr(c,a)()#根据传入不同字符串，执行不同方法，类似于鼠标点击即可执行命令,具体例子4.1__call__的应用
#hasattr(c,a)#判断是否由
# setattr(c,"k1",123)#设置
#delattr(obj,"k1")

#由于python内一切都是对象，getattr() 能获取任何形式数据内部存在的成员
# import test_module #如一个模块，可以查询其内部成员
# a=getattr(test_module,'num')
# print(a,type(a))
#
# b=getattr(C,"get")#又或者一个类的一个方法查找
# print(b,type(b))
#
# d=getattr(test_module,'F')#相当于test_module.F
# d.func()#d现在为test_moudle模块的一个类
#
# e=getattr(d,"bond")#绑定方法比较特殊，一般需要实例化一个对象，对对象使用getattr方法
# print(e)#此时e是一个function F.bond at 0x000001EB406C4E50，想要使用需要e（self）
# e(d())
#
# f=getattr(d(),"bond")()# f为d的另一个表达形式

#17.1反射的应用 用字符串形式导入模块的模块 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# import importlib
# path="test_module.F"
# module_name,class_name=path.rsplit(".",maxsplit=1)
#
# module_project=importlib.import_module(module_name)
# #test_module.F返回错误test不是个包，因为它是个模块，这边建议把test这个模块放在有许多py文件的文件夹内
# getattr(module_project,class_name).func()
# importlib.reload(test_module)#可重新加载这个模块**









#18.__str__  ，魔法命令\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class C:
#     def __str__(self):
#         return '123'
# c=C()
# print(c)  #str魔法方法在打印对象自身时拦截，并打印返回值
# class C:
#     def __init__(self,name,age):
#          self.name=name
#          self.age=age
#     def __str__(self):
#         return "%s %d" %(self.name,self.age)
# u_list=[C("e",18),C("a",19)]
# for item in u_list:
#     print(item)#这样打印对象的时候就可以直接打印对象的属性

#19.__dict__ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
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


#20.with上下文管理\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class Manage:
#     def __enter__(self):
#         self.x=open("wite_test","a",encoding="utf-8")
#         return self.x
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type,exc_val,exc_tb)
#         self.x.close()
# with Manage() as f:#with执行 被enter拦截 首先将打开的文件给self.x 并将该方法返回值给f ，在with方法推出时 执行 exit方法 关闭文件。
#     f.write("这是with魔法方法测试用")

#21.类型注解\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# def func(x:int):
#     print(x)
# func("l")#类型注解不强制
# class student:
#     pass
# stu:student=student()#标注该对象所属于的类
#
# my_tu:tuple[int,int,int]=(1,2,3)
# print(my_tu,type(my_tu))#可以定义一个类型，同时也定义类型内的类型, 其本质是告诉pycharm该类型究竟是什么类型
# my_lis:list[int]=[1,2,3]
#
# def fun (x:list):
#     x.append([1])
# def fun1 (x):
#     # x.???#当将x定义为list时 pycharm会给你推荐x的用法
#       pass
# import random
# x:int=random.randint(1,10)#  当你不熟悉返回值是多少时，可以注释一下
#
# def fun2(x:int)->int:#也可以对返回值进行类型注解
#     return x
# from typing import Union
# def fun4(date:Union[int,str])->Union[int,str]:#联合类型标注
#
#     pass
# my_dict:dict[str,Union[int,str]]={"name":"a","age":15}#可以进行联合类型标注

#22.字符串的格式化\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# a="name is %s,age is %s" %("tpz",18)
# print(a)
# b="name is %(name)s,age is %(age)s" %{"name":"tpz",'age':18}
# print(b)
#
# c1="tpz"
# c2=18
# c=f"name is {c1},age is {c2}"
# print(c)
#
# d="name is {0},age is {1}".format("tpz",18)#d="name is {},age is {}".format("tpz",18)
# print(d)
#
# e="name is {name},age is {age}".format(name="tpz",age=18)
# print(e)

#22.1有序字典\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# from collections import OrderedDict
# info=OrderedDict()
# info["k1"]=123
# info["k2"]=134
# for i in info:#迭代顺序严格按照字典的生成顺序，字典内部顺序不可跳动，为有序字典
#     print(i)

#23栈 后进先出\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class stack:
#     def __init__(self):
#         self.data_list=[]
#     def push(self,val):
#         self.data_list.append(val)
#     def pop(self):
#         return self.data_list.pop()
# obj=stack()
# obj.push("alex")
# obj.push("epic")
# obj.push("fishc")
# v1=obj.pop()
# print(v1)
# v2=obj.pop()
# print(v2)
# v3=obj.pop()
# print(v3)
# print(obj.data_list)

#24设计模式 --单例模式\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class Foo:#如此一来所有创造的对象都共用一个地址  /class Singleton:,一般用于数据库链接和数据库链接池
#     ins = None
#
#     def __new__(cls, *args, **kwargs):
#
#         # if Foo.ins:
#         #     return Foo.ins
#         # Foo.ins=super().__new__(cls)
#         # return Foo.ins
#         if not cls.ins:
#             cls.ins = super().__new__(cls)
#         return cls.ins
# f=Foo()
# a=Foo()
# print(f,a)
# if f==a:#内存地址时存储对象的唯一标志
#     print("y")
# else:
#     print("n")
# class file_helper:
#     ins=None
#     def __init__(self,path):
#         self.file_object=open(path,mode="r",encoding="utf-8")
#     def __new__(cls, *args, **kwargs):
#         if not cls.ins:
#             cls.ins=super().__new__(cls)
#         return cls.ins
# obj1=file_helper("wite_test")
# obj2=file_helper("wite_test")
#
# print(obj1.file_object.read(1))#每一次用户访问不需要重新调用open方法，可直接接着读取字节
# print(obj1.file_object.read(2))
#25.pytorch-gpu 版本现在已经可以使用啦\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# import  torch

# #print(dir(getattr(torch,dir(torch)[dir(torch).index("cuda")])))#无聊写的可以尝试分析
# # print(type(torch.cuda.is_available))
# print(dir(torch.cuda))

#26.md5字符串加密\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# import hashlib
# def get_md(data):
#     obj=hashlib.md5("asd".encode("utf-8"))#此为加盐操作
#     obj.update(data.encode("utf-8"))#需要加密的data字符串 必须是utf-8编码
#     result=obj.hexdigest()
#     return result
# member={}
# #为了防止md5撞库，可以加盐
# def regester():
#     while True:
#         name = input("请输入用户名：")
#         key=input("请输入密码：")
#         member[name]=get_md(key)
#         if name== "N":
#                return
#         print(member)
# regester()
#27.正则化表达式 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\




#28.logging模块\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# import logging#logging模块对多个请求施行排队的方式处理，可以处理并发问题
# # import requests
# #
# # logging.basicConfig(filename="Logs",level=logging.ERROR,
# #                     format="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s",#定义写的格式
# #                     datefmt='%Y-%m-%d %H:%M:%S %p')#定义时间
# # #设置等级为debug debug及以上等级的信息会被生成在file里#basicConfig方法只适用于一个file_handel对象 即 下面只同时向一个文件写入
# # logging.error("alex")
# #
# # try:
# #     requests.get("http://www.google.com")
# # except Exception as e:
# #     var=str(e)#调用e.__str__ 方法
# #     logging.error(var,exc_info=True)# exc_info 返回错误的堆栈信息 直到错误来自哪一行
#
# file_handlers=logging.FileHandler(filename="Logs",mode="a",encoding="utf-8")#创建一个FILEhandler对象，该对象制定了写入地点和写入编码，将该对象
# #作为参数传入到logging对象的参数中 及完成了 编码方式，写入方式，文件名等共同设置。filehandler对象也包含fmt对象 可以设置格式，这里被basicConfig方法封装了
# logging.basicConfig(level=logging.ERROR,
#                     format="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s",
#                     handlers=[file_handlers],
#                     datefmt='%Y-%m-%d %H:%M:%S %p')#这种方法写出来，Logger名字就是root不能更改 也就是  %(name)s内部的内容
# logging.error("你好")
