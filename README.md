启动：
```
./run.sh
```

输入密码：1234
节点开启端口9000提供gRPC服务。

目前还没有提供sdk。

```
sudo apt install gyp
sudo apt install protobuf-compiler
```

```
python -m pip install grpcio
python -m pip install grpcio-tools
```

```
pip install -r requirements.txt
```

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./wallet.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./common.proto
```


```
pip freeze > requirements.txt
```