import grpc
import users_pb2_grpc
import users_pb2

TOKEN = "MY TOKEN t.*******"



def run():
    credentials = grpc.ssl_channel_credentials(root_certificates=None, private_key=None, certificate_chain=None)   

    metadata = []
    metadata.append(('authorization', 'Bearer ' + TOKEN))
    with grpc.secure_channel(target = 'invest-public-api.tinkoff.ru:443', credentials = credentials,  options = metadata) as channel: #
        stub = users_pb2_grpc.UsersServiceStub(channel)
        response = stub.GetAccounts(users_pb2.GetAccountsRequest(), metadata=metadata)
        print(response)

if __name__ == '__main__':
    run()
