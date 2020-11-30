from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeOfflineSoldItemsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5913
        self.bidHouseItems = {"type": "Vector.<ObjectItemQuantityPriceDateEffects>", "value": ""}
        self.merchantItems = {"type": "Vector.<ObjectItemQuantityPriceDateEffects>", "value": ""}
