from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyCannotJoinErrorMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4290
        self.vars.append({"name": "reason", "type": "uint", "value": ""})
