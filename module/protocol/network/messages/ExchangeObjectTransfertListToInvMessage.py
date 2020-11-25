from module.protocol.network.message import Message


class ExchangeObjectTransfertListToInvMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 622
        self.ids = {"type": "Vector.<uint>", "value": ""}
