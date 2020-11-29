from module.protocol.network.messages.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyMemberRemoveMessage(AbstractPartyEventMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyEventMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2903
        self.vars.append({"name": "leavingPlayerId", "type": "Number", "value": ""})
