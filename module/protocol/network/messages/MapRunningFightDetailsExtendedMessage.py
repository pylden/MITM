from module.protocol.network.messages.MapRunningFightDetailsMessage import MapRunningFightDetailsMessage


class MapRunningFightDetailsExtendedMessage(MapRunningFightDetailsMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        MapRunningFightDetailsMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8300
        self.namedPartyTeams = {"type": "Vector.<NamedPartyTeam>", "value": ""}
