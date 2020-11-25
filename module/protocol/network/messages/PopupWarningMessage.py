from module.protocol.network.message import Message


class PopupWarningMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6411
        self.author = {"type": "String", "value": ""}
        self.content = {"type": "String", "value": ""}
