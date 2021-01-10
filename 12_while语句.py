# while语句
# 语法 :
#   while 条件表达式 :
#       代码块
#   else
#       代码块

# 循环三个要件(表达式)
# 初始化表达式,通过初始化表达式初始化一个变量
i = 1000
#条件表达式,条件表达式用来设置循环执行条件
while i < 100 :
    #更新表达式,修改初始化变量的值
    i += 1
    print('hello world',i)
else:
    print('else')
print('循环完毕')