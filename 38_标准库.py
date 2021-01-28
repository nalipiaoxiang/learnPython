# 标准库 开箱即用
import sys
print(sys) #<module 'sys' (built-in)>
# sys.argv
# 获取执行代码时,命令行中所包含的参数
# 返回列表
print(sys.argv)

# modules
# 获取程序加载的所有的模块
print(sys.modules)

# pprint 模块
import pprint
pprint.pprint(sys.modules)

# sys.path
# 他是一个列表,列表中保存的是模块的搜索路径
pprint.pprint(sys.path)

# sys.platform 运行平台
# AIX 'aix'
# Linux 'linux'
# Windows 'win32'
# Windows/Cygwin 'cygwin'
# macOS 'darwin'
print(sys.platform)

# sys.exit() 程序结束
# sys.exit('测序异常结束')

# os 系统信息
import os
print(os)

# os.environ
pprint.pprint(os.environ['path'])

# os.system() 可以执行操作系统的命令
os.system('dir')
# os.system('notepad')

# 当前补录的文件
# 可以指定目录 参数
pprint.pprint(os.listdir())
pprint.pprint(os.listdir('C:/'))

# os.getcwd() 当前目录
print(os.getcwd())

# 切换目录 cd
os.chdir('..')
print(os.getcwd())

# 创建目录
# os.mkdir('aaa')
pprint.pprint(os.listdir())

#删除目录
# os.rmdir('aaa')

# open('aa.txt','w')

#删除文件
# os.remove('aa.txt')

#重命名 也可以剪切
# os.rename('旧名字','新名字')
