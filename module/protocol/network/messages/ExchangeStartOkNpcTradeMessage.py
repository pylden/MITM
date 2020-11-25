from module.protocol.network.message import Message


class ExchangeStartOkNpcTradeMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6982
        self.npcId = {"type": "Number", "value": ""}
