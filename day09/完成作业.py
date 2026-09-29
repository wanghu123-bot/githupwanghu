# 作业1：随机密码生成器
import random,string,json
nums=[1,2,3,4,5,6,7,8,9]
ps=random.sample(nums,4)
print(ps)
kl=list(string.ascii_letters+string.digits+string.punctuation)
ps=random.sample(nums+kl,9)
with open("data.json", "w", encoding="utf-8") as f:  # 打开文件用于写入
    json.dump(ps, f, ensure_ascii=False, indent=2)
print(ps)
# 作业2：文件信息查看器
import os

print(os.getcwd())
file=os.listdir(".")
print(file)
for i in file:
    fil=os.path.getsize('D:\\python-project\\PythonProject\\day09')
    print(fil,end='       ')
    lk=os.path.getmtime('D:\\python-project\\PythonProject\\day09')
    print(lk)