from module.protocol.network.message import Message


class ObjectGroundRemovedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1247
        self.cell = {"type": "uint", "value": ""}
