import jieba.analyse
import codecs,sys
from work import simplyParticiple

def Synonym():  #同义词函数
    seperate_word = {}
    dict1={}
    i=0
    file = codecs.open("same_word.txt","r","utf-8")  # 这是同义词库
    lines = file.readlines()  # 读取全部内容
    for line in lines:
        seperate_word[i] = line.split()  # 同义词放入字典seperate_word中
        i = i + 1
    x1 = len(lines)
    for i in range(0, x1):
        x2 = {k: seperate_word[i][0] for k in seperate_word[i]}  # 这是同义词字典，不同键，相同值
        dict1 = dict(dict1, **x2)  # 将多个字典合并为一个
    return dict1


def  Cut_Word(txt):    #txt是要分的问题,这个函数用于分词    如果已有分词函数，请把txt1=txt.strip() 加上去，目的用于去除问题结尾的空格
    txt1=txt.strip()   #加strip（）函数用于去除问题结尾的空格
    txt2 = jieba.cut(txt1)
    f2='/'.join(txt2)
    return f2

def Result(txt):
    final_sentence=""
    line_2 =simplyParticiple. participle(txt).split("/")
   # line_2=Cut_Word(txt).split("/")
    print(line_2)
    dict1=Synonym()
    #print(dict1)
    for word in line_2:
        if word in dict1:
            word = dict1[word]
            final_sentence += word
        else:
            final_sentence += word
    return final_sentence
