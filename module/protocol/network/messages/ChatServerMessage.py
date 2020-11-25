from module.protocol.network.message import Message


class ChatServerMessage(Message):
    def __init__(self):
        self.id = 5722
        self.senderName = {"type": "String", "value": ""}
        self.prefix = {"type": "String", "value": ""}
