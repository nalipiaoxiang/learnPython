# break和continue
# break跳出循环
i = 0
while i < 5 :
    if i == 3 :
        break
    print(i)
    # 循环控制
    i += 1
else:
    print('进入while循环的else阶段')
print('程序结束')

# continue跳出本次循环,继续下一次
i = 0
while i < 5 :
    # 循环控制
    i += 1
    if i == 3 :
        print(f'当前数字{i},跳过当前')
        # continue需要写在循环控制的下面
        continue
    print(i)
else:
    print('进入while循环的else阶段')
print('程序结束')