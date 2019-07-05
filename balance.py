# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
from api import wallet_pb2, wallet_pb2_grpc
import base58

_HOST = '68.183.72.212' #如果你本地没有起来jura节点，可以用这个服务器上的测试地址。
# _HOST = 'localhost' #使用本机的测试JURA
_PORT = '9000'


address = 'RW8VbQPAWpUJH3dtDDJPRaVTudXkgpv8LPAMe1kPTqwCKQ92BTArg9hxpYLwWeeKYzoxt7jdgzXRYtrxJPTDij5Y'
account = base58.b58decode(address)

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道
    client = wallet_pb2_grpc.WalletServiceStub(channel=conn)   # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    response = client.CheckBalance(wallet_pb2.CheckBalanceRequest(account=account))   # 返回的结果就是proto中定义的类
    print(response)


if __name__ == '__main__':
    run()