# 作业1：词频统计器
from pydoc import text

text=input('请输入一段英文:')
for char in '.,!;:\'()':
    text=text.replace(char,' ')
words=text.lower().split()
word_count={}
for word in words:
    if word != '':
         word_count[word]=word_count.get(word,0)+1

sorted_words=sorted(word_count.items(),key=lambda x:x[1],reverse=True)



