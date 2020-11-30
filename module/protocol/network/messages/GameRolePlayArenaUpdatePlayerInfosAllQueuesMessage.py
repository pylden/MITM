from module.protocol.network.messages.GameRolePlayArenaUpdatePlayerInfosMessage import GameRolePlayArenaUpdatePlayerInfosMessage


class GameRolePlayArenaUpdatePlayerInfosAllQueuesMessage(GameRolePlayArenaUpdatePlayerInfosMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameRolePlayArenaUpdatePlayerInfosMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5122
        self.team = {"type": "ArenaRankInfos", "value": ""}
        self.duel = {"type": "ArenaRankInfos", "value": ""}
