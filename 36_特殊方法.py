# 特殊方法(魔术方法)
# __开头和__结尾
# 特殊方法一般不需要我们手动调用,需要在一些特殊的情况下自动执行.

class Person(object):
    '''
        人类
    '''

    def __init__(self,name,age):
        self.name = name
        self.age = age

    # __str__() 会在尝试将这个对象转换为字符串的时候调用
    def __str__(self):
        return 'Person [name=%s,age=%d]'%(self.name,self.age)

    # __reper__() 会在当前对象使用reper()函数时调用
    # reper() 在'交互模式'中直接输出效果
    # 在python console
    # >>> a = 'hello'
    # >>>print(a)
    # hello
    # >>>a
    # 'hello'
    def __repr__(self):
        return 'Hello'

    # object.__lt__(self, other) 小于
    # object.__le__(self, other) 小于等于
    # object.__eq__(self, other) 等于
    # object.__ne__(self, other) 不等于
    # object.__gt__(self, other) 大于
    # object.__ge__(self, other) 大于等于
    # self:当前对象 other:和当前对象比较的对象
    def __gt__(self, other):
        return self.age > other.age

    # __len__() 长度

    # __bool__() 对象转布尔值时使用
    def __bool__(self):
        return self.age >17


# 创建person实例
p1 =Person('孙悟空',18)
p2 =Person('猪八戒',28)

print(p1) # <__main__.Person object at 0x000002B1A05FCBB0>

print(repr(p1))

# print(p1 > p2)
# TypeError: '>' not supported between instances of 'Person' and 'Person'

print(p1 > p2)
print(p2 > p1)

print(bool(p1))

if p1:
    print(p1.name,'已经成年了')
else:
    print(p1.name, '未成年了')