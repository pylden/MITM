from module.protocol.network.message import Message


class ContactLookRequestByNameMessage(Message):
    def __init__(self):
        self.id = 2201
        self.playerName = {"type": "String", "value": ""}
