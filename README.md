启动：
```
./run.sh
```

输入密码：1234
节点开启端口9000提供gRPC服务。

目前还没有提供sdk。

```
pip install -r requirements.txt
```

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./wallet.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./common.proto
```