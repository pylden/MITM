from module.protocol.network.message import Message


class ExchangeObjectMoveMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3601
        self.objectUID = {"type": "uint", "value": ""}
        self.quantity = {"type": "int", "value": ""}
