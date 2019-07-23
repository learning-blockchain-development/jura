# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
import wallet_pb2, wallet_pb2_grpc
import base58
import config
_HOST = config.getHost()
_PORT = config.getPort()



conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道
client = wallet_pb2_grpc.WalletServiceStub(channel=conn)   # 客户端使用Stub类发送请求,参数为频道,为了绑定链接

def newaccounts():
    print ("hello")

def getbalance(address):
    account = base58.b58decode(address)
    response = client.CheckBalance(wallet_pb2.CheckBalanceRequest(account=account))   # 返回的结果就是proto中定义的类
    return response

def tx(from_address,to_address,amount,privatekey):
    return true