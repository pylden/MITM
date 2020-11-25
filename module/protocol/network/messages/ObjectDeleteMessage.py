from module.protocol.network.message import Message


class ObjectDeleteMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3368
        self.objectUID = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
