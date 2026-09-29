# 5.1 import语句
# import random
# import time
# print('OK')
# sp=time.sleep(3)
# print('haode')
import random
# 从模块里面导入部分功能 from  import
# from random import randint,choice
# ps=randint(0,100)
# print(ps)
# 导入的如果是模块的话就需要写模块名,如果是功能名的话from import 的话就不用写直接写函数名
# 5.3 from...import *语句
# from random import *
# num=randint
# print(num(1,100))
# 5.4 as别名
# import random as r
# ml=r.randint(0,99)
# print(ml)
# 6.1 random模块 — 随机数
import random
from random import shuffle

# 生成随机数
# print(random.random(0,1))
# print(random.randint(0,100))
# 输出: 1.5到3.5之间的随机
print(random.uniform(0,100))
# 随机选择
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(random.choice(fruits))
# 随机抽样（不重复）
nums=list(range(10))
ps=random.sample(nums,3)
print(ps)
op=[1,2,3,4,5]
print(shuffle(op))
print(op)
# op=[1,2,3,4,5]
print(op)
from 调试代码 import *
# res=add(1,2)
# print(res)
# 6.2 datetime模块 — 日期时间
# 获取当前时间
