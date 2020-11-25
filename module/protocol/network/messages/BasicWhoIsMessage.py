from module.protocol.network.message import Message


class BasicWhoIsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6352
        self.accountNickname = {"type": "String", "value": ""}
        self.playerName = {"type": "String", "value": ""}
