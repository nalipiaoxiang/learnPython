# 遍历列表
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧']

# 遍历
print('1.原始方法遍历列表')
print(stus[0])
print(stus[1])
print(stus[2])
print(stus[3])

# 循环遍历
print('2.while循环遍历')
i = 0
while i < 4:
    print(stus[i])
    i += 1

print('3.while循环遍历Plus')
i = 0
while i < len(stus):
    print(stus[i])
    i += 1
# 通过for循环遍历
# 语法:
#   for 变量 in 序列 :
#       代码块
print('4.for循环遍历')
for s in stus:
    print(s)
