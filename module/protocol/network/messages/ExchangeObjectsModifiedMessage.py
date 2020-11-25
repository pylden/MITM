from module.protocol.network.message import Message


class ExchangeObjectsModifiedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 363
        self.object = {"type": "Vector.<ObjectItem>", "value": ""}
