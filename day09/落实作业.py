import datetime,random,string,json
from operator import length_hint


def op(length=12,use_upper=True,use_lower=True,use_splice=False):
    ch=''
    if use_upper:
        ch=ch+string.ascii_uppercase
    if use_lower:
        ch=ch+string.ascii_lowercase
    if use_splice:
        ch=ch+string.ascii_uppercase
        # print(list(ch))
        return list(ch)
ch=op(length=12,use_upper=True,use_lower=True,use_splice=True)
# kl=random.sample(ch,4)
# print(kl)
password=''
for i in range(12) :
    # kl=+i
    kl= random.choices(ch)
    password+=kl[0]
print(password)
with open("password.json", "w", encoding="utf-8") as f:  # 打开文件
    json.dump(kl, f, ensure_ascii=False, indent=2)  # 保存为JSON

print("密码已保存到password.json")                 # 提示保存成功


