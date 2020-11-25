from module.protocol.network.message import Message


class ChatServerCopyMessage(Message):
    def __init__(self):
        self.id = 5867
        self.receiverName = {"type": "String", "value": ""}
