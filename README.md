```commandline
python -m grpc_tools.protoc -I./proto --python_out=./app/stubs --grpc_python_out=./app/stubs ./proto/customer_service.proto

```
## Swagger

```commandline
protoc -I C:/Projects/us-survey-api/proto -I C:/Projects/us-survey-api/googleapis --go_out=./swagger --go-grpc_out=./swagger --grpc-gateway_out=./swagger --openapiv2_out=./swagger C:/Projects/us-survey-api/proto/customer_service.proto
```
from . import customer_service_pb2 as customer__service__pb2
