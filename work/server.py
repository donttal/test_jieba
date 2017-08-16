# coding=utf-8 ##以utf-8编码储存中文字符
import sys
import json

from work import match
from work import synonym

sys.path.append('../')

import zmq
import time

# 服务器获得zmq上下文
# socket的类型是zmq。req
# tcp://*:5555地址要与客户端接口地址相同
# message是从前端接收到数据
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
while True:
    # Wait for next request from client
    print('服务器开始工作了')
    # date1 = socket.recv_json()
    date1 = socket.recv()
    # print(date1)
    # message = json.loads(date1)
    message = date1.decode(encoding='utf-8')
    print(message)
    print(type(message))
    #   str = simplyParticiple.participle(message)
    list_final = synonym.result(message)
    print(list_final)
    # key = match.match(list_final)
    # print(key)
    # print(type(key))
    # socket.send_json(key)
    key = json.dumps(list_final)
    socket.send_json(key)

    
