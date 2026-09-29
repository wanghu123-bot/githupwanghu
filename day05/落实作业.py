# 5.1 单分支 if
# age=11
# if age>=18:
#     print('你已经成年,银行卡')
# 5.2 双分支 if-else
# sex='male'
# if sex=='male':
#      print('你好')
# else:
#       print('走吧')
# 5.3 多分支 if-elif-else
# scores=[88,76,90]
# if scores[1]>=90 and scores[1]<=100:
#     print('优秀')
# elif scores[0]>=80 and scores[0]<=90:
#     print('不错')
# elif scores[1]>=60 and scores[1]<=70:
#     print('加油')
# else:
#     print('差劲')
# 5.4 条件嵌套
# is_login = False                            # 是否登录
# is_admin = False
# has_permission = False
# if is_login:
#     if is_admin:
#         print('admin')
#     else:
#         print('user')
# else:
#     print('login fail')
# else的就近原则 以及缩进对同一个if else缩进程度要一样

# 5.5 扁平化技巧（卫语句）
# if not is_login :
#     print("请先登录")
# elif not is_admin :
#     print('需要管理员权限')
# elif not has_permission :
#     print('权限不足')
# else:
#     print('欢迎')
# 5.6 三元表达式  # 代码简化
# age=22
# result='成年' if age>=18 else '不行'
# print(result)
# 5.7 elif vs 多个if（重点！）
score=88
if score>90:
    print('很棒')
if score>85:
    print('可以')
if score>80:
    print('好的')
#     这种情况不行,因为if是独立的,不受上一个影响,所以都可以打出来
# 故建议使用 elif 这个只有等到上一个执行完了,才会执行

# 5.8 真值测试
'''- 数字：`0`、`0.0`、`0j`
- 字符串：`""`
- 容器：`[]`、`()`、`{}`、`set()`
- 特殊值：`None`、`False`
- 其他所有值都视为True'''
# eg:
if 0:
    print('h')
if 0.0:
    print('hao')
if []:
    print('hao')
if 0:
    print('hao')
if 1.0:
    print('hao')


# 代码简化