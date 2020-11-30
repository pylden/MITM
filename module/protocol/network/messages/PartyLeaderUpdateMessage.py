from module.protocol.network.messages.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyLeaderUpdateMessage(AbstractPartyEventMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyEventMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2432
        self.partyLeaderId = {"type": "Number", "value": ""}
