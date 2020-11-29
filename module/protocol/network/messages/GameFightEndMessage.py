from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightEndMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1090
        self.vars.append({"name": "duration", "type": "uint", "value": ""})
        self.vars.append({"name": "rewardRate", "type": "int", "value": ""})
        self.vars.append({"name": "lootShareLimitMalus", "type": "int", "value": ""})
        self.vars.append({"name": "results", "type": "Vector.<FightResultListEntry>", "value": ""})
        self.vars.append({"name": "namedPartyTeamsOutcomes", "type": "Vector.<NamedPartyTeamWithOutcome>", "value": ""})
