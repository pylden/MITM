from module.protocol.network.message import Message


class PartyJoinMessage(Message):
    def __init__(self):
        self.id = 4142
        self.partyName = {"type": "String", "value": ""}
