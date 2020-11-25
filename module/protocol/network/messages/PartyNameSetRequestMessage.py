from module.protocol.network.message import Message


class PartyNameSetRequestMessage(Message):
    def __init__(self):
        self.id = 1262
        self.partyName = {"type": "String", "value": ""}
