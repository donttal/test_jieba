import jieba.analyse
import codecs,sys
import itertools

from io import BufferedReader
from work import simplyParticiple

def Synonym():  #同义词函数
    seperate_word = {}
    dict1={}
    i=0
    file = codecs.open("same_word.txt","r","utf-8") # 这是同义词库
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

def _synonym(txt):
    #final_sentence=""
    list_prim=[]
    line = simplyParticiple. participle(txt)
    print(line)
    print(type(line))
    line_2 =line.split("/")
   # line_2=Cut_Word(txt).split("/")
    print(line_2)
    dict1=Synonym()
    #print(dict1)
    for word in line_2:
        if word in dict1:
            word = dict1[word]
            list_prim.append(word)
        else:
            list_prim.append(word)
    return list_prim

def getkeyword(list_A,list_B):   #getkeyword 的作为是从分词去停用词同义词过后的原始关键词中于关键词列表进行匹配，找出最后的关键词
    list_C=[]
    for each_itema in list_A:
        for item in list_B:
            if(each_itema==item):
                list_C.append(item)
                break
    return list_C


# def exchange(a,b):
#     temp=a
#     a=b
#     b=temp
#
# def fullpermutation(the_list,start,end,list_final):    #fullPermutation用于将关键词组合全排列得到字符串最后将字符串保存到list_final中
#     if(start==end):
#         list_final.append(combination(the_list))
#     else:
#         for item in range(start,end):
#             exchange(the_list[start],item)
#             fullpermutation(the_list,start+1,end,list_final)
#             exchange(the_list[start], item)
#     return list_final
#
def combination(the_list):
    str=""
    for each_item in the_list:
        str += each_item
    return str



fp=open("final_keyword.txt",encoding="utf_8")
list_keyword=[]
for lines in fp.readlines():
    lines=lines.split()
    list_keyword=list_keyword+lines
fp.close()


def result(txt):#list_final保存全排列后字符串,list_prim保存与知识点关键词匹配后的关键词，list_mid保存全排列后关键词列表
    list_final=[]
    list_prim=getkeyword(set(_synonym(txt)),list_keyword)
    list_mid=(list(itertools.permutations(list_prim, len(list_prim))))
    for item in list_mid:
        list_final.append(combination(item))
    return  list_final

list_test=result("信息的定义是什么")
for str in list_test:
    print(str)