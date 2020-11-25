from module.protocol.network.message import Message


class ObjectSetPositionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1317
        self.objectUID = {"type": "uint", "value": ""}
        self.position = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
