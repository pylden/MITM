from module.protocol.network.message import Message


class BasicWhoIsMessage(Message):
    def __init__(self):
        self.id = 6352
        self.accountNickname = {"type": "String", "value": ""}
        self.playerName = {"type": "String", "value": ""}
