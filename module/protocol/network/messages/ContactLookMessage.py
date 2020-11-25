from module.protocol.network.message import Message


class ContactLookMessage(Message):
    def __init__(self):
        self.id = 6821
        self.playerName = {"type": "String", "value": ""}
