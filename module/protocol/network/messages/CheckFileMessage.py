from module.protocol.network.message import Message


class CheckFileMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8145
        self.filenameHash = {"type": "String", "value": ""}
        self.type = {"type": "uint", "value": ""}
        self.value = {"type": "String", "value": ""}
