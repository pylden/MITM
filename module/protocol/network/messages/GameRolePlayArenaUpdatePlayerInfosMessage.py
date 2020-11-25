from module.protocol.network.message import Message


class GameRolePlayArenaUpdatePlayerInfosMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9640
        self.solo = {"type": "ArenaRankInfos", "value": ""}
