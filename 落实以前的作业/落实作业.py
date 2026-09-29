# 当你要从一堆数据里面去出某个值来计数时 思路大概就是
# 第一步:创建一个 例如 stats = {
#         "INFO": 0,
#         "WARNING": 0,
#         "ERROR": 0,
#         "其他": 0
#     }
# 第二步:在导入对应的文本 先with open(log_file, "w", encoding="utf-8") as f:  # w模式创建文件
# 再把对应的文本写进去
# 第三步 用if 判断来解决从这个文本来计数
# if "[INFO]" in line:        # 检查是否包含INFO
#             stats["INFO"] += 1      # INFO计数+1
#         elif "[WARNING]" in line:   # 检查是否包含WARNING
#             stats["WARNING"] += 1   # WARNING计数+1
#         elif "[ERROR]" in line:     # 检查是否包含ERROR
#             stats["ERROR"] += 1     # ERROR计数+1
#             errors.append((line_num, line))  # 记录ERROR详情
# 第四步 通过 print 运算来得出结果
# 例如  nums=dit['INFO']+dit['WARNING']+dit['ERROR'
# 然后后面就是用print(f'')格式化输出就行
# 补充如果想要的完美一些可以判断这个文件存不存在往往放在第一步