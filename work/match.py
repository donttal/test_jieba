# coding=utf-8 ##以utf-8编码储存中文字符
from io import BufferedReader
import codecs

def match (participle):
    "输入相应的关键字段，返回取到的md文件"
    dict = {}
    with codecs.open('keywords.txt', 'r', 'utf-8') as file:
        for row in file:
            r = row.strip().split(' ')
            dict[r[0]] = r[1]

    for str in participle:
        if dict.get(str) is not None:
            return dict[str]

    return 'cant find answer'

# list = ['定义信息','信息定义']
# c = match(list)
# print(c)
