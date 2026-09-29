import time
res=time.time()
# time 获取当前时间截,返回的 是float
print(res)
# local time
op=time.localtime()
print(op)
print(f'星期{op[6]+1}')
st=time.strftime('%Y-%m-%d %X',time.localtime())
print(st)
kl=time.strptime('2020/01/01','%Y/%m/%d')
print(kl)