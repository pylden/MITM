from module.protocol.network.message import Message


class ExchangeMountsTakenFromPaddockMessage(Message):
    def __init__(self):
        self.id = 8081
        self.name = {"type": "String", "value": ""}
        self.ownername = {"type": "String", "value": ""}
