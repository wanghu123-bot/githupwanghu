# 基本运算+-*/ // % **
# 1.1
from os import name

a=10
b=3
# print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)# 留整数
print(a%b) # 取余
print(a**b)# 幂次方
# 变量的命名规则：见名知意

# 变量名：区分大小写的
# 大小写 不一样也会有问题
# name = "zhangsan"

# Name = "zhangsi"

# 常量：不能更改的数据（告诉别人不能改）

# 常量一般所有字母都大写

# NAME = '张三'

# 1.2
# name='wanghu'
# print(name)
# print(id(name))# id() # 记录变量在内存中的位置、地址
# print(type(name)) # id() -- 记录变量在内存中的位置、地址
#
# age=input(',,,')
# print(age)
# print(type(age))
# 1.3
# 如果是一个字符串 -- 加上引号

# print("你好，python!")

# 如果是一个纯数字 -- 不加引号

# print(123)   # 123
# print('姓名:','张三')
# print('北京','上海','广州',sep='u')
# print('北京','上海','广州',end='好')
# C:/Users/Windows/Downloads/PyCharm 2025.2.5/PyCharm 2025.2.5/pycharmActivate/Activation_Code
# D:\\xz\\专门学习python
# name='张三'
# age=20
# print(f'姓名:{name},年龄:{age}')
# 1.4
# 数字类型 -- int(整数)

# 作用：年龄 等级 QQ号 各种号码

# age = 18

# print(type(age))  # <class 'int'>

# 浮点型 -- float(带有小数点)

# 作用：记录身高、体重weight、薪资
# 1.5
# 如果字符串的外面用的是单引号，那么里面就使用双引号

# msg2 = '她说"很高兴认识你"'
# msg2 = "她说`很高兴认识你`"
# print(msg2)
# 如何获取到字符串里面的某一个字符

#   索引 -- 字符串里面的第一个字符，是从索引0开始的

# print(name[0])   # a

# name=(1,2,3,4,5,6)
'''
0  1  2  3  4  5  6  （从左到右）
a  b  c  d  e  f  g  
-7 -6 -5 -4 -3 -2 -1（从右到左）
'''
# print(name[-1])
# 字符串不支持，通过索引的方式来修改其中的某一个元素
# 1.6 bool
# input(2<1)
# 1.6
# 浮点数 → 整数 -- 直接截断小数部分（不是四舍五入！）
# print(int(3.14))
# 字符串 → 整数
print(int('42'))
# 整数 → 浮点数
print(float(10))