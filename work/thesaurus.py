import jieba
import jieba.analyse
from work import simplyParticiple
import jieba.posseg as pseg

jieba.load_userdict("dictionary.txt")

# 分词导入
a = '英国方面的东道主热情地接待了我们'
c = simplyParticiple.participle(a)
print(c)
# c为分词结果


#同义词最终要返回一个字符串
seperate_word = {}
dict1 = {}
i = 0
final_sentence = ""

file=open("same_word.txt")  #这是同义词库
lines=file.readlines()#读取全部内容
for line in lines:
    seperate_word[i]=line.split()  #同义词放入字典seperate_word中
    i=i+1

x1=len(lines)
for i in range(0, x1):
    x2 = {k: seperate_word[i][0] for k in seperate_word[i]}  # 这是同义词字典，不同键，相同值
    dict1 = dict(dict1, **x2)   #将多个字典合并为一个



for line3 in open("f:\\result3.txt"):
    line_2=line3.strip().split("/")    #这里存放取出来的问题
#print(line_2)



for word in line_2:


    if word in dict1:
        word=dict1[word]
        final_sentence+=word
    else:
        final_sentence+=word
print(final_sentence)   #这是结果
