from module.protocol.network.message import Message


class ExchangeObjectRemovedFromBagMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1268
        self.objectUID = {"type": "uint", "value": ""}
