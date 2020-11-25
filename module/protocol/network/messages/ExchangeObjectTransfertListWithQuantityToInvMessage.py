from module.protocol.network.message import Message


class ExchangeObjectTransfertListWithQuantityToInvMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3741
        self.ids = {"type": "Vector.<uint>", "value": ""}
        self.qtys = {"type": "Vector.<uint>", "value": ""}
