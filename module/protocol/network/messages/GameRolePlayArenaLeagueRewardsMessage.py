from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaLeagueRewardsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9791
        self.seasonId = {"type": "uint", "value": ""}
        self.leagueId = {"type": "uint", "value": ""}
        self.ladderPosition = {"type": "int", "value": ""}
        self.endSeasonReward = {"type": "Boolean", "value": ""}
