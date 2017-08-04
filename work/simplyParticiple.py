# coding=utf-8 ##以utf-8编码储存中文字符
from __future__ import print_function, unicode_literals
import sys
sys.path.append("../")
import jieba
jieba.load_userdict("dictionary.txt")
import jieba.posseg as pseg

import jieba.analyse
from optparse import OptionParser

# 新增关键词
jieba.add_word('信息定义')


USAGE = "usage:    python extract_tags_with_weight.py [file name] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()

# 设定了权重前十的显示出来
if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

jieba.analyse.set_stop_words("stop_words.txt")  # 关键词提取所使用停止词（Stop Words）

def participle (content):
    tags = jieba.analyse.extract_tags(content, topK=topK)


    print(tags)
    str = '/'.join(tags)
    return str
