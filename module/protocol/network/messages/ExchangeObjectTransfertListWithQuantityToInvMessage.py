from module.protocol.network.message import Message


class ExchangeObjectTransfertListWithQuantityToInvMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3741
        self.ids = {"type": "Vector.<uint>", "value": ""}
        self.qtys = {"type": "Vector.<uint>", "value": ""}
