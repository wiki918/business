'''
@author: wangwei
@project: workdirly
@file: exe_Singleton.py
@time: 2019-10-25 11:18
@desc:
'''


'''
所谓单例，是指一个类的实例从始至终只能被创建一次。
'''



'''
method 1：使用__new__方法会很简单。Python中类是通过__new__来创建实例的
'''
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance
if __name__ == '__main__':
    class A(Singleton):
        def __init__(self,s):
            self.s = s

    a = A('apple')
    b = A('bannana')
    print(id(a), a.s)
    print(id(b), b.s)

print("***%%%%%****")

#python3
class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # cls.__instance = super().__new__(cls)
            # cls.__instance = object.__new__(cls)
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, status_number):
        self.status_number = status_number

test1 = Singleton("2")
print(id(test1),test1.status_number)

test2 = Singleton("3")
print(id(test2),test2.status_number)
class Foo(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance
class A(Foo):
    def __init__(self,s):
        self.s = s
a = A('apple')
b = A('bannana')
print(id(a))
print(id(b))
# a = Foo()
# b = Foo()
# print(id(a)==id(b))

class Test(object):

    __instance = None

    def __init__(self):
        print("----init方法----")

    def __del__(self):
        print("----del方法----")

    def __str__(self):
        print("----str方法----")

    def __new__(cls):
        print("----new方法----")
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

test1 = Test()
print(id(test1))

test2 = Test()
print(id(test2))


