from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyNameSetRequestMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1262
        self.partyName = {"type": "String", "value": ""}
