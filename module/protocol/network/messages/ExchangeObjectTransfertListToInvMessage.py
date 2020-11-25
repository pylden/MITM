from module.protocol.network.message import Message


class ExchangeObjectTransfertListToInvMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 622
        self.ids = {"type": "Vector.<uint>", "value": ""}
