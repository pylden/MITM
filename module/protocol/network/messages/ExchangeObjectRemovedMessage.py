from module.protocol.network.message import Message


class ExchangeObjectRemovedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1377
        self.objectUID = {"type": "uint", "value": ""}
