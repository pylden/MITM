from module.protocol.network.message import Message


class ObjectMovementMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3380
        self.objectUID = {"type": "uint", "value": ""}
        self.position = {"type": "uint", "value": ""}
