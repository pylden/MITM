from module.protocol.network.message import Message


class HavenBagDailyLoteryMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9224
        self.returnType = {"type": "uint", "value": ""}
        self.gameActionId = {"type": "String", "value": ""}
