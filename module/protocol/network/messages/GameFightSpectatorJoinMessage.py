from module.protocol.network.messages.GameFightJoinMessage import GameFightJoinMessage


class GameFightSpectatorJoinMessage(GameFightJoinMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameFightJoinMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6917
        self.vars.append({"name": "namedPartyTeams", "type": "Vector.<NamedPartyTeam>", "value": ""})
