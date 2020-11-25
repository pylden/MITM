from module.protocol.network.message import Message


class ConsoleMessage(Message):
    def __init__(self):
        self.id = 3514
        self.content = {"type": "String", "value": ""}
