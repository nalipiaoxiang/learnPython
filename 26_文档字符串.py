# 文档字符串
# help()是python中的内置函数
# help(print)


def fn(a:int,b:bool,c:str='hello') -> int:
    '''
    :param a: 参数a
    :param b: 参数b
    :param c: 参数c
    :return: 返回10
    '''
    print(locals())
    global_scope = globals()
    print(global_scope)
    return 20

# help(fn)
# help(str)

# 当前的命名空间
print(locals())
fn(1,2,3)
scope = locals()
scope['c'] = 'HelloWorld'
# print(c) 向作用域中添加未定义变量相当代码中创建变量

# 递归
def recursion(n):
    if n == 1:
        return 1
    return n * recursion(n-1)

print(10*9*8*7*6*5*4*3*2*1)
print(recursion(10))

# n ** i 幂运算(power)
def power(n:int,i:int)-> int:
    if i == 0:
        return 1
    elif i == 1:
        return n
    return n * power(n,i-1)

print(2**16)
print(power(2, 16))




# 回文(Palindrome)字符串 abcba



