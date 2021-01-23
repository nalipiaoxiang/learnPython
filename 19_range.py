# range()函数
# 可以生成一个自然数序列
print(list(range(5)))
print(list(range(10)))
# 该函数需要三个参数
#   1.起始位置
#   2.结束位置
#   3.步长(可以省略,默认1)
#   [a,b)
print(list(range(0,10)))
print(list(range(0,10,2)))
print(list(range(10,0,-1)))

# 通过range()可以执行指定次数的for循环
for i in range(1,10):
    print(i)
