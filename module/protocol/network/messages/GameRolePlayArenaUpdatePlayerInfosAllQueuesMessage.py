from module.protocol.network.message import Message


class GameRolePlayArenaUpdatePlayerInfosAllQueuesMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5122
        self.team = {"type": "ArenaRankInfos", "value": ""}
        self.duel = {"type": "ArenaRankInfos", "value": ""}
