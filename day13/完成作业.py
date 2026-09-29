# import math
# class Shape:
#     # import math
#     op=math.pi
#     @property
#     def area(self):
#         radius=int(input('请输入半径'))
#         return f'面积是:{radius*radius},周长:{2*math.pi*radius}'
#     @property
#     def perimeter(self):
#         length=int(input('请输入你的长度'))
#         width=int(input('请输入你的宽度'))
#         return f'面积:{length*width},周长:{2*length*width}'
# class Circle(Shape):
#     nums=Shape()
#     print(nums.area)
#     # print(nums.area())
# class Rectangle (Shape):
#      num=Shape()
#      # print(num.perimeter())
#      print(num.perimeter)
class Animal :
    def __init__(self,name):
        self.name=name
    def speak (self):
        pass
class Dog(Animal):
    def speak (self):
        print(f'{self.name}旺旺')

class Cat(Animal):
    def speak (self):
        print(f'{self.name}喵喵喵！')
class Bird(Animal):
    def speak (self):
        print(f'{self.name}叽叽喳喳！')
animals=[Dog('旺财')
         ,Cat('咪咪'),
         Bird('小黄')]
for animal in animals:
    animal.speak()