class Person:
# 先调用属性(变量)
    name='张三'
    age=10
    # 方法
    def course(self):
        print('上课')
        return 11111
# 类的调用
print(Person.name)
# 没有创建对象 这里的Person这个就是类的变量名
print(Person.course) # 拿到的是内从地址
Person.course(100)#上课
# 添加类的新属性
Person.play='haode'
print(Person.__dict__)
# 删除属性
del Person.play
print(Person.__dict__)
# 生成对象 可以通过对象,获取类里面属性的值
t1=Person()
t2=Person()
print(t1.name)
print(t1.course())# 这个就是启动那个函数
print(t1.course)# 获取地址
#如果是类来操作这个方法就需要传递参数,反之对象则不需要
print(Person.course(100))
print(t1.course)
# 通过对象去修改类里面的函数值
t1.name='李四'
print(t1.name)
print(t1.__dict__)
# 删除对象属性
del t1.name
print(t1.__dict__)
#
class Teacher:
    school='蓝星学院'
    xxx='我是类的属性'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def teach(self,name):
        print('%s上课'%name)
# t3=Teacher()
# t3.xxx='ok'
# print(t3.xxx)
''' 如果对象和类里面都有相同的属性,如果你想要调用同样的属性,对象在调用时会优先看
首先会看对象里面有没有这个值,如果没有就去类里面找这个属性'''
# _int_方法
dahai=Teacher('张三',10)
print(dahai.name)
# dahai=Teacher()
dahai.name='莉莉'
dahai.teach('dahai')



