# 条件判断语句(if语句)
# 语法: if 条件表达式 : 语句
#   如果为True,则执行if后面的语句
#   如果为False,则不执行
if True : print("出来了")
if False : print("出来了")
# 默认情况下,if语句只会控制紧随其后的语句,如果希望控制多条语句
#可以在if后面跟着一个代码块
# 代码块
#   代码块中保存着一组代码,要么都执行,要么都不执行
#   代码块就是一种为代码分组的机制
if True :
    print('hell01')
    print('hell02')
if False :
    print('hell04')
    print('hell05')
print("if结束")