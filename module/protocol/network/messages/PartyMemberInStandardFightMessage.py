from module.protocol.network.messages.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage


class PartyMemberInStandardFightMessage(AbstractPartyMemberInFightMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMemberInFightMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8731
        self.vars.append({"name": "fightMap", "type": "MapCoordinatesExtended", "value": ""})
