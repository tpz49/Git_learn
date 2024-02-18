#一个用于测试各种模块导入操作的模块
# num=1
# class F:
#     x=1
#     @staticmethod
#     def func():
#         print('1')
#     def bond(self):
#         print("绑定方法")
#
#
# def leixingzhushi(x:str,y:str="b")-> str:
#     print("1")
#     # return x+"and"+y
#     return x+y
# a=leixingzhushi("a")
# print(a)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# import json
# import os
# import random#令一个变量等于random alt加回车 导入该模块
# import sys
# import time
#
# ram=random
# sy=sys
# ti=time
# o=os
# js=json
#
# class Foo:
#     print("test")#只要创造类就会执行
#     def fun(self):
#         pass

# class Foo:
#     def __init__(self,age):
#         self.age=age
#     def display(self):
#         return self.age
# f=Foo(5)
# print(f.age,f.display())
# a=Foo(f.display())
# print(a.age)
# class Foo:
#
#     def __getitem__(self, item):
#         return item
#
# f=Foo()
# print(f[2])


# li=["李杰","苛责"]
# for item in li:
#     if item.startswith("李"):
#         li.remove(item)
# print(li)

# class Foo:
#     ins = None
#
#     def __new__(cls, *args, **kwargs):
#
#         if Foo.ins:
#             return Foo.ins
#         Foo.ins=super().__new__(cls)
#         return Foo.ins
# f=Foo()
# a=Foo()
# print(f,a)

