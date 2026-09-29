class Solution:
    def __init__(self,name,age,average):
        self.name=name
        self.age=age
        self.average=average
zhangsan=Solution("zhangsan",[78],85.0)
zhangsan.age.append(98)
zhangsan.age.append(85)
print(zhangsan.age)
lisi=Solution("lisi",[88],89.0)
lisi.age.append(90)
print(lisi.age)

dict={'《Python入门》':3 ,'《算法导论》':1}
with open('作业素材12','rt',encoding='utf-8') as f:
    lines=f.readlines()
    wr=input('请输入你的书籍和你所需要的数量')
    # wr=int(wr[1])
    ind=wr.split()
    wr=int(wr[1])
    for line in lines:
        if ind==1 and wr[0]=='《Python入门》':
            print('《Python入门》借出成功，剩余库存：2')
        if ind==2 and wr[0]=='《Python入门》':
            print('《Python入门》借出成功，剩余库存：1')
        if ind==3 and wr[0]=='《Python入门》':
            print('算法导论》借出成功，剩余库存：0')




