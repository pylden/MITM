from module.protocol.network.message import Message


class MapRunningFightDetailsExtendedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8300
        self.namedPartyTeams = {"type": "Vector.<NamedPartyTeam>", "value": ""}
