# 垃圾回收


class A:
    def __init__(self):
        self.name = 'A类'

    # del是一个特殊方法,它会在对象被垃圾回收前调用.
    def __del__(self):
        print('A()对象被删除',self)

a = A()

print(a.name)

a = None
# 将a设置为None,此时没有任何变量对A()对象进行应用就变成垃圾


input('回车键退出...')