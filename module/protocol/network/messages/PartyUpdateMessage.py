from module.protocol.network.messages.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyUpdateMessage(AbstractPartyEventMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyEventMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4697
        self.vars.append({"name": "memberInformations", "type": "PartyMemberInformations", "value": ""})
