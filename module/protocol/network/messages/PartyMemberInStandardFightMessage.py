from module.protocol.network.message import Message


class PartyMemberInStandardFightMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8731
        self.fightMap = {"type": "MapCoordinatesExtended", "value": ""}
