from day07.落实 import student, name, age


# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def work(self):
#         print(f'{self.name} 正在工作中...')
# class Student(Employee):
#     def __init__(self,name,age,salary):
#         super().__init__(name,age,salary)
# p1=Student('zhangsan',18,99)
# p1.work()
# 父类
# class Employee:
#     school='蓝心学院'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# # 子类
# class Student(Employee):
#     def syu(self):
#         print('%s啥阴'%self.name)
# f=Student('张三',29)
# f.syu()
# 总结一下:对于继承这总样式可以直接调用父式的方法包括里面的函数,如果你是要再创造一个新的函数和参数就要使用上面那个super()
# class Employee:
#     def __int__(self,name,age,num):
#       self.name=name
#       self.age=age
#       self.num=num
#     print('haode')
# class Student(Employee):
#     def __init__(self,name,age,num,salary):
#         super().__int__(name,age,num)
#         self.salary=salary
#     def printinfo(self):
#         print('%s啥阴'%self.name)
# op=Student('张三',19,88,99)
# op.printinfo()
# 这总是对于要写多个参数的时候,拿父式的参数来写,如果不用则可以直接继承并带这父式的参数
# 父类和子类中,各有一个同名的函数,并且这两个函数的参数不同,在这种情况下使用super()

# 一个父类多个子类 子类里面也可以套用子类也可以套用父类
# class Employee:
#      def __int__(self,name,age,num):
#        self.name=name
#        self.age=age
#        self.num=num
#      def op(self):
#          print('%s18岁'%self.name)
# class Student(Employee):
#      def __init__(self,name,age,num,salary):
#          super().__int__(name,age,num)
#          self.salary=salary
#      def printinfo(self):
#          print('%s啥阴'%self.name)
# class Nmub (Student):
#      def play(self):
#          print('%s厉害'%self.name)
# p=Student('张三',17,191,99)
# p.printinfo()
# s=Nmub('李四',18,99,99)
# s.play()
# 一个子类多个父类 会执行父类
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass
# print(D.__mro__)
# 组合



# 多态









# 封装
# 并不是父式的东西并不全部子类可以继承
# class Guio:
#     x=111
#     __y=777
#     def __int__(self ,name ,age):
#         self.__name=name
#         self.age=age
#     def __uu(self):
#         print('jjjj')
#     def __del__(self):
#         print('dddd')
#     def vv(self):
#         print(self.__y,self.__name)
#         self.__uu()
# # print(Foo.x)
# # print(Foo.__y)
# f1=Guio('张三',18)
# proprety
# class Student:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     @property
#     def vv(self):
#         print('%s阴间'%self.__name,self.__age)
# p1=Student('zhangsan',18)
# print(p1.vv)
class Shape:
    def area(self):
        radius=input('请输入半径')
        return radius * radius
    def perimeter(self):
        length=input('请输入你的长度')
        width=input('请输入你的宽度')
        return '面积是length*width'
class Circle(Shape):
    nums=Shape()

