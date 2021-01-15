# 循环的嵌套
# 控制台打印矩形

#外层控制行数
i = 0
while i <5 :
    #控制列数
    j = 0
    while j <5 :
        print('#',end='')
        j += 1
    # 打印完后换行
    print()
    i += 1

# 打印三角形
#外层控制行数
i = 0
while i <5 :
    #控制列数
    j = 0
    while j < i + 1 :
        print('#',end='')
        j += 1
    # 打印完后换行
    print()
    i += 1

# 打印倒立三角
#外层控制行数
i = 0
while i < 5 :
    #控制列数
    j = 0
    while j < 5 - i :
        print('#',end='')
        j += 1
    # 打印完后换行
    print()
    i += 1

# 打印9*9乘法表
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
#外层控制行数
i = 0
while i < 100 :
    #控制列数
    j = 0
    while j < i + 1 :
        print(j + 1,'*',i + 1 ,'=',( j + 1 )*( i + 1 ),' ',end='')
        j += 1
    # 打印完后换行
    print()
    i += 1