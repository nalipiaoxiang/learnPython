# 递归
def recursion(n):
    if n == 1:
        return 1
    return n * recursion(n-1)

print(10*9*8*7*6*5*4*3*2*1)
print(recursion(10))

# n ** i 幂运算(power)
def power(n:int,i:int)-> int:
    '''
    这是一个计算幂运算的函数
    :param n: 计算的数
    :param i: 幂
    :return: 结果
    '''
    # 基线条件
    if i == 0:
        return 1
    elif i == 1:
        return n
    # 递归
    return n * power(n,i-1)

print(2**16)
print(power(2, 16))




# 回文(Palindrome)字符串
# abcba
#  bcb
#   c

def hui_wen(s:str)->bool:
    '''
    检查字符串是否为回文
    :param s: 待检测字符串
    :return: 结果
    '''
    # 基线条件
    if len(s) <2:
        return True
    elif s[0] != s[-1] :
        return False
    # 递归
    return hui_wen(s[1:-1])

# 测试回文
print(hui_wen('asdfghjkllkjhgfdsa'))
print(hui_wen('asdasd'))
print(hui_wen('abcba'))