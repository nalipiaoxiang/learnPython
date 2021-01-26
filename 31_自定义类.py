# 类的基本结构
# class 类名([父类]):
#
#   公共的属性...
#
#   对象的初始化方法
#   def __init__(self,...):
#       ...
#
#   其他方法
#   def method_1(self,...):
#       ...
#
#   def method_2(self,...):
#       ...

# 创建对象的流程
#   变量 = 对象()的运行流程
#   1.创建一个变量
#   2.在内存中创建一个新对象
#   3.执行类的公共属性
#   4.__init__(self,...)方法执行
#   5.将对象的ID复制给变量


class Person :

    def __init__(self,name):
        self.name = name
    name = 'swk'

    def say_hello(self):
        # print(self)
        print('你好',self.name)

p1 =Person('猪八戒')
p2 =Person('沙和尚')

p1.say_hello()
p2.say_hello()