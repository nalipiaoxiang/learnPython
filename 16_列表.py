# 列表
# 创建列表,通过[]创建列表
my_list = [] # 创建了一个空列表
print(my_list , type(my_list))

# 列表存储的数据,我们称为元素
# 一个列表中可以存储多个元素,也可以在创建列表时,来指定列表中的元素.
my_list = [10] # 创建一个只包含一个元素的列表.
print(my_list)
print(id(my_list))

my_list = [10,20,30,40,50]
print(my_list)
print(id(my_list))

# 列表中可以保存任意的对象。
my_list = [10,'hello',True,None,[1,2,3],print]
print(my_list)

# 列表中的对象都会按照插入的顺序存储列表中/
my_list = [10,20,30,40,50]

# 通过索引(index)来获取列表中的元素
# 所以是元素在列表中的位置.列表中的每一个元素都有一个索引.
# 所以是从0开始的整数列表，第一个所以为0,二1,三2...
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
# print(my_list[5]) IndexError: list index out of range

# 获取列表的长度
print(len(my_list))

# 切片
# 切片指从现有列表中获取一个子列表
# 创建列表一般变量名会用复数
stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']
print(stus)

# 如果是索引是负数,则从后向前获取元素,-1表示倒数第一个,-2表示倒数第二个...

# 通过切片获取指定元素
# 语法 : 列表[起始:结束]
#   通过切片获取元素时,会包括起始位置的元素,不会包括结束位置的元素
#   返回一个新列表,不影响原始列表
#   省略结束位置,则一直到最后
#   省略开始位置,则从头开始
#   全省略,则复制全部
print(stus[0:5])

# 语法 : 列表[起始:结束:步长]
# 默认步长为1,不能为0
# 如果是步长是负数,则从后向前获取元素
print(stus[0:5:2])

# + 和 *
# +可以将两个列表拼接
# *复制
my_list = [1,2,3] + [4,5,6]
my_list = [1,2,3] * 5
print(my_list)

# 创建一个列表
stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精','沙和尚','沙和尚']

# in 和 not in
# in用来检测指定元素是否存在列表中
# not in 与之相反
print('沙和尚' in stus)
print('牛魔王' in stus)

# len() 元素个数
arr = [1614,1561,516,4,23,564,89,7,126,0,48,]
# min() 最小值
# max() 最大值
print(len(arr),min(arr),max(arr))

# 两个方法(method) , 方法和函数基本一致,方法必须通过 对象.方法()的形式调用
# index()
print(stus.index('孙悟空')) # 元素在列表中第一次出现的索引,没有的元素会报错
# 第二个参数,表示查找的起始位置,第三个参数表示查找的结束位置(不包括)
print(stus.index('沙和尚',3,7))
# count() 统计指定元素在列表中出现的次数
print(stus.count('沙和尚'))



