# 测试模块
print('我是测试模块')
print(__name__)
a = 10
b = 20

def test1():
    print('test1')

def test2():
    print('test2')

def test3():
    print('test3')

class Person:
    def __init__(self):
        self.name = '熏悟空'


# 测试的时候执行
if __name__ == '__main__':
    test3()