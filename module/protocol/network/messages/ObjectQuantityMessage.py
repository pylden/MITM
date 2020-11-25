from module.protocol.network.message import Message


class ObjectQuantityMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9459
        self.objectUID = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
        self.origin = {"type": "uint", "value": ""}
