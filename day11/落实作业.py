def haod(age):
    if not type(age)==int:
        raise TypeError('类型不符合')
    if age<0 or age>150:
        raise TypeError('年龄不符合')
    return age


try:
    haod(180)
    print(haod(180))
except Exception as e:
    print(e)
# **自定义异常类**：
