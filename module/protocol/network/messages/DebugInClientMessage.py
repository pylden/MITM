from module.protocol.network.message import Message


class DebugInClientMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1327
        self.level = {"type": "uint", "value": ""}
        self.message = {"type": "String", "value": ""}
