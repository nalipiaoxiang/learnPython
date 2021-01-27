# 在一个模块中引入外部模块
# ① import 模块名
# ② import 模块名 as 模块别名
import test_module
import test_module as test
print(test_module)
print(test)

print(test.__name__)

print(__name__)

# 访问模块属性 模块名.变量
print(test.a)
print(test.b)

# 访问模块方法
test.test1()
test.test2()

p = test.Person()
print(p)
print(p.name)

# 也可以只引入模块中的部分内容
# 语法 from 模块名 import 变量,变量,...
from test_module import Person

import test_package
print(test_package)

print(test_package.a)
print(test_package.b)
test_package.test()

# __pycache__ 是模块缓存文件