from module.protocol.network.message import Message


class HavenBagDailyLoteryMessage(Message):
    def __init__(self):
        self.id = 9224
        self.gameActionId = {"type": "String", "value": ""}
