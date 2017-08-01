from io import BufferedReader
def match (participle):
    "输入相应的关键字段，返回取到的md文件"
    dict = {}
    with open('keywords.txt', 'r') as file:
        for row in file:
            r = row.strip().split(' ')
            dict[r[0]] = r[1]
    if dict.get(participle) is not None:
        return dict[participle]
    else:
        return 'cant find answer'

