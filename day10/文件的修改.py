# 先读后修改
with open ('完成进度2.py','rt',encoding='utf-8')as f:
    date=f.read()
with open ('完成进度2.py','wt',encoding='utf-8')as f:
     f.write(date.replace('haode','等到'))