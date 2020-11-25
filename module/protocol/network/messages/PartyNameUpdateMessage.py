from module.protocol.network.message import Message


class PartyNameUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6017
        self.partyName = {"type": "String", "value": ""}
