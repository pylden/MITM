from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseUnsoldItemsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5367
        self.items = {"type": "Vector.<ObjectItemGenericQuantity>", "value": ""}
