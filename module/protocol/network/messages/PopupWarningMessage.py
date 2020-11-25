from module.protocol.network.message import Message


class PopupWarningMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6411
        self.lockDuration = {"type": "uint", "value": ""}
        self.author = {"type": "String", "value": ""}
        self.content = {"type": "String", "value": ""}
