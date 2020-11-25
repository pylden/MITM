from module.protocol.network.message import Message


class PartyNameSetRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1262
        self.partyName = {"type": "String", "value": ""}
