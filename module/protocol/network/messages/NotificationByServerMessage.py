from module.protocol.network.message import Message


class NotificationByServerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 312
        self.id = {"type": "uint", "value": ""}
        self.parameters = {"type": "Vector.<String>", "value": ""}
        self.forceOpen = {"type": "Boolean", "value": ""}
