# 文件
# I/O
# 文件操作步棸
#   1.打开文件
#   2.操作文件(读,写)
#   3.关闭文件

# 打开文件
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 参数:
# file 要打开文件的名字
# r'xxx' 原始字符串
file_name = r'demo.txt'

# 打开文件
file_obj = open(file_name,encoding='utf-8')

print(file_obj)

content = file_obj.read()

print(content)

# 关闭
file_obj.close()

# with ... as 语句
with open(file_name,encoding='utf-8') as  file_obj:
    # 在with语句中可以直接使用file_obj来对文件进行操作
    print(file_obj.read())
# file_obj.read()
# with 结束文件会自动结束


# 文件
#   一种,纯文本文件
#   一种,二进制文件
with open('shi.txt',encoding='utf-8') as  file_obj:
    # read()可以接收一个size作为参数,用于读取字符的个数
    # 默认为-1,读取所有
    content = file_obj.read(6)
    print(content, '长度:', len(content))
    content = file_obj.read(6)
    print(content, '长度:', len(content))
    content = file_obj.read(6)
    print(content, '长度:', len(content))
    content = file_obj.read(6)
    print(content,'长度:',len(content))

# 读取大文件
try:
    with open('shi.txt',encoding='utf-8') as file_obj:
        # 每次读取个数
        chunk = 6
        while True:
            # 读取chunk大小的内容
            content = file_obj.read(chunk)
            if not content:
                # 内容读取完毕
                break
            print('长度:',len(content),content,end='')
        print()
except FileNotFoundError:
    print('文件不存在')

try:
    with open('shi.txt',encoding='utf-8') as file_obj:
        # 每次读取个数
        chunk = 6
        while True:
            # 读取chunk大小的内容
            content = file_obj.readline()
            if not content:
                # 内容读取完毕
                break
            print('长度:',len(content),content,end='')
        print()
except FileNotFoundError:
    print('文件不存在')

with open('shi.txt',encoding='utf-8') as file_obj:
    lines = file_obj.readlines()
    print(lines)
    print(lines[0],end='')
    print(lines[1],end='')
    print(lines[2],end='')
    print(lines[3])

with open('shi.txt', encoding='utf-8') as file_obj:
    # 使用for迭代file_obj也是一行一行的读
    for t in file_obj:
        print(t)

# open()打开文件 读,写,追加 不指定默认为读
# mode='r' 读
# mode='w' 写                文件不存在会创建文件
# mode='a' 最近 append       文件不存在会创建文件
# mode='+' 为操作增加功能      r+ 可读可写,文件不存在报错 w+ a+
# mode='x' 新建
with open('xie.txt','a', encoding='utf-8') as file_obj:
    # write()写
    # 写文本,需要传递字符串做参数
    print(file_obj.write('HelloWorld\n'))
    print(file_obj.write('HelloWorld\n'))
    print(file_obj.write('HelloWorld\n'))

# 读二进制
# mode='t' 读取文本(默认值)
# mode='b' 读取文二进制
file_name = 'G:/无损音乐/薛之谦 - 天外来物.flac'
with open(file_name,'rb') as file_obj:
    # 读取文本,字符为单位
    # 读二进制,字节为单位
    print(file_obj.read(100))

# 读写
file_name = 'G:/无损音乐/薛之谦 - 天外来物.flac'
with open(file_name,'rb') as file_obj:
    # 写到当前目录
    new_name = '1.flac'
    with open(new_name,'wb') as new_obj:
        # 定义读取大小
        # 每次读取1kb
        chunk = 1024 * 1024 * 10
        while True:
            # 读取数据
            content = file_obj.read(chunk)
            print('读取了:',len(content),'个字节')
            # 内容读取完毕,终止循环
            if not content:
                print('读取了完毕')
                break
            # 将读取的东西写到新的东西里
            new_obj.write(content)

# 二进制读取文本
with open('demo.txt','rb') as file_obj:
    print(file_obj.read(5))
    # tell()当前读取的位置
    print('当前读取的位置->',file_obj.tell())
    # seek() 修改当前读取的位置
    # 两个参数
    #   1.前换到的位置
    #   2.计算位置的方式
    #       可选值:
    #           0 从头开始,默认值
    #           1 累加
    #           0 从最后开始
    file_obj.seek(7,2)
    # 12345\r\n
    # 54321
    print(file_obj.read(5))
    # tell()当前读取的位置
    print('当前读取的位置->', file_obj.tell())
