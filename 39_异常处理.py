# 异常
# try语句:
#   try:
#       代码块(可能出错的语句)
#   except 异常类型 as 异常名(变量):
#       代码块(出现错误以后的处理方式)
#   except 异常类型 as 异常名(变量):
#   ...
#       代码块(出现错误以后的处理方式)
#   else:
#       代码块(没出错要执行的语句)
#   finally::
#       代码块(无论是否异常总会执行)

print(1)
try:
    print(a)
    print(1/0) #ZeroDivisionError: division by zero
except NameError as e:
    # except 跟单个异常类型,则只会捕获一种异常
    print('出NameError')
    print(e)
except ZeroDivisionError:
    print('出现ZeroDivisionError')
except:
    print('捕获所有异常')
else:
    print('没有出错')
finally:
    print('无论是否异常都执行')
print(2)

# print(1/0)
def fn():
    print('hello fn')
    # print(1 / 0)

fn()

# ZeroDivisionError
# NameError

# raise 抛出异常

class MyError(Exception):
    print('自定义异常')

def add(a,b):
    if a <0 or b <0:
        # 如果是a或b是负数抛异常
        # raise Exception('两个参数不能有负数')
        raise MyError('两个参数不能有负数')
    r = a + b
    return r


print(add(1, -2))