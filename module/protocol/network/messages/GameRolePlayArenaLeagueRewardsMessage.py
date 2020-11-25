from module.protocol.network.message import Message


class GameRolePlayArenaLeagueRewardsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9791
        self.seasonId = {"type": "uint", "value": ""}
        self.leagueId = {"type": "uint", "value": ""}
        self.ladderPosition = {"type": "int", "value": ""}
        self.endSeasonReward = {"type": "Boolean", "value": ""}
