from module.protocol.network.message import Message


class PopupWarningMessage(Message):
    def __init__(self):
        self.id = 6411
        self.author = {"type": "String", "value": ""}
        self.content = {"type": "String", "value": ""}
