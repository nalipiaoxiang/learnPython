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
