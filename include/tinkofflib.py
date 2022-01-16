from urllib import response
import grpc
import include.stoporders_pb2
import include.stoporders_pb2_grpc
import include.orders_pb2
import include.orders_pb2_grpc
import include.users_pb2
import include.users_pb2_grpc
import include.operations_pb2
import include.operations_pb2_grpc

# ok


def GetAccountsRequest(connection_data):
    stub = include.users_pb2_grpc.UsersServiceStub(connection_data['channel'])
    response = stub.GetAccounts(
        include.users_pb2.GetAccountsRequest(), metadata=connection_data['metadata'])
    print(response)
    return response

# ok


def GetMarginAttributesRequest(connection_data, account_id):
    stub = include.users_pb2_grpc.UsersServiceStub(connection_data['channel'])
    response = stub.GetMarginAttributes(
        include.users_pb2.GetMarginAttributesRequest(account_id=account_id), metadata=connection_data['metadata'])
    print(response)
    return response

# ok


def GetWithdrawLimitsRequest(connection_data, account_id):
    stub = include.operations_pb2_grpc.OperationsServiceStub(
        connection_data['channel'])
    response = stub.GetWithdrawLimits(include.operations_pb2.WithdrawLimitsRequest(
        account_id=account_id), metadata=connection_data['metadata'])
    print(response)
    return response


def GetChannel():
    credentials = grpc.ssl_channel_credentials(
        root_certificates=None, private_key=None, certificate_chain=None)
    channel = grpc.secure_channel(
        target='invest-public-api.tinkoff.ru:443', credentials=credentials)
    return channel
