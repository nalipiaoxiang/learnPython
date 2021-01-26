# 类
# 定义一个类
# 语法: class 类名([父类]):
#       代码块

class MyClass():
    pass

print(MyClass) # <class '__main__.MyClass'>

mc = MyClass()
mc_1 = MyClass()

# <__main__.MyClass object at 0x0000025FFC8FCBB0> <class '__main__.MyClass'>
print(mc,type(mc))

# 用isinstance() 来检查对象是否是一个类的实例
print(isinstance(mc,MyClass))
print(isinstance(mc_1,MyClass))

print(id(MyClass))
print(type(MyClass)) # <class 'type'>

mc.name = 'swk'
print(mc.name)