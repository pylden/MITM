from module.protocol.network.message import Message


class ExchangeMountsTakenFromPaddockMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8081
        self.name = {"type": "String", "value": ""}
        self.ownername = {"type": "String", "value": ""}
