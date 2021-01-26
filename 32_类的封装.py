# 类的封装
class Person:
    def __init__(self,name,age):
        print('初始化Person')
        self._name = name
        self._age = age

    @property
    def name(self):
        print('调用namegetter方法')
        return self._name

    @property
    def age(self):
        print('调用agegetter方法')
        return self._age

    @name.setter
    def name(self,name):
        print('调用namesetter方法')
        self._name = name

    @age.setter
    def age(self,age):
        print('调用agesetter方法')
        self._age = age

zs = Person('张三',18)
print(zs.name,zs.age)
zs.name = '王五'
zs.age = 28
print(zs.name,zs.age)