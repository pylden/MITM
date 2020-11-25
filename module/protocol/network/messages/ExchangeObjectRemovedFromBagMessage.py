from module.protocol.network.message import Message


class ExchangeObjectRemovedFromBagMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1268
        self.objectUID = {"type": "uint", "value": ""}
