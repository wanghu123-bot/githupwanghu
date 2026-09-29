from logging import INFO

dit={'INFO':0,'WARNING':0,'ERROR':0,'CRITICAL':0}
print('日志报告分析:')
print('-------------------------------------')
print('-------------------------------------')
with open ('日志文件.py', 'rt',encoding='utf-8') as f:
    # date=f.read()
    print('统计概括:')
    print('-----------------------------------')
    for i in f:
        if 'INFO' in i:
           dit['INFO']=dit['INFO']+1
      # print(dit['INFO'])
        if'WARNING' in i:
            dit['WARNING']=dit['WARNING']+1
        if'ERROR' in i:
            dit['ERROR']=dit['ERROR']+1
        nums=dit['INFO']+dit['WARNING']+dit['ERROR']
    a=dit['INFO']/nums*100
    a=round(a,1)
    b=dit['WARNING']/nums*100
    b=round(b,1)
    c=dit['ERROR']/nums*100
    c=round(c,1)
    print(a)
    print(b)
    print(c)
    print('级别统计:')
    print(f'INFO {dit['INFO']}条 ({a}%)')
    print(f'WARNING,{dit['WARNING']}条 ({b}%)')
    print(f'ERROR,{dit['ERROR']}条 ({c}%)')
    print('统计概括:')
    print(f'{nums}条')







