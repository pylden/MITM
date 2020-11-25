from module.protocol.network.message import Message


class GameRolePlayArenaUpdatePlayerInfosAllQueuesMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5122
        self.team = {"type": "ArenaRankInfos", "value": ""}
        self.duel = {"type": "ArenaRankInfos", "value": ""}
