from module.protocol.network.message import Message


class ChatClientPrivateMessage(Message):
    def __init__(self):
        self.id = 9769
        self.receiver = {"type": "String", "value": ""}
