from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseItemAddOkMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4893
        self.vars.append({"name": "itemInfo", "type": "ObjectItemToSellInBid", "value": ""})
