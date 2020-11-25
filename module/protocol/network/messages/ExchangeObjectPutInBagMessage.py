from module.protocol.network.message import Message


class ExchangeObjectPutInBagMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6105
        self.object = {"type": "ObjectItem", "value": ""}
