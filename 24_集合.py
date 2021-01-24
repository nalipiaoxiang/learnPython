# 集合
# 集合和列表非常相似.
# 1.集合中只能存储不可变对象.
# 2.集合中存储的对象是无序.
# 3.集合中不能出现重复的元素.

# 使用{}创建集合
s ={1,2,3,4,5,1,1,1,1}
#s ={[1,2],[3,4]} TypeError: unhashable type: 'list'
print('s:',s,type(s)) #<class 'set'>

# 使用set()函数
s = set() #空集合
print('s:',s,type(s)) #<class 'set'>

# 可以通过set()来讲序列和字典转换为集合
s = set([1,2,2,3,4,5,1,1,1,1,2,3])
print('s:',s,type(s)) #<class 'set'>
s = set('hello')
print('s:',s,type(s)) #<class 'set'>
s = set({'a':1,'b':2,'c':3})
print('s:',s,type(s)) #<class 'set'>
s = {'a','b',1,2,3}
print('s:',s,type(s)) #<class 'set'>
# print(s[0]) TypeError: 'set' object is not subscriptable
print(list(s)[0])

# 使用in 和 not in 来检查集合中的元素
print('a' in s)

# len() 集合中的元素
print(len(s))
print(s)

# add() 向集合中添加元素
s.add(10)
print(s)

# update() 将一个集合中的元素添加到另一个集合中.
s2 = set('hello')
s.update(s2)
s.update((11,12,13))
s.update({10:100,100:1000,1000:1000})
s.update('序列')
print(s)

# pop() 随机删除集合中的元素
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s)

# remove() 删除集合中的指定元素
print(s.remove(1000)) # 不存在的键 KeyError:
print(s)

# clear() 清空集合
# copy() 对集合进行浅复制

# 创建两个集合
# 在对两个集合做运算时,不会影响原来的集合,而是将运算结果返回.
s = {1,2,3,4,5}
s2 = {3,4,5,6,7}

# & 交集运算
print(s & s2)
print(s,s2)

# | 并集运算
print(s | s2)
print(s,s2)

# - 差集(只要s有的)
print(s - s2)
print(s,s2)

# 异或集(只在一个集合中有的)
print(s ^ s2)
print(s,s2)

# <= 检查一个集合是否为另一个集合的子集
a = {1,2,3}
b = {1,2,3,4,5}
c = {1,2,3}
print(a <= b) #True
print(a <= c) #True

# 检查一个集合是否为另一个集合的真子集
print(a < b) #True