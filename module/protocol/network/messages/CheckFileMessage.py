from module.protocol.network.message import Message


class CheckFileMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8145
        self.filenameHash = {"type": "String", "value": ""}
        self.type = {"type": "uint", "value": ""}
        self.value = {"type": "String", "value": ""}
