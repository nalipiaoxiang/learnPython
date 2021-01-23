# 序列(sequence)
# 一种数据存储的结构
# 序列的分类
#   可变序列(序列中的元素可以改变)
#       > 列表(list)
#   补不可变序列(序列中的元素不可以改变)
#       > 字符串(str)
#       > 元组(tuple)
# 通用操作

# 可变序列
# 列表修改
# 1.通过索引修改(不变序列无法使用)
stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']
print('修改前:',stus)
stus[0] = 'xunwukong'
print('修改后:',stus)
# 2.通过del删除元素
del  stus[2] #删除索引为2的元素
print('删除后:',stus)

# 2.通过切片修改
stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']
print('修改前:',stus)
# stus[0:2] = 'swk'
# print('修改后:',stus)
# 再给切片赋值时只能使用序列
# stus[0:2] = 123,456,789
# print('修改后:',stus)
# stus[0:2] = "123","456","789"
stus[0:2] = ['牛魔王','红孩儿','二郎神','玉面狐狸']
print('修改后:',stus)
# 插入
stus[0:0] = ['牛魔王']
print('修改后:',stus)
# 步长和替换序列要=
print('步长:',stus[::2])
stus[::2] = ['#', '#', '#', '#', '#']
print('修改后:',stus)

# 通过切片删除
del  stus[::2]
print('删除后:',stus)
stus[0:2] = []
print('删除后:',stus)

# 类型转换
s = 'hello'
print(s)
print(list(s))

# 通过方法修改列表
stus = ['孙悟空','猪八戒','沙和尚']
print('源列表:',stus)

# append() 向列表后添加一个元素
stus.append('唐僧')
print('修改后',stus)
# insert()
#   参数:
#       1.插入的位置
#       2.插入的元素
stus.insert(2,'唐僧')
print('修改后',stus)
# extend() 用新序列宽展
stus.extend(['唐僧','白骨精','白晶晶']) # stu += ['唐僧','白骨精','白晶晶']
print('修改后',stus)

# clear()
stus.clear()
print('清空后',stus)

# pop()
# 根据索引删除并返回指定元素
stus = ['孙悟空','猪八戒','沙和尚']
print('源列表:',stus)

print('删除了:',stus.pop(2))
print('删除后:',stus)
# 无参数表示最后
print('删除了:',stus.pop())
print('删除后:',stus)

# remove()
# 删除指定元素
stus = ['孙悟空','猪八戒','沙和尚','沙和尚']
print('源列表:',stus)
stus.remove('沙和尚') #只删除第一个
print('删除后:',stus)

# reverse()
# 翻转
stus.reverse()
print('翻转后:',stus)

# sort()
# 排序
my_list = list('qwertyuioplkjhgfdsazxcvbnm')
print('修改前:',my_list)
my_list.sort() # 默认升序
print('修改前:',my_list)
my_list.sort(reverse=True) # 降序
print('修改前:',my_list)
