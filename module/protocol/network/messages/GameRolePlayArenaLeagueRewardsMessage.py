from module.protocol.network.message import Message


class GameRolePlayArenaLeagueRewardsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9791
        self.seasonId = {"type": "uint", "value": ""}
        self.leagueId = {"type": "uint", "value": ""}
        self.ladderPosition = {"type": "int", "value": ""}
        self.endSeasonReward = {"type": "Boolean", "value": ""}
