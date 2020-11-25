from module.protocol.network.message import Message


class ExchangeOfflineSoldItemsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5913
        self.bidHouseItems = {"type": "Vector.<ObjectItemQuantityPriceDateEffects>", "value": ""}
        self.merchantItems = {"type": "Vector.<ObjectItemQuantityPriceDateEffects>", "value": ""}
