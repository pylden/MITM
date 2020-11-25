from module.protocol.network.message import Message


class ExchangeObjectTransfertListFromInvMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4400
        self.ids = {"type": "Vector.<uint>", "value": ""}
