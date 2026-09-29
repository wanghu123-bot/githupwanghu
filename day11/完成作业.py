# 作业1：读取文件
import os
try:
    def file():
        if os.path.exists('完成作业.py'):
             with open('文件.py','r',encoding='utf-8') as f:
                f=f.read()
                print(f)
except Exception as e:
    print('请重新尝试')
finally:
    print('已关闭')
# 作业2：写函数验证年龄
class nums:
     def file2(age):
         try:
             if not type(age)==int:
                raise TypeError('类型错误')
             if age<0 or age>100:
                raise ValueError('数字太大了')
         except (TypeError,ValueError) as e:
             input(e)
             input('请重新尝试一下')
         else:
             print('注册成功')
     file2(30)



