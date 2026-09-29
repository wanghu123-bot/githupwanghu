# os模块 — 操作系统接口
# 当前目录

import os
# 打开电脑自带的系统功能
# os.system('start cmd')
# 获取当前文件的路径目录
print(os.getcwd())
# D:\python-project\PythonProject\day09
# __file__
print(__file__)
# 用于表示当前模块的路径
# D:\python-project\PythonProject\day09\os模块.py
# 创建目录
# os.makedirs('test')
# 删除目录
# os.rmdir('test')
# 对目录重命名
# os.rename('test','test2')
# 判断文件是否存在
#
# 获取当前文件所在的目录
print(os.path.dirname(__file__))
print(os.path.basename(__file__))