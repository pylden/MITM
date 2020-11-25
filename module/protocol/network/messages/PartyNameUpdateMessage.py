from module.protocol.network.message import Message


class PartyNameUpdateMessage(Message):
    def __init__(self):
        self.id = 6017
        self.partyName = {"type": "String", "value": ""}
