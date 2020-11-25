from module.protocol.network.message import Message


class DebugInClientMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1327
        self.message = {"type": "String", "value": ""}
