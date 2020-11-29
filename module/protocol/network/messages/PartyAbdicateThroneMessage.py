from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyAbdicateThroneMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 793
        self.vars.append({"name": "playerId", "type": "Number", "value": ""})
