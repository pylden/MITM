from module.protocol.network.message import Message


class PartyMemberInStandardFightMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8731
        self.fightMap = {"type": "MapCoordinatesExtended", "value": ""}
