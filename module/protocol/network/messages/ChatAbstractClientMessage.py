from module.protocol.network.message import Message


class ChatAbstractClientMessage(Message):
    def __init__(self):
        self.id = 8438
        self.content = {"type": "String", "value": ""}
