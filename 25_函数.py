# 函数
# 函数的定义(function)
#   函数也是一个对象
#   对象是内存中专门用来存储数据的一块区域.
#   函数可以用来保存一些可执行的代码,并且可以在需要的时候,对这些语句进行调用.
#   创建函数(defind定义)
#       def 函数名([形参1,形参2,...形参n]) :
#           代码块
#   函数名需要符合规范(字母,数字,下划线,不能以数字开头)
# 定义函数
def fn():
    print('this is my fist function')
    print('It\'s a nice day today')


# 打印fn
print(fn)  # <function fn at 0x00000250BE8A9160>
print(type(fn))  # <class 'function'>

# 调用函数
#   函数对象()
# fn是函数对象 fn()调用函数
# print是函数对象 print()调用函数
fn()

print('*'*60)
# 参数可以设置默认值
# 如果用户传递了参数,默认值会失效
# 如果用户没有传默认值,则默认值生效
def fn1(a,b,c=10):
    print('a=',a)
    print('b=',b)
    print('c=',c)
fn1(1,2)
print('*'*60)

# 位置参数,形参和实参的顺序必须一致
# 关键字参数,不需要肾虚
# 混合使用位置参数必须不能放到前面
fn1(c=7,b=6,a=5)
print('*'*60)

# 不定长参数,参数前加*,转化为<class 'tuple'>
def fn3(a,b,*c):
    print('a=',a,type(c))
    print(sum(c))
print(type(range(0,101)))
print(sum(range(0,101)))
fn3(1,2,3,4,5)

# *只能接受位置参数
# **(只能有一个,必须放在最后)接受关键字参数,将这些参数保存到字典中.
def two_xing(**a):
    print('a=',a,type(a))
two_xing(a=2,b=3,c=1)