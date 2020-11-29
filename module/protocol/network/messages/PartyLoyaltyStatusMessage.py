from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyLoyaltyStatusMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4294
        self.vars.append({"name": "loyal", "type": "Boolean", "value": ""})
