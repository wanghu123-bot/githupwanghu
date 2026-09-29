# 只读模式:rt(默认)
# with open('完成进度2.py','rt',encoding='utf-8') as f:
# res=f.read()
    # print(res)
# 判断rt能不能读
#     print(f.readable())
# 判断能不能写
#     print(f.writable())
# 写的模式 wt
# with open('完成进度2.py','wt',encoding='utf-8') as f:
#      op=f.write('haode')
# 追加模式 at
# with open('完成进度2.py','at',encoding='utf-8') as f:
#     kl=f.write('好的\n')
# rb 二进制读的模式(只用于读的模式)
# with open('1.png','rb') as f:
#     date=f.read()
#     print(date)
# wb 二进制写模式(表示二进制打开一个文件只写)
# with open('2.png',"wb")as f:
#     f2.write(date)
with open('D:\\python-project\\PythonProject\\day10\\完成进度','rt') as f:
    date=f.read()
    print(date)
with open('.\\完成进度2.py', 'rt') as f:
    date2=f.read()
    print(date2)