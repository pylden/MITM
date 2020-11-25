from module.protocol.network.message import Message


class CheckFileMessage(Message):
    def __init__(self):
        self.id = 8145
        self.filenameHash = {"type": "String", "value": ""}
        self.value = {"type": "String", "value": ""}
