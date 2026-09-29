# try-except 语法详解
from day02.完成day01作业 import age

try:
    a=2
    print(a)
    B=[1,2,3]
    print(B[4])

except (NameError,IndexError)as e:
    print(e)
    print('重新尝试一下')
# except Exception as f:
    # print(B[4])
    # print(f)
else:
    print('文件读取成功')
finally:
    print('终于结束了')

# **raise主动抛异常**：
# 传参的应该都可以用函数来做
# def haod(age):
#     if type(age)==int:
#         raise TypeError('类型不符合')
#     if age<0 or age>150:
#         raise TypeError('年龄不符合')
#     return age
#
#
# try:
#     f(180)
#     print(f(180))
# except Exception as e:
#     print(e)
