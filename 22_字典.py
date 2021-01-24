# 字典(dict)
# 字典属于一种新的数据结构，称为映射( Mapping )
# 字典的作用和列表类似都是用来存储对象的.
# 列表存储数据的性能很好.查询数据的性能很差.
# 在字典中每一个元素都有一个唯一的名字,通过这个唯一的名字可以快速的查找到指定的元素.
# 在查询元素时,字典的效率是非常快的.
# 在字典中可以保存多个对象,每个对象都会有一个唯一的名字.
#   这个唯一的名字我们称其为键(Key),通过key可以快速查找value
#   这个对象,我们称其为值(Value)
#   所以字典,我们也称为叫做键值对(Key-Value)结构.
#   每个字典中都可以有多个键值对,按每一个键值对我们称其为一项(Item)

# 使用{}创建字典
d = {}  # 空字典
print(d, type(d))
# 语法:
#   {key:value,key:value,key:value,key:value,key:value,...}
#   字典的值可以是任意对象
#   字典的键可以是任意不可变对象(int,str,bool,tuple...)
#   字典的键是不能重复的,如果重复会被后边的替换掉
d = {'name': '孙悟空', 'age': 18, 'gender': '男'}
print(d, type(d))

# 根据键获取值
print(d['name'], d['age'], d['gender'])
# print(d['hello']) 不存在的键 报错KeyError: 'hello'

# 使用dict()函数创建字典
# key都是字符串
d = dict(name='猪八戒', age=19, gender='男')
print(d, type(d))

# 将一个包含双值子序列转换为字典
# 双值序列,序列中只有两个值,[1,2],('a',3),'ab'
# 子序列,如果序列中的元素也是序列,那么我们就称这个元素为子序列
# [(1,2),(3,5)]
d = dict([('name','熏悟空'),('age',27)])
print(d, type(d))

# len() 获取字典中键值对的个数
print(len(d))

# in 和 not in
# in 检查字典中是否包含指定的键
print('name' in d)
print('hello' in d)

# 获取字典的值
# 语法: d[key]
# 如果key不存在会抛出异常
print(d['name'])

# get(key[,default]) ,通过该方法来获取字典中的值
# 获取的键没有时不会报错
print(d.get('name'))
print(d.get('hello'))
# 获取不到返回默认值
print(d.get('hello','默认值'))

# 修改字典
# d[key] = value
d['name'] = '老熏'
# 没有就加上
d['address'] = '花果山'
print(d)

# setdefault(key[,default])
#   如果key存在于字典中,则返回key值,不会对字典做任何操作
#   如果key不存在,则向字典中添加这个key,并设置value
print(d.setdefault('name', '猪八戒'))
print(d.setdefault('hello', '猪八戒'))
print(d)

# update([other])
# 将其他的字典中的key-value添加到当前字典中.
# 如果有重复的key则后边的会替换到当前的.
d = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6,'a':7}
d.update(d2)
print(d)

# 删除,可以使用del来删除字典中的key-value.
del d['a']
print(d)

# popitem() 删除空字典会报错
# 随机删除字典中的一个键值对,一般都会删除最后一个键值对.
# 返回的是一个元组。元素中有两个元素,第1个元素是删除的key,第2个删除的是vlue.
print(d.popitem())
print(d)

# pop(key[,default])
# 根据key删除字典中的key-value.
# 它会将删除的值返回
# 删除不存在的key,会抛出异常
print(d.pop('d'))
print(d.pop('z','删除不存在的key不会报错,返回这个默认值'))
print(d)

# clear() 清空字典
# copy()
# 该方法用于对字典进行浅复制(如果字典的值还是字典则失效)
d = {'a':1,'b':2,'c':3}
# 两个变量指向一个对象不属于复制
d2 = d
print('d =' ,d,id(d))
print('d2 =' ,d2,id(d2))

d2 = d.copy()
print('d =' ,d,id(d))
print('d2 =' ,d2,id(d2))

# 浅复制中的可变对象无法真正复制
d = {'a':{'name':'熏悟空'},'b':2,'c':3}
d2 = d.copy()
print('d =' ,d,id(d))
print('d2 =' ,d2,id(d2))
d2['a']['name'] = '猪悟净'
print('d =' ,d,id(d),id(d['a']))
print('d2 =' ,d2,id(d2),id(d2['a']))