from module.protocol.network.message import Message


class ExchangeMountSterilizeFromPaddockMessage(Message):
    def __init__(self):
        self.id = 7328
        self.name = {"type": "String", "value": ""}
        self.sterilizator = {"type": "String", "value": ""}
