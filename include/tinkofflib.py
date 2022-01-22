import grpc
import uuid
from include.common_pb2 import Quotation
import include.stoporders_pb2
import include.stoporders_pb2_grpc
import include.orders_pb2
import include.orders_pb2_grpc
import include.users_pb2
import include.users_pb2_grpc
import include.operations_pb2
import include.operations_pb2_grpc
import include.marketdata_pb2
import include.marketdata_pb2_grpc
import include.instruments_pb2
import include.instruments_pb2_grpc


def GetAccountsRequest(connection_data):
    stub = include.users_pb2_grpc.UsersServiceStub(connection_data['channel'])
    response = stub.GetAccounts(
        include.users_pb2.GetAccountsRequest(), metadata=connection_data['metadata'])
    print(response)
    return response


def GetMarginAttributesRequest(connection_data, account_id):
    stub = include.users_pb2_grpc.UsersServiceStub(connection_data['channel'])
    response = stub.GetMarginAttributes(
        include.users_pb2.GetMarginAttributesRequest(account_id=account_id), metadata=connection_data['metadata'])
    print(response)
    return response


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

def GetPostOrderRequest(connection_data, account_id, figi, quantity, price, direction, order_type):
    order_id = uuid.uuid4()
    stub = include.orders_pb2_grpc.OrdersServiceStub(connection_data['channel'])
    # ВАЖНО!!! переделать множетель, подходит только для акций. Возможно другой для фьючерсов и т.д.
    price_Quotation = Quotation(units = int(price // 1), nano= int((price - (price // 1)) % 1 * 1000000000))
    response = stub.PostOrder(include.orders_pb2.PostOrderRequest(account_id=account_id, figi=figi, quantity=quantity, price=price_Quotation, direction=direction, order_type=order_type, order_id = order_id.hex), metadata=connection_data['metadata'])
    print(response)
    return response

def GetOrderBookRequest(connection_data, figi, depth = 1):
    stub = include.marketdata_pb2_grpc.MarketDataServiceStub(connection_data['channel'])
    response = stub.GetOrderBook(include.marketdata_pb2.GetOrderBookRequest(figi=figi, depth=depth), metadata=connection_data['metadata'])
    print(response)
    return response    

def GetTradingStatusRequest(connection_data, figi):
    stub = include.marketdata_pb2_grpc.MarketDataServiceStub(connection_data['channel'])
    response = stub.GetTradingStatus(include.marketdata_pb2.GetTradingStatusRequest(figi=figi), metadata=connection_data['metadata'])
    print(response)
    return response    

def InstrumentByfigiRequest(connection_data, figi):
    stub = include.instruments_pb2_grpc.InstrumentsServiceStub(connection_data['channel'])
    response = stub.GetInstrumentBy(include.instruments_pb2.InstrumentRequest(id_type = 1, id = figi), metadata=connection_data['metadata'])
    print(response)
    return response    

def PortfolioRequest(connection_data, account_id):
    stub = include.operations_pb2_grpc.OperationsServiceStub(connection_data['channel'])
    response = stub.GetPortfolio(include.operations_pb2.PortfolioRequest(account_id=account_id), metadata=connection_data['metadata'])
    print(response)
    return response 

def GetOrdersRequest(connection_data, account_id):
    stub = include.orders_pb2_grpc.OrdersServiceStub(connection_data['channel'])
    response = stub.GetOrders(include.orders_pb2.GetOrdersRequest(account_id=account_id), metadata=connection_data['metadata'])
    print(response)
    return response     


def CancelOrderRequest(connection_data, order_id):
    stub = include.orders_pb2_grpc.OrdersServiceStub(connection_data['channel'])
    response = stub.CancelOrder(include.orders_pb2.CancelOrderRequest(order_id=order_id), metadata=connection_data['metadata'])
    print(response)
    return response         
