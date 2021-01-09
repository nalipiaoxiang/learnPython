# 类型转换
# 类型转换四个函数 int(),float(),str(),bool()
# int() 可以用其他的对象转换为整形
# 布尔值: True -> 1 False -> 0
# 浮点数: 直接取整,省略小数点后的内容
# 字符串: 合法的整数字符串直接转化成对应的数字
#        如果不是一个合法的整数字符串,则报错
a = True
print('a = ',a)
print('a的类型是',type(a))
# int函数不会改变原来的变量产生影响
print('a = ',int(a))
print('a的类型是',type(int(a)))
# str()可以将对象转换为字符串
# True  -> 'True'
# False -> 'False'
# 123   -> '123'
b = True
print('b = ',str(b))
print('b的类型是',type(str(b)))
# 可以将对象转换为布尔值,任何对象都可以转换成为布尔值
# 规则:对于所有表示空性的对象都会转换成为False,其余的转换为True
# 空性: 0,None,''
c = False
c = ''
c = None
c = 0
print('c = ',bool(c))