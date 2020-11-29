from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaLeagueRewardsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9791
        self.vars.append({"name": "seasonId", "type": "uint", "value": ""})
        self.vars.append({"name": "leagueId", "type": "uint", "value": ""})
        self.vars.append({"name": "ladderPosition", "type": "int", "value": ""})
        self.vars.append({"name": "endSeasonReward", "type": "Boolean", "value": ""})
