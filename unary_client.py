import grpc
from include.tinkofflib import GetAccountsRequest, GetWithdrawLimitsRequest, GetChannel, GetMarginAttributesRequest
from config import account_id, TOKEN


if __name__ == '__main__':
    channel = GetChannel()
    metadata = []
    metadata.append(('authorization', 'Bearer ' + TOKEN))
    connection_data = {'channel': channel, 'metadata': metadata}
    with channel:
        GetAccountsRequest(connection_data)
        #GetMarginAttributesRequest(channel, metadata, account_id)
        GetWithdrawLimitsRequest(connection_data, account_id)
    pass