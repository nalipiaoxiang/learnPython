# 运算符
# 1.算数运算符
print(1+1)
print("a"+"b")
# +加,-减,*乘,/除,//整除,**幂,%取模
print(16**0.5) #16开平方
# 2.赋值运算符
a = 10
a = 30
print('a=',a)
a += 10
print('a=',a)
a -= 10
print('a=',a)
print('a=',a)
# 3.比较运算符(关系)
c = 1
d = 2
print(c > d)
print(c < d)
print(c == d)
print(c != d)
#比较Unicode编码
print('2' > '11')
print('a' > 'b')
# 4.逻辑运算符
# not逻辑非
# and逻辑与,短路,找False,如果第一个是False则不看第二个
# or 逻辑或,短路,找True,如果第一个是True则不看第二个
# 非布尔值逻辑运算返回原值
e = True
e = not e
print(e)
result = True and True # True
result = True and False # False
result = False and True # False
result = False and False # False
print(result)
result = True or True # True
result = True or False # True
result = False or True # True
result = False or False # False
print(result)
# 5.条件运算符(三元)
# 语法: 语句1 if 条件表达式 else 语句2
#       如果判断结果为True,则执行语句1,并返回执行结果
#       如果判断结果为False,则执行语句2,并返回执行结果
print('你好') if True else print('hello')
f = 10
g = 20
print('a的值比较大!') if f > g else print('b的值比较大!')
max = f if f > g else g
print(max)
