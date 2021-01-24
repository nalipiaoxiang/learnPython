# 遍历字典
# keys() 该方法会返回字典的所有key.
# 这些方法会返回一个序列序列中，保存有字典的所有的键.
d = {'name': '孙悟空', 'age': 18, 'gender': '男'}

# 通过遍历所有的keys()来获取所有的键
print(d.keys())

for k in d.keys():
    print(k, d[k])

# values()
# 该方法会返回一个序列,序列中存有字典的所有的值
for v in d.values():
    print(v)

# items()
# 该方法会返回字典中所有的项
# 它会返回一个序列,序列中包含双值子序列
# 双值就是字典中的键和值
print(d.items())

for k, v in d.items():
    print(k, '=', v)
