# __str__():在对象打印的时候会自动触发,可以用来定义对象被打印时的输出信息,魔法方法
class Peple:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "name:%s,age:%s"%(self.name,self.age)
obj=Peple('大海',19)
print(obj)
# __call__():在对象被调用的时候会自动触发该方法
class Teacher:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print(self.name)
bh=Teacher('大海',19)
bh(11111,34,a=3,b=4)
# args接住，打包成元组，所以打印出来是(11111, 34)
# 全部被**kwargs接住，打包成字典，所以打印出来是{'a': 3, 'b': 4}
# 闭包函数 1
def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function(6)
result=outer_function(7)
print(result)

def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function
result=outer_function(7)
print(result(6))
# 装饰器
# 装饰器是Python里非常实用的高级特性
# ，核心作用是在不修改原函数代码、不改变原函数调用方式的前提下
# ，动态给函数增加额外功能，完美符合软件工程里的「开放封闭原则」——对扩展开放，
# 对修改封闭。不能修改装饰器的源代码,和调用方式
def func():
    print('hello')
    func1()
def func1():
    print('world')
func()
#如果给原来的功能添加一个功能而不修改原来的代码需要使用的是装饰器, 也需要满足闭包的方式
# def log(func):
# 迭代器  将列表对象转换为迭代器对象
my_list=[10,20,30,40]
my_iter=iter(my_list)
print(next(my_iter))
print(next(my_iter))
# 结合for循环一起使用
for i in my_iter:
    print(i,end="")
# 迭代器只能迭代迭代器对象
# 生成器
# 使用了yield 定义的函数,就是生成器函数
def number_bgf():
    for i in range(4):
        yield i
Num=number_bgf()
for y in Num:
    print(y)






