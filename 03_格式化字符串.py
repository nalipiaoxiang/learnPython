# 格式化字符串
# 字符串之间的加法,起到拼接的作用
a = 'aaa' + 'bbb' + 'ccc'
print(a)
# 字符串不能喝其他类型进行加法运算
b = 123
print("a = ",b)
# 在创建字符串时,可以在字符串中指定占位符
# %s 在字符串中便是任意字符串
c = 'hello %s'  %'艾斯比'
d = 'hello %s 你好 %s'  %('艾斯比','沙雕')
e = 'hello%5s'  %'a'
f = 'hello%3.5s'  %'aaaaaaaaaaa'
print(c)
print(d)
print(e)
print(f)
# %f 浮点数占位符
# %d 整数占位符
g = '小数%f'  %0.123456789
h = '小数%.2f'  %0.123456789
i = '小数%.9f'  %0.123456789
print(g)
print(h)
print(i)
number = 'abc'
print('a = %s' %number)

# 格式化字符串,可以通过在字符串前添加一个f来创建一个格式化字符串
# 在格式化字符串中可以直接嵌入变量
j = f'hello {a} {b}'
print(j)

# 字符串的复制
k = '哈'
print(k * 2)
print(k * 20)
