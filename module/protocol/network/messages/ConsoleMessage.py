from module.protocol.network.message import Message


class ConsoleMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3514
        self.type = {"type": "uint", "value": ""}
        self.content = {"type": "String", "value": ""}
