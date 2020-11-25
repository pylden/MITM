from module.protocol.network.message import Message


class ObjectAddedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4410
        self.object = {"type": "ObjectItem", "value": ""}
        self.origin = {"type": "uint", "value": ""}
