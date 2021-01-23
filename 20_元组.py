# 元组 tuple
# 元组是不可变序列

# 创建元组
my_tuple = ()
print(my_tuple)
print(type(my_tuple))

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[1])

# 当元组不是空时,括号可以省略
my_tuple = 10, 20, 30, 40, 50
print(my_tuple)
my_tuple = 50,  # my_tuple = (60) 这样的数据不是元组,而是整形
print(my_tuple, type(my_tuple))

my_tuple = 10, 20, 30, 40, 50
# 元组的解包(解构)
a, b, c, d, e = my_tuple
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)
print('e =', e)

# 交换变量的值
a = 100
b = 300
print(a, b)
a, b = b, a
print(a, b)

# 解包(序列都可以)
# 在对一个元组进行解包时,变量的数量必须和元组中的数量一致
# 也可以在变量前边加一个*,这样可以接受剩余元素
# *可以在任意前中后,不可以多个
print(my_tuple)
a, b, *c = my_tuple
print('a =', a)
print('b =', b)
print('c =', c)
