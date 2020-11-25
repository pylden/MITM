from module.protocol.network.message import Message


class MapRunningFightDetailsExtendedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8300
        self.namedPartyTeams = {"type": "Vector.<NamedPartyTeam>", "value": ""}
