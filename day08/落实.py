# def fut_name(a,b):
#    re = a+b
#    return re

# re=fut_name(1,2)
# print(re)
# 示例3】多返回值（本质是元组）
def fut_name(a,b):
    body=a/b
    height=a%b
    return body,height


# 方式1：用一个变量接收（得到元组）
result=fut_name(5,19)
print(result)
# 方式2：用多个变量接收（元组拆包）
n,v=fut_name(1,19)
print(f'商是{n},乘是{v}')
# 文档字符串示例
def fut_name(a,b):
    '''
    计算BMI的值
    参数:
    a:体重:(千克)
    b:身高(米)
    返回:
       BMI的值
       示例:
       fut_name(70.1.75)
       22.86
       '''
print(help(fut_name))

# 1. 位置参数
def func(a, b):
    func(1,2)


# 2. 默认参数
def func(a, b=10 ):
    print(a)
    print(b)
func(1,20)

# 可变位置参数 *args
def func(*name):
    print(name)
func(1,2,3,4,5)
print(type(func))
# 可变关键字参数 **kwargs
# def func(**typr):
#     print(type)
#     for key,value in typr.items():
#         print(key,value)
# func(a=1,b=2)


def func(a, b, c=10, *args, **kwargs):
    print(a,b,c,args,kwargs)


# 【调用示例1】只传必填参数
# func(1,2)
print(func(1,2),end='')
# 【调用示例2】传默认参数
print(func(1,2,3))
# 【调用示例3】传多余位置参数
print(func(1,2,3,4,5,6,7,8,9))
# 【调用示例4】传关键字参数
func(1,2,f=1,p=2)
# 【调用示例5】混合使用
print(func(1,2,3,4,5,6,7,8,9,g=10,o=18))# 尽量不要用,啊,吧,这些排在前面的字母作变量名
# 【调用示例6】用关键字参数跳过默认参数

# 可变默认参数陷阱示例
def add_item(item,items=None):
    if items is None:
        items=[]
    items.append(item)
    return items
print(add_item('pg'))
print(add_item('kl'))
# 第四环节：作用域
# 局部变量,在函数外不能调用
# def func1():
#     x=10# 报错了
# print(x)
    # 全局变量在函数里面可以获取全局变量得
y=10
def func2():
    print(y)
func2()
z=10
def func3():
    global z
    z=z+1
    print(z)
func3()
# 匿名函数
# 多用于使用一次的功能
print((lambda a,b:a+b)(1,2))
(lambda :print('haode'))()