# 装饰器

def add(a,b):
    '''
    求任意两个数的和
    '''
    return a+b

def mul(a,b):
    '''
    求任意两个数的积
    '''
    return a*b

r =add(123,456)
print(r)

# 希望打印前加入日志

def new_add(a,b):
    print('计算开始...')
    result =add(a,b)
    print('计算结束...')
    return result


print(new_add(111, 222))

# 优化升级
def fn():
    print('我是fn()函数')


def begin_end(old):
    '''
    扩展
    '''
    # 创建一个新函数
    def new_functuion(*args,**kwargs):
        print('开始执行...')
        # 调用被扩展的函数
        result = old(*args,**kwargs)
        print('开始结束...')
        return result
    return new_functuion

f = begin_end(fn)
f()
ff = begin_end(add)
print(ff(111, 555))

@begin_end
def say_hello():
    print('HelloWorld')

say_hello()