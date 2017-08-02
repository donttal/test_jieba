import zmq
import json

context = zmq.Context()
# Socket to talk to server
print("开始连接服务器")
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:5555")
# Do 10 requests, waiting each time for a response
for request in range (1,10):
    print("Sending request ", request,"...")
    content = '信息的定义是什么'
    data1 = json.dumps(content)
    socket.send_json(data1)
    # Get the reply.
    message = socket.recv_json()
    # print(type(message))
    # print(message)
    data2 = json.loads(message)
    print('Received reply ', message)