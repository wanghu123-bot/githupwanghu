# 创建列表
'''
nums=[1,2,3,4,5]
src=[1,'好的',True,]# 注意：虽然可以混用类型，但实际开发中不建议这样做
empty=[]
print(empty)

range_list=list(range(1,10))
print(range_list)
'''
from itertools import count
from pydoc import text
from turtledemo import colormixer

# 正索引访问
fruits=['苹果','香蕉','橘子']
# print(fruits[0])
# 负索引访问
# print(fruits[-1])
# 检查元素是否存在
# print('苹果'in fruits)a
'''
# 可以直接再赋值后面+.函数()
# 获取元素的位置（index方法）
# print(fruits.index('苹果'))
# 统计元素出现次数（count方法）
# print(fruits.count('苹果'))
# append
# print(fruits.append('梨子'))
# print(fruits.append(['西瓜','火龙果']))
# insert
# print(fruits.insert(1,'往往'))
# fruits.insert(100,'苹果')
# print(fruits)
# extend
# more_fruits=['橘子','桃子']
# fruits.extend(more_fruits)
# print(fruits)
# fruits.extend(('好的','究竟'))
# print(fruits)
remove
nums.remove(2)
print(nums)
nums.remove(2)
print(nums)
# sort
nums = [3, 1, 4, 1, 5, 9, 2, 6] 
nums.sort()
print(nums)
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()
print(nums)

nums.sort(reverse=True) # 降序排序（从大到小）
print(nums)
names = ["张三", "欧阳锋", "李四", "司马光", "王"]
names.sort()
print(names)
 append insert extend remove pop del clear sort 只能在原地修改print不会返回值'''
'''
# 省略起始索引
# print(fruits[:3])
# 省略结束索引
# print(fruits[1::])
# 带步长的切片：list[start:stop:step]
# print(fruits[::2])
# 负数切片
# print(fruits[-1::])
# 反转列表（步长为-1）
# print(fruits[::-1])
'''
# 删除
nums = [1, 2, 3, 2, 4, 2, 5]
# pop

# last=nums.pop()
# print(last)
# # 如果给上面来命名的话就会返回它所删除的元素
# nums.pop(0)
# print(nums)
# del

# del nums[0]
# print(nums)
# del nums
# print(nums)
# del nums[2:4]
# print(nums)
# clear

# nums.clear()
# print(nums)
# 列表
# fruits[1:2]=['芒果,香蕉']
# print(fruits)

# classroom = [
#     ["张三", 18, "北京"],               # 第1行：姓名、年龄、城市
#     ["李四", 20, "上海"],               # 第2行
#     ["王五", 19, "广州"],               # 第3行
# ]
# 访问元素
# print(classroom[0])
# 修改嵌套元素
# classroom[0][2]=19
# print(classroom)
# 添加新行
# classroom.append(['好的',20])
# print(classroom)

'''
不修改原列表,需要建立一个新的表格 sorted()

 sorted 元组和列表的方法是一样的
# nums = [3, 1, 4, 1, 5, 9, 2, 6]
# new_nums=sorted(nums)
# print(new_nums)
# 
# text=('python')
# new_text=sorted(text)
# print(new_text)
'''
# print(sum(nums))
# 元组  不可修改,只能重新创建一个
# 方法一：用圆括号创建（最常用）
color=('红色','蓝色')
print(color)

# 方法二：创建单元素元组（重要！）
color=('红色',)
print(type(color))

# 方法三：省略括号创建
color='红色','蓝色'
# 方法四：创建空元组
# nums=()
# print(type(nums))
# 元组索引和切片（与列表相同）
nums=(1,2,3,4,5,6,7,8)
print(nums[:7])
# 元组长度
print(len(nums))
# 检查元素是否存在
print(3 in nums)
print(nums.count(3))
print(nums.index(3))

# 元组可以改变的情况
new_nums=nums+('48',)
print(new_nums)

mixed = (1, 2, [3, 4])
print(mixed)
mixed[2].append(5)
print(mixed)













