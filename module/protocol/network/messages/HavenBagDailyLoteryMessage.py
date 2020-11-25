from module.protocol.network.message import Message


class HavenBagDailyLoteryMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9224
        self.returnType = {"type": "uint", "value": ""}
        self.gameActionId = {"type": "String", "value": ""}
