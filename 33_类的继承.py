# 类的继承

# 定义一个类 Animal(动物)
#       动物有俩个方法: run() sleep()
class Animal:
    def run(self):
        print('动物可以跑...')
    def sleep(self):
        print('动物可以睡觉...')

# 定义一个类 Dog(父类)
#       狗有俩个方法: run() sleep() bark()

class Dog(Animal):
    def bark(self):
        print('动物可以叫...')

d = Dog()
# 父类的方法
d.run()
d.sleep()
# 自己的方法
d.bark()

print(isinstance(d, Dog))
print(isinstance(d, Animal))

class Hashiqi(Dog):

    def __init__(self):
        print('使用super()调用父类的方法')
        super().bark()

    def chaijia(self):
        print('哈士奇在拆家')

h = Hashiqi()
h.run()
h.sleep()
h.bark()
h.chaijia()

# 在创建类时,如果省略了父类,则默认父类为object.
# object是所有类的父类，所有类都继承自object。

# issubclass()检查一个类是不是另一个类的子类
print(issubclass(Dog, Animal))
print(issubclass(Animal, object))
print(issubclass(int, object))

# isinstance() 用来检查一个对象是否是另一个类的实例
# 如果这个类是这个对象的父类也会返回True
print(isinstance(print, object))

class A(object):
    def test(self):
        print('AAA')

class B(object):
    def test2(self):
        print('BBB')

# 尽量避免多继承,多继承方法重写优先从前到后
class C(A,B):
    def test(self):
        print('CCC')

# 类名.__bases__ 查看当前类的所有父类
print(A.__bases__) # (<class 'object'>,)
print(B.__bases__) # (<class 'object'>,)
print(C.__bases__) # (<class 'object'>,<class '__main__.B'>)

c = C()
c.test()
c.test2()