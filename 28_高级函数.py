# 高级函数
# 在Python中函数是一等对象.
# 一等对象一般都会具有如下特点.
#   ① 对象是在运行时创建的.
#   ② 能赋值给变量或作为数据结构中的元素.
#   ③ 能做为参数传递.
#   ④ 能作为返回值返回.
# 高级函数
#   高级函数至少要符合以下两个特点中的一个.
#       ① 接收一个或多个函数作为参数.
#       ② 将函数作为返回值返回.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 常规
# 定义一个函数
#   把所有的偶数,保存到新的列表中

def fn(lst: list):
    '''
        fn()函数把指定列表中所有的偶数,保存到新的列表中
    :param lst: 要筛选的列表
    :return:
    '''
    # 创建一个新列表
    new_list = []
    # 对列表进行筛选
    for n in lst:
        # 判断n是奇数还是偶数
        if n % 2 == 0:
            new_list.append(n)
    # 返回结果
    return new_list


print(l)
print(fn(l))


# 进化+1
#  把所有的偶数,保存到新的列表中
def fn_new(lst: list):
    # 检查偶数
    def fn2(i):
        if i % 2 == 0:
            return True
        return False

    # 检查大于5
    def fn3(i):
        if i > 5:
            return True
        return False

    # 创建一个新列表
    new_list = []
    # 对列表进行筛选
    for n in lst:
        # 判断n是奇数还是偶数
        if fn2(n):
            new_list.append(n)
    # 返回结果
    return new_list


print(fn_new(l))


# 进化+2
# 检查偶数
def fn2(i):
    if i % 2 == 0:
        return True
    return False


# 检查大于5
def fn3(i):
    if i > 5:
        return True
    return False


def fn_new_new(func, lst: list):
    # 创建一个新列表
    new_list = []
    # 对列表进行筛选
    for n in lst:
        # 判断n是奇数还是偶数
        if func(n):
            new_list.append(n)
    # 返回结果
    return new_list


print(fn_new_new(fn2, l))
print(fn_new_new(fn3, l))


def fn4(i):
    if i % 3 == 0:
        return True
    return False


print(fn_new_new(fn4, l))

# filter(function, iterable)
# 用 iterable 中函数 function 返回真的那些元素，构建一个新的迭代器。
# iterable 可以是一个序列，一个支持迭代的容器，或一个迭代器。
# 如果 function 是 None ，则会假设它是一个身份函数，
# 即 iterable 中所有返回假的元素会被移除。
# 请注意， filter(function, iterable) 相当于一个生成器表达式，
# 当 function 不是 None 的时候为
# (item for item in iterable if function(item))；
# function 是 None 的时候为 (item for item in iterable if item) 。
# 请参阅 itertools.filterfalse() 了解，
# 只有 function 返回 false 时才选取 iterable 中元素的补充函数。

print(filter(fn4, l))  # <filter object at 0x0000026CD7169CD0>
print(list(filter(fn4, l)))


# 匿名函数
# Lambda 函数表达式
# Lambda函数表达式专门用来创建一些简单的函数,他是创它是创建函数的又一种方式.
# 语法: lambda 参数列表 : 返回值

def fn5(a, b):
    return a + b


print(fn5(123, 456))

lambda a, b: a + b
print(lambda a, b: a + b)  # <function <lambda> at 0x0000028F2EB114C0>
print((lambda a, b: a + b)(10, 20))

fn6 = lambda a, b: a + b
print(fn6)
print(fn6(10, 50))

print(list(filter(lambda i: i % 3 == 0, l)))
print(list(filter(lambda i: i % 2 == 0, l)))
print(list(filter(lambda i: i != 0, l)))
print(list(filter(lambda i: i > 5, l)))

# map()
# map()函数可以对可迭代对象中的所有元素做指定操,将其添加到新的对象中返回.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r = map(lambda i: i + 1, l)
print(list(r))

r = map(lambda i: i ** 2, l)
print(list(r))

# sort() 列表
# sort()函数用来排序
# 默认比较元素的大小
l = ['bb','aaaa','c','dddddddd','fff']
print(l)
l.sort()
print(l)
# 在sort()可以接收一个关键字参数,key
#   key需要一个函数作为参数,当设置了函数作为参数.
#   每次都会以列表中的一个元素作为参数来调用,并且使用函数的返回值来，比较元素的大小。
l.sort(key=len)
print(l)
l.sort(key=len,reverse=True)
print(l)
l = [2,5,'1',3,'6','9']
l.sort(key=int)
print(l)

# sorted()
# sorted()任意序列
# 不会影响源列表
l = [2,5,'1',3,'6','9']
l = '98216456465468145648'
print('排序前:',l)
print('排序时:',sorted(l, key=int))
print('排序后:',l)

def fn666():
    def inner():
        print('我是fn2')
    return inner

print(fn666())
r = fn666()
print(r())