from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyRestrictedMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2491
        self.restricted = {"type": "Boolean", "value": ""}
