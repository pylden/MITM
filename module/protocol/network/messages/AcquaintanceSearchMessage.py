from module.protocol.network.message import Message


class AcquaintanceSearchMessage(Message):
    def __init__(self):
        self.id = 1282
        self.nickname = {"type": "String", "value": ""}
