# 字典
# 直接创建
docu={'name':'王胡呈','age':18}
# dict()函数创建
dcu=dict(name='whc',age=18)
# 从两个列表创建
age=[16,17,18]
name=['whc','whc','whc']
dic=dict(zip(name,age))
# 空字典
emp={}
# 查
student = {"name": "小明", "age": 18}
print(student['name'])
print(student.get('name'))
# 增
student['grade']='一年级'
print(student.get('grade'))
# 改
student['age']=19
print(student.get('age'))
# 删
del student['name']
print(student.get('name'))
# 遍历方法
student = {"name": "小明", "age": 18, "city": "北京"}
# 遍历键
for key in student.keys():
    print(key)
# 遍历值
for value in student.values():
    print(value)
# 遍历键值对（最常用！）
for key,value in student.items():
    print(key,value)
    # ** 字典合并 **：
# 方法1：update()（修改原字典）
dict1 = {"a": 1, "b": 2}                             # 第一个字典
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(dict1)
# 第四环节：集合
colors = {"红", "绿", "蓝"}
# 创建集合
# ku=[12,13,14]
# cu=set([12,13,14])
# print(cu)
# 添加元素到集合
colors.add('紫')
print(colors)
# 删除元素（不存在会报KeyError）
colors.remove('蓝')
print(colors)
# 有重复元素的列表
data = [1, 2, 2, 3, 3, 3, 4]
cu=list(set(data))
print(cu)

# 交集：两个集合都有的
a = {1, 2, 3, 4, 5}                                  # 集合A
b = {4, 5, 6, 7, 8}                                  # 集合B
print(a&b)
# 并集：两个集合所有的（去重）
print(a|b)
# 差集：a有但b没有的
print(a-b)
# 对称差集：只有一个集合有的（去掉共有的）
print(a^b)
