from module.protocol.network.message import Message


class PartyLocateMembersMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2685
        self.geopositions = {"type": "Vector.<PartyMemberGeoPosition>", "value": ""}
