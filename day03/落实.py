# 字符串的数据类型：str
from gettext import find

# 需要使用单引号、双引号、三引号来定义

# 通过索引的方式，只能获取到字符串里面的某一个值，不能修改
# msg='hello'
# print(msg[1])
# 切片
# 注意:左闭右开    [起始值:终止值]步长默认为1
# 1.1步长如果是整数  空格也占一行
# print(msg[0:5])
# print(msg[0:5:2])
# 这个是提取一段连续性的多个元素
# klj='hello world'
# print(klj[0:2:1])
# 如果省略终止值,默认到字符串末尾结束
# print(klj[::])
# 如果什么也不打就会默认初始值也就是从第一个元素开始
# 1.2 步长是负数 也就是从左到右
# print(klj[::-1])
# print(klj[10::-1])
# dlrow olleh 两个值一样得
# 其实这里的10可以理解为索引 但是这是理解方面的,这里的[n::]n代表的是元素 代表的 是从n+1开始读起
# 同时也要注意顺序,如果顺序出错了,那么打印出来的就是空字符串
# 自己的感悟
# 其实你输出自变量的时候往往是可以不用带括号基本只有函数才带括号
# 1.2 常见的函数
# a:len
# print(len(klj))
# len 它是用来计算字符串的长度,同样空格也会占一行,这里的klj有10个元素但有一个空格就会被解读为11
# b:in not in 返回类型-布尔类型
# print('zhangsan' in 'zhangsan is sb')
# print('zhangsan' not in 'zhangsan is sb')
# 1.3增删改查的函数
# 方式一: + 字符串拼接
# print('zhangsan' +''+'is'+''+"dabos")
# 空格也要单独打出来
# 方式二:formate()
# 一般是{}.formate()的方式来使用
# print('my name is {}'.format('zhangsan'))
# 参数一般要顺序一致
# print('my name is {},my age is {}'.format('zhangsan',18))
# 同样也可以用索引
# print('my name is {1},my age is {0}'.format(18,'zhangsan'))# 做一个大致的了解
# print('my name is {name}'.format(name='zhangsan'))
# 方式三:join()
# str1='真正的勇士'
# str2='敢于直面惨淡的人生'
# str3='敢于正视淋漓的鲜血'
# print(','.join([str1,str2,str3]))
# ''这个就相当set的作用,也就是在这些句子中插入其他的元素
# 1.4 删 主要是del
# del=删除的内容   eg:  del name
# 1.5  修改
# 方式一:给字符串重新赋值
# 方式二:字符串字母变成大写(upper())和变成小写(lower())这里都是一起变成大写
# mnb='abc'
# result=mnb.upper()
# print(result)
# 方式三:把第一个字母换成大写
# bh=msg.capitalize()
# print(bh)  # Abc
# 方式四:每个单词的首字母进行大写转换 title()
# qaz='hello world'
# knb=qaz.title()
# print(knb) # Hello World
# 方式五:将一个字符串,拆分成多个字符串
# bhu='helloworldpython'
# h=bhu.split(';')
# print(h) # [hello world python]
# 它这里面的括号就是在把这些单词拆分的时候用什么形式
# 方式六:去掉字符串左右两边的字符 strip()
# hhh = '   huahua   '
# bh=hhh.strip()  # huahua
# print(bh)/
# 方式七:字符串的替换
# shj='kl world'
# op=shj.replace('kl','hi')
# print(op)
# 替换所有匹配的字符串
# msg='不吃香菜  真爱粉 不吃香菜 两年半 不吃香菜'
# res=msg.replace('不吃香菜','好的' ,2)
# print(res)
# 1.6 查
msg = 'hello dahai is dsb dahai'
# print(msg.find(''))  X
# print(msg.index('dahai'))
# 与find的区别就是find只要有字母就可以运行而index就是完整的单词
# 并且如果没找到find会打-1而index会打报错

# 比较开头的元素是否相同 startswith()
# 字母也可以#
# 比较结尾的元素是否相同 endswith()

# 返回布尔类型
# print(msg.count('dahai'))# 出现的次数
# print(msg.startswith('he'))
# print(msg.endswith('ai'))
# 字符串的转义

# 常用的  \n     \t

# \n 换行符
# print('hello \n python')#hello
                            # python
print('hell0 \t python')
# 只有当前面的单词是完整的时候才会独占一行
# print('a\t')    # 代表3个空格字母也算
# 不让它转义
print(r'hello \n python \t')   # hello \n python \t
# 这里的r其实也相当于read

# 这就用到了占位符，常用的：%s  %d
name = input("请输入你的名字")
# age=input('年龄')
print('my name is %s'%name)
# 只是输出一个值的话，直接放到%后面就可以了
# 多个值的话，直接放到%后面,有括号()
print('my name is %s,my name is %s'%(name,10))
