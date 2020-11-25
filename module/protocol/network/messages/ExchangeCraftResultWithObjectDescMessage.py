from module.protocol.network.message import Message


class ExchangeCraftResultWithObjectDescMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8570
        self.objectInfo = {"type": "ObjectItemNotInContainer", "value": ""}
