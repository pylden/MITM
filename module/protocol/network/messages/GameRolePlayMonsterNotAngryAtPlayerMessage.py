from module.protocol.network.message import Message


class GameRolePlayMonsterNotAngryAtPlayerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1541
        self.playerId = {"type": "Number", "value": ""}
        self.monsterGroupId = {"type": "Number", "value": ""}
