# for
# for i in range(1,10,2):   # 从0到9
    # print(i)
# for j in range(10,1,-1):
#     print(j)
    # ** range左闭右开，步长正走负回头 **
    # ** 【遍历列表】 **
    # fruits=['苹果','香蕉','橘子']
    # for k in  fruits:
    #     print(k)
        # ** enumerate()
# enumerate(iterable, start=0)  iterable:要遍历的对象
# for i, fruit in enumerate(fruits):  # i是索引，fruit是元素值
#    print(f'第{i}个:{fruit}')
# 【zip()函数】
names=['张三','李四','王五']
ages=[18,19,20]
for name,age in zip(names,ages):
    print(f'{name}:{age}岁')
    print(name,age)
    # 也就是说平常打出来只能用逗号隔开,要想写出正规一点的要用f
    ### while循环与流程控制
     # 密码错误提示
    # while True:
    #     password=input('请输入密码:')
    #     if password=='123456':
    #         break
    #     print('错误')
# break
# "break是'紧急出口'，遇到break，整个循环立刻结束。"
# for i in range(10):
#     if i==4:
#        break
#     print(i)
# continue：跳过本次】
# "continue是'请假'，遇到continue，跳过本次循环的剩余代码，直接进入下一次。"
# for j in range(10):
#     if j==4:
#         continue
#     print(j)
# 第四环节：嵌套循环
for i in range(1,10):
    print(f'第一{i}')
    for j in range(8):
        print(f'第{j}',end='')
    print()# 内层一轮结束后换行
    print()# 外层每次结束后空一行