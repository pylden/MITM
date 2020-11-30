from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyLocateMembersMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2685
        self.geopositions = {"type": "Vector.<PartyMemberGeoPosition>", "value": ""}
