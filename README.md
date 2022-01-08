# TinkoffNewAPI
Мои личные наработки по новому API Тинькофф. Не официально.

Официально тут: https://github.com/Tinkoff/investAPI/

Выложено по просьбе в телеграмм канале https://t.me/joinchat/VaW05CDzcSdsPULM

Полезные команды из Windows, VSC:

pip install grpc
pip install grpcio-tools
python -m grpc_tools.protoc -I ./proto --python_out=. --grpc_python_out=. ./proto/users.proto
