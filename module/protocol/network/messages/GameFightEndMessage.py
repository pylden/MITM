from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightEndMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1090
        self.duration = {"type": "uint", "value": ""}
        self.rewardRate = {"type": "int", "value": ""}
        self.lootShareLimitMalus = {"type": "int", "value": ""}
        self.results = {"type": "Vector.<FightResultListEntry>", "value": ""}
        self.namedPartyTeamsOutcomes = {"type": "Vector.<NamedPartyTeamWithOutcome>", "value": ""}
