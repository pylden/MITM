from module.protocol.network.message import Message


class NotificationByServerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 312
        self.id = {"type": "uint", "value": ""}
        self.parameters = {"type": "Vector.<String>", "value": ""}
        self.forceOpen = {"type": "Boolean", "value": ""}
