import sys
import json

from work import match
from work import simplyParticiple
from work import synonym

sys.path.append('../')

import zmq
import time

# 服务器获得zmq上下文
# socket的类型是zmq。req
# tcp://*:5555地址要与客户端接口地址相同
# message是从前端接收到数据
print("hello!")
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
while True:
    # Wait for next request from client
    print('服务器开始工作了')
    date1 = socket.recv_json()
    print(date1)
    message = json.dumps(date1)
    print(message)
    #   str = simplyParticiple.participle(message)
    str = synonym.Result(message)
    print(type(str))
    print(str)
    # Do some 'work'
    time.sleep(0.5)  # Do some 'work'
    # Send reply back to client
    key = match.match(str)
    print(type(key))
    print(key)
    date2 = json.loads(key)
    print(date2)
    socket.send_json(date2)