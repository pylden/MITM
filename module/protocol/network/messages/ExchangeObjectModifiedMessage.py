from module.protocol.network.message import Message


class ExchangeObjectModifiedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6307
        self.object = {"type": "ObjectItem", "value": ""}
