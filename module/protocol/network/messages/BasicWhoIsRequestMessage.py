from module.protocol.network.message import Message


class BasicWhoIsRequestMessage(Message):
    def __init__(self):
        self.id = 7214
        self.search = {"type": "String", "value": ""}
