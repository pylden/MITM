from module.protocol.network.message import Message


class BasicWhoIsNoMatchMessage(Message):
    def __init__(self):
        self.id = 5493
        self.search = {"type": "String", "value": ""}
