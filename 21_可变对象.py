# 可变对象
# 每个对象都有三个数据:
#   1.id(标识)
#   2.type(类型)
#   3.value(值)
#
# 列表就是一个可变对象
a = [1,2,3]
print('修改前:',a,id(a))
a_id = id(a)
a[0] = 9
print('修改后:',a,id(a))
# 这个操作修改了变量的值,不会改变指向的对象
a = [4,5,6]
print('修改后:',a,id(a))
# 这个操作是改对象,会改变指向的对象
# print('id为:',a_id,'的值为:',id(a_id))

# 改对象,会影响所有指向该对象的变量
b = a
print('a:',a,id(a))
print('b:',b,id(b))
b[0] = 0
print('a:',a,id(a))
print('b:',b,id(b))

# == 和 != 比较值是否相等
# is 和 is not 比较对象的id是否相等
a = [1,2,3]
b = [1,2,3]
c = a
print(id(a),id(b))
print(a == b)
print(a is b)
print(a is not b)
print(c is a)